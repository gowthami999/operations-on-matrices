#Importing numpy as np
import numpy as np
a=np.array(input("enter the matrix values"))
b=np.array(input("enter the another matrix values"))
print('The given array is:\n',a)
print('The another array is:\n',b)
#To find determinant
print('The determinant of the given matrix is\n',np.linalg.det(a))
#To find inverse of given matrix
print('The inverse of the given matrix is\n',np.linalg.inv(a))
#To find trace of given matrix
print('The trace of the given matrix is\n',np.trace(a))
#To find tanspose of given matrix
print('The transpose of given matrix is\n',np.transpose(a))
#To find rank of given matrix
print('The rank of given matrix is\n',np.linalg.matrix_rank(a))
#To find addition of given two  matrix
print('The addition of two matrixes is\n',np.add(a,b))
#To find subtraction of given two  matrix
print('The subtraction of two matrixes is\n',np.subtract(a,b))
#To find multlipication of given two matrix
print('The multlipication of two matrixes is\n',np.matmul(a,b))
#To find divison of given two matrix
print('The division of two matrixes is\n',np.divide(a,b))
#To find square of given matrix
print('The square of given matrix is\n',np.square(a))
#To find square root of given matrix
print('The squart of given function is\n',np.sqrt(a))

