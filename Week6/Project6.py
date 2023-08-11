import numpy as np






def main():

    variables = int(input("Please enter the number of variables: "))
    matrix = eval(input("Enter the data for the square matrix using stating the constraints (ex. [[2,4,5], [1,2,4], [8,0,3]]): "))
    constraint_limits = eval(input("Enter the constraint limits (ex. [300, 200, 300]): "))
    coeffiecients = input("Enter the coefficients of each variable for the objective function (ex. 3000, 2000, 2000): ")

    variables = 3
    matrix = [[2,4,5], [1,2,4], [8,0,3]]
    constraint_limits = [300, 200, 300]
    coeffiecients = 3000, 2000, 2000



    # A = np.array(matrix)
    A = np.array([[2,4,5], [1,2,4], [8,0,3]])
    # inv_A = np.linalg.inv(A)
    inv_A = np.linalg.inv(A)
    # b = np.array(constraint_limits)
    b = np.array([300, 200, 300])
    # x = np.linalg.inv(A).dot(b)
    x = np.linalg.inv(A).dot(b)

    for i in range(variables):
        for j in matrix:
            for k in coeffiecients:
                print(f"Variable {i}, {j}, {k}")
    
    print(f"AVAILIBILITY, {constraint_limits}")
    
    # print(x)

main()