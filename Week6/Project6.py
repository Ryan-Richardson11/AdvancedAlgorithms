import numpy as np

def get_variables():
    """
    get_variable(): Takes user input for number of variables and returns it.
    """
    while True:
        try:
            variables = int(input("Please enter the number of variables: "))
            return variables
        except:
            print("Please enter an integer.")

def get_matrix():
    """
    get_matrix(): Takes user input representing the matrix and returns it.
    """
    while True:
        try:
            mat_input = input("Enter the data for the square matrix stating the constraints, separate each row with a semicolon and each value with a space (ex. 2 1 8:4 2 0:5 4 3): ")
            mat_rows = mat_input.split(":")
            matrix = [list(map(int, row.split())) for row in mat_rows]
            return matrix
        except:
            print("Please follow the example matrix format.")

def get_const():
    """
    get_const(): Takes user input for the constraints and returns it.
    """
    while True:
        try:
            constraint_limits = input("Enter the constraint limits with a space separating each (ex. 300 200 300): ")
            constraint_limits = list(map(int, constraint_limits.split()))
            return constraint_limits
        except:
            print("Please follow the example constraints format.")

def get_coefficients():
    """
    get_coefficients(): Takes user input for the coefficients and returns it.
    """
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
    """
    solo_profit(): Takes the units from find_units() and calculates profit when only making one option.
    Parameters: number of units and the corresponding coefficient.
    """
    unit_profit = units * coefficients
    return unit_profit

def profit(array, coefficients):
    """
    profit(): Returns the profit for the most optimal scenario.
    Parameters: An array and its corresponding coefficients.
    """
    profit = sum(array[i] * coefficients[i] for i in range(len(array)))
    return profit
        
def main():
    """
    main(): Sets all variables by taking user input.
    Prints out a formatted table with all of the data.
    Finds the most optimal combination, and the profit for each option alone.
    """
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