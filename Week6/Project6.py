import numpy as np

def get_variables():
    while True:
        try:
            variables = int(input("Please enter the number of variables: "))
            return variables
        except:
            print("Please enter an integer.")

def get_matrix():
    while True:
        try:
            mat_input = input("Enter the data for the square matrix stating the constraints, separate each row with a semicolon and each value with a space (ex. 2 1 8:4 2 0:5 4 3): ")
            mat_rows = mat_input.split(":")
            matrix = [list(map(int, row.split())) for row in mat_rows]
            return matrix
        except:
            print("Please follow the example matrix format.")

def get_const():
    while True:
        try:
            constraint_limits = input("Enter the constraint limits with a space separating each (ex. 300 200 300): ")
            constraint_limits = list(map(int, constraint_limits.split()))
            return constraint_limits
        except:
            print("Please follow the example constraints format.")

def get_coefficients():
    while True:
        try:
            coeffiecients = input("Enter the coefficients of each variable for the objective function with a space separating each (ex. 3000 2000 2000): ")
            coeffiecients = list(map(int, coeffiecients.split()))
            return coeffiecients
        except:
            print("Please follow the example coefficients format.")

def best_combination(matrix):
    """
    best_combination(): Returns converted matrix from one that prints out the table to one that can be used in numpy.
    """
    adjusted_matrix = []
    
    for i in range(len(matrix[0])):
        column = [matrix[j][i] for j in range(len(matrix))]
        adjusted_matrix.append(column)
    
    return adjusted_matrix

def find_units(array, constraint_limits):
    """
    find_units(): Finds the number of units by finding the limiting ratio of each subarray to its constraint, 
    then divides the constraint by the value in that index to get units.
    Parameters: An array and its constraints.
    """
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
    try:
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
    except:
        print("Incorrect inputs. Please try again using the correct format and values.")


main()
