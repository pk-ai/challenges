# python3 driver_3.py 000000000302540000050301070000000004409006005023054790000000050700810000080060009
# Should print the output as
# 148697523372548961956321478567983214419276385823154796691432857735819642284765139
import sys, copy
import itertools
variables = dict()
variableConsts = [
    'A1','A2','A3','A4','A5','A6','A7','A8','A9',
    'B1','B2','B3','B4','B5','B6','B7','B8','B9',
    'C1','C2','C3','C4','C5','C6','C7','C8','C9',
    'D1','D2','D3','D4','D5','D6','D7','D8','D9',
    'E1','E2','E3','E4','E5','E6','E7','E8','E9',
    'F1','F2','F3','F4','F5','F6','F7','F8','F9',
    'G1','G2','G3','G4','G5','G6','G7','G8','G9',
    'H1','H2','H3','H4','H5','H6','H7','H8','H9',
    'I1','I2','I3','I4','I5','I6','I7','I8','I9']
constraints = [
    ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'],
    ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'],
    ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
    ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'],
    ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'],
    ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'],
    ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'],
    ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'],
    ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'],
    ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'],
    ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
    ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'],
    ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'],
    ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'],
    ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'],
    ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'],
    ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'],
    ['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'],
    ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'],
    ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3'],
    ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3'],
    ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6'],
    ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6'],
    ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6'],
    ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9'],
    ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9'],
    ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']
]
domains = ['1','2','3','4','5','6','7','8','9']

def backtrack(var_with_vals):
    if assignmentComplete(var_with_vals): return var_with_vals
    var_copy_with_vals = copy.deepcopy(var_with_vals)
    unassigned_var = getUnAssignedValue(var_copy_with_vals)
    reduced_domains = getReducedDomains(var_copy_with_vals, domains[:], unassigned_var)
    # As per definition of Forward Checking(FC)
    # Def: Keep track of remaining legal values for the unassigned variables. Terminate when any variable has no legal values.
    # Here the Forward checking Heuristic also integrated
    # Since the reduced_domains may return an empty list []
    # for which we are not proceeding further
    for el in reduced_domains:
        var_copy_with_vals[unassigned_var] = el
        if alldiff(var_copy_with_vals):
            result = backtrack(var_copy_with_vals)
            if result != 1: return result
        var_copy_with_vals[unassigned_var] = '0'
    return 1

# Minimum Remaining Value(MRV) Heuristic
# Def: Choose the variable with the fewest legal values in its domain. Pick the hardest.!
def getReducedDomains(varVals, orgDomains, unassigned_var):
    # Reducing the domain by checking the applicable constraints
    # Get the applicable constraints which have the unassigned_var. i.e. 
    # Application row wise, column wise and 3x3 box wise
    # From the applicable constraints, get only assigned vars and not the
    # unassigned_var to build assigned_vars
    assigned_vars = []
    for constraint in constraints:
        if unassigned_var in constraint:
            for el in constraint:
                if el != unassigned_var and el not in assigned_vars and varVals.get(el, '0') != '0':
                    assigned_vars.append(el)
    # From the built assigned vars, get the values and remove them from the domains
    for el in assigned_vars:
        if varVals[el] in orgDomains:
            orgDomains.remove(varVals[el])
    # Returning reduced domain
    return orgDomains

def alldiff(varVals):
    for list1 in constraints:
        for a, b in itertools.combinations(list1, 2):
            if varVals.get(a, 'x') == varVals.get(b, 'y'):
                return False
    return True

def assignmentComplete(varDict):
    for el in variableConsts:
        if varDict.get(el, '0') == '0':
            return False
    return True

def getUnAssignedValue(var_dict):
    for el in variableConsts:
        if var_dict.get(el, '0') == '0':
            return el

if __name__ == '__main__':
    inputSudoku = list(sys.argv[1])
    for key, el in zip(variableConsts, inputSudoku):
        if el != '0':
            variables[key] = el
    result = backtrack(variables)
    final_res = ''
    for el in variableConsts:
        final_res += result[el]
    print(final_res)