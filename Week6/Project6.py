import numpy as np

def get_variables():
    variables = int(input("Please enter the number of variables: "))
    return variables

def get_matrix():
    matrix = eval(input("Enter the data for the square matrix using stating the constraints (ex. [[2, 1, 8], [4, 2, 0], [5, 4, 3]]): "))
    return matrix

def get_const():
    constraint_limits = eval(input("Enter the constraint limits (ex. [300, 200, 300]): "))
    return constraint_limits

def get_coefficients():
    coeffiecients = input("Enter the coefficients of each variable for the objective function (ex. 3000, 2000, 2000): ")
    return coeffiecients

def best_combination(matrix):
    arr_one = []
    arr_two = []
    arr_three = []

    for i in matrix:
        arr_one.append(i[0])
        if len(i) > 1:
            arr_two.append(i[1])
        if len(i) > 2:
            arr_three.append(i[2])

    return [arr_one] + [arr_two] + [arr_three]

def profit(array, coefficients):
    profit = sum(array[i] * coefficients[i] for i in range(len(array)))
    return profit
        
def main():
    variables = 3
    matrix = [[2, 1, 8], [4, 2, 0], [5, 4, 3]]
    constraint_limits = [300, 200, 300]
    coefficients = [3000, 2000, 2000]
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
        profit_for_variable = profit([matrix[i]], coefficients)
        print(f"If only variable {i+1} is made, there would be a profit of: {profit_for_variable}. The number of units would be {matrix[i]}.")


    best_profit = profit(x, coefficients)
    print(f"The balanced amount is {best_profit}. The breakdown is: {x} of each of the variables")
    print(f"The best possible solution is {best_profit} using the Balanced method.")



main()
