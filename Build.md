Build Framework

1. read project spec from 00_Project.spec
2. read next pending feature spec from XX_Feature.spec
3. assess if sufficient detail is available to complete work on the next feature
    - if not, stop and consult human
(4 and 5 may be done in reverse order)
4. build feature
5. build test
6. run test
7. criticall assess - review work for completeness, correctness

**Repeat if needed**
- Repeat steps as needed until the Critical Assess step confirms the feature is complete and testing shows it is functional.

**After Critical Assess complete (feature ready):**
- Record any major issues or adjustments in the relevant spec(s)
- Mark feature as **Complete**
- Optionally update `00_Project.spec` with cross-feature insights

**Phase Mini-Retrospective**  
List significant problems, research gaps, extra iterations, unplanned human interventions, or items warranting framework changes.
