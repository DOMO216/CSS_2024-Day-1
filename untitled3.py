#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:42:00 2024

@author: thabangmolefi
"""
"""
Storing data in Python
1. Lists 
2. Dictionaries
3. Data Frames - specific to pandas
"""
age1 = 30
age2 = 25
age3 = 29

age = [30,25,29,46,22]
print(age)
"""
[30, 25, 29, 46, 22]
"""

print(age[0])
"""
30
"""

print(min(age))
"""
22
"""

print(max(age))
"""
46
"""
print(len(age))
"""
5
"""
print(sum(age)/len(age))
"""
30.4
"""

g1 = "M"
g2 = "F"
g3 = "M"

c1 = "South Africa"
c2 = "Lesotho"

print(age[0:2])
"""
[30, 25]
"""

age.append(100)

print(age)


age.insert(0, 100)
print(age)

"""
Dictionaries - key:value pairs

cat: "A cute animal"

"""

mammals = {"cat":"a cute animal", 
           "lion":"king of the jungle", 
           "elephant":"a gigantic herbivore"}
print(mammals["cat"])

"""
Data frames

"""
fruits = ["apple", "banana","orange", "grape", "kiwi"]

size_nm = [9.8,10.1,13.2,8.7,20.5]

fruit_sizes = {'fruit' :fruits, 'sizes':size_nm}

"""
Using pandas 

"""

import pandas as pd

df = pd.DataFrame(fruit_sizes)

print(df[fruit])


print(df.describe())

print(df[sizes].min())

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns=["sizes"], inplace=True)
