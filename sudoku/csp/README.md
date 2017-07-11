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