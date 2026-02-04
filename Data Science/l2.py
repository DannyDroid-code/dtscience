
import numpy as np
# Concept of array slicing array[start : end : step]

linear_array = np.array([1,2,3,4,5,6,7,8])

print(linear_array[0:4])
print(linear_array[:7])
print(linear_array[::2]) # prints every second element
print(linear_array[::-1]) # reverse the array

multi_array = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(multi_array[0:2, 0:1])

# Exercise - Create a matrix of 7*7 and take out the middle 3*3 cross-seciton out of the 7*7 matrix

# Conditional selection of elements
# Select all the even elements from a numpy array

k = np.array([1,2,3,4,5,6,7,8])
even_array = k[k % 2 == 0]
great = k [k>4]

print(even_array)

# # compare with a value

bool_array = k[k == 5]
print(bool_array) # only the value with 5 has True

# selection by indexes
print(k[[2,4,6]]) # 2,4,6 are indexes

# # Exercise - Select the value less than 5 from an array of 1-10

# # Operations on Numpy array

# Task +1 to each element
sample_list = [1,2,3,4,5,6,7,8]

for i in range(0, len(sample_list)):
	sample_list[i] += 1
	
print(sample_list)

sample_array = np.array([1,2,3,4,5,6,7,8])

sample_array += 1 # No need to run a for loop

print(sample_array)


sample_array1 = np.array([1,2,3,4,5,6,7,8])
sample_array2 = np.array([1,2,3,4,5,6,7,8])

print(sample_array1 + sample_array2)

#Explanation - Why Loop is not required for mathematical operation on numpy lists

# Matrix Addition through numpy 

matA = np.random.permutation(np.arange(16)).reshape(4,4)
matB = np.random.permutation(np.arange(16)).reshape(4,4)

print(matA + matB) # compare the ease of doing matrix operation with or without numpy

# Exercise - Do the matrix multiplication in the same way, It would be wrong way of doing matrix mutiplication

# Create a function for numpy operation

#y = 2x + 3
def solve(k):
	return 2*k + 3
	
x = np.array([1,2,3,4,5])

y = solve(x) # function is applied to every element



