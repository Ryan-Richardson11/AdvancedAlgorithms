import numpy as np






# def main():

#     # variables = int(input("Please enter the number of variables: "))
#     # matrix = eval(input("Enter the data for the square matrix using stating the constraints (ex. [[2,4,5], [1,2,4], [8,0,3]]): "))
#     # constraint_limits = eval(input("Enter the constraint limits (ex. [300, 200, 300]): "))
#     # coeffiecients = input("Enter the coefficients of each variable for the objective function (ex. 3000, 2000, 2000): ")

#     variables = 3
#     matrix = [[2,4,5], [1,2,4], [8,0,3]]
#     constraint_limits = [300, 200, 300]
#     coefficients = 3000, 2000, 2000


#     # A = np.array(matrix)
#     A = np.array([[4, 1, 8], [4, 2, 0], [5, 4, 3])
#     # inv_A = np.linalg.inv(A)
#     inv_A = np.linalg.inv(A)
#     # b = np.array(constraint_limits)
#     b = np.array([300, 200, 300])
#     # x = np.linalg.inv(A).dot(b)
#     x = np.linalg.inv(A).dot(b)

#     for i in range(variables):
#         mat_row = matrix[i]
#         const = constraint_limits[i]
#         coefficient = coefficients[i]

#         row_str = ', '.join(str(val) for val in mat_row)
#         row_str2 = ', '.join(const)
#         print(f"Variable {i+1}, {row_str}, {coefficient}")

#         print(f"AVAILABILITY, {row_str2}")
    
    

def main():
    variables = 3
    matrix = [[4, 1, 8], [4, 2, 0], [5, 4, 3]]
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



main()



