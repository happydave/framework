# Forgejo (private forge, `ro-anchor`)

Reference material, non-normative. Policy lives in `skills/tooling.md`.

Recorded 2026-09-02 during WI 1257 (renaming the Sounding repo).

## Access shape

The instance runs as systemd `forgejo.service` on host `ro-anchor` (`172.234.38.82`), user/group
`git`, config `/etc/forgejo/app.ini`, work dir `/var/lib/forgejo`.

- **The HTTP API binds `127.0.0.1:3000` only.** Ports 80 and 443 are not served. From a workstation
  the API is therefore unreachable — `curl` to the host times out — while git over SSH works fine.
  Do not read a timeout as "the server is down"; it is bound to loopback by design.
- Reach the API by SSH'ing in first: `ssh dave@172.234.38.82`, then `curl http://127.0.0.1:3000/...`.
  That account has a shell and sudo. The `git` user does not (git-shell only).
- **Sign-in is required for every API call**, including `/api/v1/version` and public-looking repo
  reads — unauthenticated calls return `403 {"message":"Only signed in user is allowed to call APIs."}`.
- Database is **sqlite3** at `/var/lib/forgejo/forgejo.db`. There is **no `sqlite3` binary
  installed**; `python3` is present and its stdlib driver works (run it as the `git` user so file
  ownership is preserved).
- No `tea` CLI installed and no token config on the box.

## Auth quirks

**A token cannot revoke itself.** Forgejo's token endpoints
(`GET|POST|DELETE /api/v1/users/{username}/tokens[/{name}]`) are gated behind `reqBasicAuth`,
inherited from Gitea. Presenting a valid access token to `DELETE .../tokens/{name}` returns **401**
regardless of the token's scopes — `write:user` does not help. Basic auth is the only accepted
credential there, and it is unavailable when the account has 2FA enabled.

Consequence: **verify the revocation path before minting a token, not after.** The mint→use→revoke
pattern silently leaves a live credential if you assume the API can close the loop.

Working revocation when basic auth is not available: delete the row from the `access_token` table.

```
sudo -n -u git python3 -c "
import sqlite3
c = sqlite3.connect('/var/lib/forgejo/forgejo.db', timeout=15)
print(c.execute(\"delete from access_token where name=?\", ('TOKEN-NAME',)).rowcount)
c.commit()"
```

Inspect the table read-only first (`mode=ro` URI) and delete by exact name/id — the table holds
other people's long-lived tokens. Forgejo authenticates tokens by DB lookup per request, so removing
the row is the revocation; no service restart is needed.

## Minting without leaking the value

`forgejo admin user generate-access-token -u <user> -t <name> --scopes <scopes> --raw
--config /etc/forgejo/app.ini` prints the token on stdout. Capture it into a shell variable inside a
single remote session and pass it to curl via a config on stdin, so it never lands in argv (`ps`),
shell history, or the session transcript:

```
auth() { printf 'header = "Authorization: token %s"\n' "$TOK"; }
auth | curl -sK - "$API/repos/owner/repo"
```

## Repo rename

`forgejo admin` has **no repo-rename subcommand** (only `user`, `repo-sync-releases`, `regenerate`,
`auth`, `sendmail`). Renaming must go through `PATCH /api/v1/repos/{owner}/{repo}` with
`{"name":"<new>"}` and scope `write:repository`.

Do **not** rename by moving the bare repository directory — the name is a database record, and a
filesystem-only move desynchronises Forgejo from its own DB.

**Forgejo does not redirect old SSH paths after a rename** (unlike GitHub, which keeps the old
`git@github.com:owner/old.git` working). Every checkout pointing at the old URL breaks immediately
and needs `git remote set-url`. Sweep for other clones before renaming a shared repo.
