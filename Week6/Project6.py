import numpy as np

def get_variables():
    variables = int(input("Please enter the number of variables: "))
    return variables

def get_matrix():
    mat_input = input("Enter the data for the square matrix using stating the constraints (ex. 2 1 8:4 2 0:5 4 3): ")
    mat_rows = mat_input.split(":")
    matrix = [list(map(int, row.split())) for row in mat_rows]
    return matrix

def get_const():
    constraint_limits = input("Enter the constraint limits (ex. 300 200 300): ")
    constraint_limits = list(map(int, constraint_limits.split()))
    return constraint_limits

def get_coefficients():
    coeffiecients = input("Enter the coefficients of each variable for the objective function (ex. 3000 2000 2000): ")
    coeffiecients = list(map(int, coeffiecients.split()))
    return coeffiecients

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
    variables = get_variables()
    matrix = get_matrix()
    coefficients = get_coefficients()
    constraint_limits = get_const()

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
