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
#     A = np.array([[2,4,5], [1,2,4], [8,0,3]])
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
    matrix = [[2, 4, 5], [1, 2, 4], [8, 0, 3]]
    constraint_limits = [300, 200, 300]
    coefficients = [3000, 2000, 2000]

    A = np.array(matrix)
    inv_A = np.linalg.inv(A)
    b = np.array(constraint_limits)
    x = np.linalg.inv(A).dot(b)

    print("[SUPPLY, CONSTRAINT 1, CONSTRAINT 2, CONSTRAINT 3, PROFIT]")

    for i in range(variables):
        mat_row = matrix[i]
        const = constraint_limits[i]
        coefficient = coefficients[i]

        row_str = ', '.join(str(val) for val in [f"{variable}" for variable in [f"variable {i+1}"] + mat_row + [coefficient]])
        print(f"[{row_str}]")

    avail_str = ', '.join(str(val) for val in constraint_limits)
    print(f"[AVAILABILITY, {avail_str}]")

    print("Optimal Solution:", x)


main()



