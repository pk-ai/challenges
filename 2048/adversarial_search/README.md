# 2048 Game solving using Adversarial Search.

> python3 GameManager.py

### Minimax algorithm with Alpha-Beta Pruning
```
function MINIMIZE(state, alpha, beta) returns Tuple of (state, utility):
    if terminal_test(state):
        return (null, eval(state))
    (minChild, minUtility) = (null, Infinity)
    for child in state.children():
        (_, utility) = MAXIMIZE(child, alpha, beta)
        if utility < minUtility:
            (minChild, minUtility) = (child, utility)
        if minUtility <= alpha:
            break;
        if minUtility < beta:
            beta = minUtility
    return (minChild, minUtility)

function MAXIMIZE(state, alpha, beta) returns Tuple of (state, utility):
    if terminal_test(state):
        return (null, eval(state))
    (maxChild, maxUtility) = (null, -Infinity)
    for child in state.children():
        (_, utility) = MINIMIZE(child, alpha, beta)
        if utility < maxUtility:
            (maxChild, maxUtility) = (child, utility)
        if maxUtility >= beta:
            break;
        if maxUtility > alpha:
            beta = maxUtility
    return (maxChild, maxUtility)

function DECISION(state) returns state:
    (child, _) = MAXIMIZE(state, -Infinity, Infinity)
    return child
```