#!/usr/bin/env python
# coding: utf-8

# ## 1. Find the Cartesian Product of the below given sets in the 
# ## below cell. (In Python Code)
# ## A = set(['a','b','c'])
# S = {1,2,3}

# In[1]:


A = set(['a','b','c'])
S = {1,2,3}
cartesian_product = {(a,s) for a in A for s in S}
print(cartesian_product)
{('b', 3), ('c', 1), ('a', 1), ('b', 2), ('c', 3), ('a', 3), ('c', 2),
('b', 1), ('a', 2)}


# # 2. Find all the possible permutations and number of 
# # permutations of A
# ## #A = {'Red','Green','Blue'}
# 

# In[2]:


from itertools import permutations
A = {'Red','Green','Blue'}
p_list = list (permutations(A))
num_p = len (p_list)
print("ALL THE POSSIBLE PERMUTATIONS ARE :- ")
for p in p_list:
 print(p)
print("NUMBER OF PERMUTATIONS ARE :- ", num_p)


# ## 3. Research Question on Hypothesis Testing. In previous years, 52% of parents believed that electronics and social media was the cause of their teenager’s lack of sleep. Do more parents today believe that their teenager’s lack of sleep is caused due to electronics and social media?
# ## Population: Parents with a teenager (age 13-18) ## Parameter of Interest: p
# ## Null Hypothesis: p = 0.52 ## Alternative Hypthosis: p > 0.52 (note that this is a one-sided test)
# ## Data: 1018 people were surveyed. 56% of those who were surveyed believe that their teenager’s lack of sleep is caused due to electronics and social media.
# ## Hint: Use proportions_ztest() from statsmodels ## Note the argument alternative="larger" indicating a one-sided test. The function returns two values - the z-statistic and the corresponding p-value.
# ## What is your Conclusion of the hypothesis test ?

# In[3]:


import statsmodels.api as sm
# Given data
n = 1018 # Total number of people surveyed
p0 = 0.52 # The assumed population proportion under the null hypothesis
p1 = 0.56 # The sample proportion
# Perform the one-sided hypothesis test
z_stat, p_value = sm.stats.proportions_ztest(p1 * n, n, p0, 
alternative='larger')
# Significance level (alpha)
alpha = 0.05
# Check if the p-value is less than the significance level
if p_value < alpha:
 print("Reject the null hypothesis")
else:
 print("Fail to reject the null hypothesis")
# Determine the conclusion based on the result
if p_value < alpha:
 print("There is enough evidence to conclude that more parents today believe that their teenager’s lack of sleep is caused due to electronics and social media.")
else:
       
     print("There is not enough evidence to conclude that more parents") 


# ## 4. Calculate the set difference between the 2 sets (set1 - multipes of 3 upto a range of 31 and set2 - multiples of 2 upto a range of 31)

# In[1]:


# Create sets of multiples of 3 and multiples of another number (e.g.,
#2) up to a range of 31
set1 = set(range(3, 32, 3))
set2 = set(range( 2,32,2))
# Calculate the set difference (set1 - set2)
difference = set1 - set2
# Print the result
print("Difference between Set1 and Set2 (i.e. Multiples of 3 up to 31 excluding multiples of 2 upto 31) is :- ")
print(difference)


# ## 5. Calculate a function to generate random arrays with range of (1,100) and the naive functions to calculate Mean, Varience and Standard deviation for the array generated
# 

# In[6]:


import random
import math
def generate_random_array(size):
 return [random.randint(1, 100) for i in range(size)]
def calculate_mean(array):
 return sum(array) / len(array)
def calculate_variance(array, mean):
 return sum((x - mean) ** 2 for x in array) / len(array)
def calculate_standard_deviation(variance):
 return math.sqrt(variance)
# Generating a random array
random_array = generate_random_array(20)
# Calculating mean, variance, and standard deviation
mean = calculate_mean(random_array)
variance = calculate_variance(random_array, mean)
standard_deviation = calculate_standard_deviation(variance)
# Printing the results
print(f"Random Array: {random_array}")
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")


# In[ ]:




