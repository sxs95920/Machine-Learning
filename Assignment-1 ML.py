#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# # Question - 1
# 

# In[6]:


#Sort the list and find the min and max age

ages =[19,22,19,24,20,25,26,24,25,24]

ages.sort()

min_ages = ages[0]

max_ages = ages[-1]

print(min_ages,max_ages)


# In[7]:


#Add the min age and the max age again to the list


ages.append(min_ages)

ages.append(max_ages)

ages


# In[8]:


#Find the median age (one middle item or two middle items divided by two)

ages.sort()
x= len(ages)

if x%2==1:
    median_ages =(x//2) 

else:
    median_ages  = (ages[x//2-1]+ages[x//2])/2

    
median_ages


# In[9]:


#Find the average age (sum of all items divided by their number)

average_ages = sum(ages)/len(ages)

average_ages


# In[10]:


#Find the range of the ages (max minus min)

range_ages = max(ages) - min(ages)
range_ages


# # Question -2 

# In[11]:


#Create an empty dictionary called dog

Dog = {}
Dog


# In[12]:


#Add name, color, breed, legs, age to the dog dictionary

Dog = {
    'name': 'Snoopy',
    'color': 'Brown',
    'breed': 'Labrador',
    'legs': 4,
    'age': 3
}


Dog


# In[13]:


# Create a student dictionary and add first_name, last_name, gender, age, marital status,skills, country, city and address as keys for the dictionary

Student = {
    'first_name': 'Sai',
    'last_name': 'Siddipeta',
    'gender': 'Male',
    'age': 27,
    'marital_status': 'Single',
    'skills': ['Python', 'Java', 'HTML', 'CSS'],
    'country': 'United States',
    'city': 'Kansas',
    'address': 'Overland Park'
}

Student


# In[14]:


#Get the length of the student dictionary
len(Student)


# In[40]:


#Get the value of skills and check the data type, it should be a list

skills_value = Student['skills']
print(skills_value)
print(type(skills_value))


# In[16]:


# Modify the skills values by adding one or two skills
Student = {
    'first_name': 'Sai',
    'last_name': 'Siddipeta',
    'gender': 'Male',
    'age': 27,
    'marital_status': 'Single',
    'skills': ['Python', 'Java', 'HTML', 'CSS', 'MACHINE LEARNING','SQL'],
    'country': 'United States',
    'city': 'Kansas',
    'address': 'Overland Park'
}

Student


# In[17]:


#Get the dictionary keys as a list

Key_List = list(Student.keys())

print(Key_List)


# In[18]:


#Get the dictionary values as a list

Values_List = list(Student.values())

print(Values_List)




# # Question 3
# 
# 

# In[19]:


#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

Siblings_brothers = ("Sai","Rahul","Sumeet","Sudhamash","Krishna","Venkat Sai",)

Siblings_sisters =("Komal","Mounica","Aishwarya","Raji")

print(Siblings_brothers,Siblings_sisters)


# In[20]:


#Join brothers and sisters tuples and assign it to siblings
Siblings = Siblings_brothers + Siblings_sisters
print(Siblings)


# In[21]:


#How many siblings do you have?

num_siblings = len(Siblings)

print(f"Number of Siblings = {num_siblings}")


# In[22]:


#Modify the siblings tuple and add the name of your father and mother and assign it to family_members

Father = "Sanjeeva"
Mother = "Vani Sree"
family_members = Siblings +(Father, Mother)

print(family_members)


# # Question 4
# 

# In[23]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
len(it_companies)


# In[24]:


it_companies.add("Twitter")
print(it_companies)


# In[25]:


#Insert multiple IT companies at once to the set it_companies
new_companies = ["Wipro","Accenture","TCS","CapeGemini"]

it_companies.update(new_companies)

print(it_companies)


# In[26]:


#Remove one of the companies from the set it_companies

it_companies.remove("Wipro")

print(it_companies)

#What is the difference between remove and discard

# remove() method:

The remove() method removes the specified element from the set.
Ex: it_companies.remove("Wipro")

#discard() method:

The discard() method removes the specified element from the set if it exists.
Ex: set.discard(element)
# In[27]:


#Join A and B

result = A.union(B)

print(result)


# In[28]:


#Find A intersection B

result1 = A.intersection(B)

print(result1)


# In[29]:


#Is A subset of B

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

result2 = A.issubset(B) 

print(result2)


# In[30]:


#Are A and B disjoint sets
dis_joint = A.isdisjoint(B)

print(dis_joint)


# In[31]:


#Join A with B and B with A
result = A.union(B)
result3 = B.union(A)

print("A union B:", result)
print("B union A:", result3)


# In[32]:


#What is the symmetric difference between A and B

result4 = A.symmetric_difference(B)

print(result4)


# In[33]:


#Delete the sets completely
del B
print(B)


# In[34]:


#Convert the ages to a set and compare the length of the list and the set.

ages_list =  age

ages_set = set(ages_list)

length_list = len(ages_list)
length_set = len(ages_set)

print("Length of the list:", length_list)
print("Length of the set:", length_set)

if length_list == length_set:
    print("The lengths of the list and the set are equal.")
else:
    print("The lengths of the list and the set are different.")


# # Question 5

# In[35]:


#The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of _area_of_circle_

import math

# Radius of the circle
radius = 30

# Calculate the area of the circle
area_of_circle = math.pi * radius ** 2

print("Area of the circle:", area_of_circle)


# In[36]:


#Calculate the circumference of a circle and assign the value to a variable name of_circum_of_circle_

circum_of_circle_ = 2* math.pi*radius

print(circum_of_circle_)


# In[37]:


#Take radius as user input and calculate the area.

radius = float(input("Enter the radius of the circle (in meters): "))

area_of_circle = math.pi * radius ** 2

print("Area of the circle:", area_of_circle)


# # Question 6

# In[68]:


#How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = 'I am a teacher and I love to inspire and teach people'

words = sentence.split()

unique_words = set(words)


num_unique_words = len(unique_words)

print("Number of unique words:", num_unique_words)


# # Question 7

# In[70]:


#Use a tab escape sequence to get the following lines.
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")


# # Question 8

# In[75]:


#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")


# # Question 9

# In[38]:


#Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using Loop. N: No of students (Read input from user)



N = int(input("Enter the number of students: "))

weights_lbs = []

# Read the weights of N students into the list
for i in range(N):
    weight_lbs = float(input(f"Enter the weight of student {i+1} (in lbs): "))
    weights_lbs.append(weight_lbs)

# Initialize an empty list to store the weights in kilograms
weights_kgs = []

# Convert the weights from pounds to kilograms and store them in the new list
for weight_lbs in weights_lbs:
    weight_kgs = weight_lbs * 0.453592  # 1 pound = 0.453592 kilograms
    weights_kgs.append(round(weight_kgs, 2))  # Round to 2 decimal places

# Print the converted weights in kilograms
print("Weights in kilograms:", weights_kgs)


# In[ ]:




