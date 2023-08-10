import numpy as np


constraint_limits = eval(input("Please enter an array of constraints (ex. [[2,4,5], [1,2,4], [8,0,3]]): "))
A = np.array(constraint_limits)


inv_A = np.linalg.inv(A)

constraints = eval(input("Please enter the constraints for the problem (ex. [300, 200, 200]): "))
b = np.array()

x = np.linalg.inv(A).dot(b)