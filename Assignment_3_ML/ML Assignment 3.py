#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Numpy:


# In[2]:


#a
# Creating random vector of size 15 having only Integers in the range 1-20.
import numpy as np
v =  np.random.randint(1,20,(15,))

# Reshaping the array to 3 by 5 
arr = v.reshape(3,5)
print(arr.shape)
print(arr)

# Replacing the max in each row by 0
row_max = arr.max(axis=1).reshape(-1,1)
arr = np.where(arr == row_max, 0, arr)
print('\n',arr)


# In[3]:


# Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements), also print the shape, type and data type of the array
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 5, 7]], np.int32)
print('Shape:', x.shape)
print('Type:', type(x))
print('Data type:', x.dtype)


# In[4]:


#B
import numpy as np

# create the square array
A = np.array([[3, -2], [1, 0]])

# compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# print the results
print("Eigenvalues: ", eigenvalues)
print("Right Eigenvectors: \n", eigenvectors)


# In[5]:


#C
import numpy as np

# create the array
A = np.array([[0, 1, 2], [3, 4, 5]])

# compute the sum of diagonal elements
diagonal_sum = np.trace(A)

# print the result
print("Sum of diagonal elements: ", diagonal_sum)


# In[6]:


#D
import numpy as np

# create the original array
original_array = np.array([[1, 2], [3, 4], [5, 6]])

# reshape the array to a new shape
new_array = original_array.reshape((2, 3))

# print both arrays to verify the data is not changed
print("Original array:\n", original_array)
print("New array:\n", new_array)


# In[7]:


# Reshape 2x3:
import numpy as np

# create the original array
original_array = np.array([[1, 2, 3], [4, 5, 6]])

# reshape the array to a new shape
new_array = original_array.reshape((2, 3))

# print both arrays to verify the data is not changed
print("Original array:\n", original_array)
print("New array:\n", new_array)


# In[ ]:





# In[ ]:




