# Constraint Satisfaction Problem

# Backtracking Search

```
function backtracking_search(csp) returns a solution or failure
    return backtrack({}, csp)

function backtrack(assignment, csp) returns a solution or failure
    if assignment is complete then return assignment
    var = select_unassigned_variable(csp)
    for each value in order_domain_values(var, assignment, csp)
        if value is consistent with assignment then
            add { var = value } to assignment
            # Recursion
            result = backtrack(assignment, csp) 
            if result != failure
                return result
        remove { var = value } from assignment
    return failure
```

# Arc Consistency AC3

```
function ac3(csp) returns False if an inconsistency is found, True otherwise
inputs: csp, a binary CSP with components (X, D, C)
local variables: queue, a queue of arcs, initially all arcs in csp
while queue is not empty do
    (Xi, Xj) = REMOVE-FIRST(queue)
    if REVISE(csp, Xi, Xj) then
        if size of Di = 0 then return False
        for each Xk in Xi.Neighbors - {Xj} do
            add (Xk, Xi) to queue
return true

function REVISE(csp, Xi, Xj) returns True iff we revise the domain of Xi
revised = False
for each x in Di, do
    if no value y in Dj allows (x,y) to satisfy the constraint between Xi and Xj then
        delete x from Di
        revised = True
return revised
```