import numpy as np

def best_combination(matrix):
    adjusted_matrix = []
    
    for i in range(len(matrix[0])):
        column = [matrix[j][i] for j in range(len(matrix))]
        adjusted_matrix.append(column)
    
    return adjusted_matrix

def find_units(array, constraint_limits):
    ratio_arr = [array[i] / constraint_limits[i] for i in range(len(array))]
    limit_ratio = max(ratio_arr)
    limit_index = ratio_arr.index(limit_ratio)
    limit = array[limit_index]
    
    return constraint_limits[limit_index] // limit

def solo_profit(units, coefficients):
    unit_profit = units * coefficients
    return unit_profit

def profit(array, coefficients):
    profit = sum(array[i] * coefficients[i] for i in range(len(array)))
    return profit
        
def main():
    # Testcase 1 (Chemical Factory)
    variables = 3
    matrix = [[2, 1, 8], [4, 2, 0], [5, 4, 3]]
    constraint_limits = [300, 200, 300]
    coefficients = [3000, 2000, 2000]

    # Testcase 2 (Pants and Jackets)
    # variables = 2
    # matrix = [[2, 2], [3, 1]]
    # constraint_limits = [1500, 1000]
    # coefficients = [50, 40]

    const_count = len(constraint_limits)

    const_print = ', '.join([f"CONSTRAINT {i+1}" for i in range(const_count)])
    print("[SUPPLY, " + const_print + ", PROFIT]")
    for i in range(variables):
        row = matrix[i]
        row_str = ', '.join(str(val) for val in row)
        coefficient = coefficients[i]
        print(f"[variable {i+1}, {row_str}, {coefficient}]")
    constraint_str = ', '.join(str(val) for val in constraint_limits)
    print(f"[AVAILABILITY, {constraint_str}]")

    adjusted_matrix = best_combination(matrix)
    A = np.array(adjusted_matrix)
    b = np.array(constraint_limits)
    x = np.linalg.inv(A).dot(b)
    
    for i in range(len(matrix)):
        units_for_variable = find_units(matrix[i], constraint_limits)
        profit_for_variable = solo_profit(units_for_variable, coefficients[i])
        
        print(f"If only variable {i+1} is made, there would be a profit of: {profit_for_variable}. The number of units would be {units_for_variable}.")

    best_profit = profit(x, coefficients)
    print(f"The balanced amount is {best_profit}. The breakdown is: {x} of each of the variables")
    print(f"The best possible solution is {best_profit} using the Balanced method.")


main()


# Testcase 1 (Chemical Factory) Output
# Please enter the number of variables: 3
# Enter the data for the square matrix stating the constraints, separate each row with a semicolon and each value with a space (ex. 2 1 8:4 2 0:5 4 3): 2 1 8:4 2 0:5 4 3
# Enter the coefficients of each variable for the objective function with a space separating each (ex. 3000 2000 2000): 3000 2000 2000
# Enter the constraint limits with a space separating each (ex. 300 200 300): 300 200 300
# [SUPPLY, CONSTRAINT 1, CONSTRAINT 2, CONSTRAINT 3, PROFIT]
# [variable 1, 2, 1, 8, 3000]
# [variable 2, 4, 2, 0, 2000]
# [variable 3, 5, 4, 3, 2000]
# [AVAILABILITY, 300, 200, 300]
# If only variable 1 is made, there would be a profit of: 111000. The number of units would be 37.
# If only variable 2 is made, there would be a profit of: 150000. The number of units would be 75.
# If only variable 3 is made, there would be a profit of: 100000. The number of units would be 50.
# The balanced amount is 183333.3333333333. The breakdown is: [25.         20.83333333 33.33333333] of each of the variables
# The best possible solution is 183333.3333333333 using the Balanced method.


# Testcase 2 (Pants and Jackets) Output
# Please enter the number of variables: 2
# Enter the data for the square matrix stating the constraints, separate each row with a semicolon and each value with a space (ex. 2 1 8:4 2 0:5 4 3): 2 2:3 1
# Enter the coefficients of each variable for the objective function with a space separating each (ex. 3000 2000 2000): 50 40
# Enter the constraint limits with a space separating each (ex. 300 200 300): 1500 1000
# [SUPPLY, CONSTRAINT 1, CONSTRAINT 2, PROFIT]
# [variable 1, 2, 2, 50]
# [variable 2, 3, 1, 40]
# [AVAILABILITY, 1500, 1000]
# If only variable 1 is made, there would be a profit of: 25000. The number of units would be 500.
# If only variable 2 is made, there would be a profit of: 20000. The number of units would be 500.
# The balanced amount is 28750.0. The breakdown is: [375. 250.] of each of the variables
# The best possible solution is 28750.0 using the Balanced method.