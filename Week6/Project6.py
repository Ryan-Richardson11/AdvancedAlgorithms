import numpy as np


constraints = eval(input("Enter the data for the square matrix using stating the constraints (ex. [[2,4,5], [1,2,4], [8,0,3]]): "))
A = np.array(constraints)

inv_A = np.linalg.inv(A)

coefficients = eval(input("Enter the coefficients of each variable for the objective function (ex. [300, 200, 200]): "))
b = np.array(coefficients)

x = np.linalg.inv(A).dot(b)