#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:07:45 2024

@author: thabangmolefi
"""

import pandas as pd 

file = pd.read_csv('country_data.csv')

print(file)

"""
   Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
"""

print(file.info())


"""
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 392.0+ bytes

"""

print(file.describe())
"""
             Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000
"""
file_2 =    pd.read_csv('iris.csv')
print(file_2)
"""
    sepal_length  sepal_width  petal_length  petal_width         species
0             5.1          3.5           1.4          0.2     Iris-setosa
1             4.9          3.0           1.4          0.2     Iris-setosa
2             4.7          3.2           1.3          0.2     Iris-setosa
3             4.6          3.1           1.5          0.2     Iris-setosa
4             5.0          3.6           1.4          0.2     Iris-setosa
..            ...          ...           ...          ...             ...
145           6.7          3.0           5.2          2.3  Iris-virginica
146           6.3          2.5           5.0          1.9  Iris-virginica
147           6.5          3.0           5.2          2.0  Iris-virginica
148           6.2          3.4           5.4          2.3  Iris-virginica
149           5.9          3.0           5.1          1.8  Iris-virginica

[150 rows x 5 columns]
"""

print(file_2.describe())
"""
      sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

"""

file_3 = pd.read_csv('insurance_data.csv', skiprows = 5)

print(file_3)

"""
     X      Y
0   108  392.5
1    19   46.2
2    13   15.7
3   124  422.2
4    40  119.4
..  ...    ...
58    9   87.4
59   31  209.8
60   14   95.5
61   53  244.6
62   26  187.5

[63 rows x 2 columns]
"""

file_4 = pd.read_csv('diab_data.csv')

print(file_4)
"""
    preg_count  glucose  bp  skinfold  insulin   BMI  predigree  age  class
0             6      148  72        35        0  33.6      0.627   50      1
1             1       85  66        29        0  26.6      0.351   31      0
2             8      183  64         0        0  23.3      0.672   32      1
3             1       89  66        23       94  28.1      0.167   21      0
4             0      137  40        35      168  43.1      2.288   33      1
..          ...      ...  ..       ...      ...   ...        ...  ...    ...
763          10      101  76        48      180  32.9      0.171   63      0
764           2      122  70        27        0  36.8      0.340   27      0
765           5      121  72        23      112  26.2      0.245   30      0
766           1      126  60         0        0  30.1      0.349   47      1
767           1       93  70        31        0  30.4      0.315   23      0

[768 rows x 9 columns]
"""

file_5 = pd.read_csv('housing_data.csv')
print(file_5)

"""
print(file_5)
     0.00632   18   2.31    0  0.538  6.575  ...  1    296  15.3   396.9  4.98    24
0    0.02731  0.0   7.07  0.0  0.469  6.421  ...  2  242.0  17.8  396.90  9.14  21.6
1    0.02729  0.0   7.07  0.0  0.469  7.185  ...  2  242.0  17.8  392.83  4.03  34.7
2    0.03237  0.0   2.18  0.0  0.458  6.998  ...  3  222.0  18.7  394.63  2.94  33.4
3    0.06905  0.0   2.18  0.0  0.458  7.147  ...  3  222.0  18.7  396.90  5.33  36.2
4    0.02985  0.0   2.18  0.0  0.458  6.430  ...  3  222.0  18.7  394.12  5.21  28.7
..       ...  ...    ...  ...    ...    ...  ... ..    ...   ...     ...   ...   ...
500  0.06263  0.0  11.93  0.0  0.573  6.593  ...  1  273.0  21.0  391.99  9.67  22.4
501  0.04527  0.0  11.93  0.0  0.573  6.120  ...  1  273.0  21.0  396.90  9.08  20.6
502  0.06076  0.0  11.93  0.0  0.573  6.976  ...  1  273.0  21.0  396.90  5.64  23.9
503  0.10959  0.0  11.93  0.0  0.573  6.794  ...  1  273.0  21.0  393.45  6.48  22.0
504  0.04741  0.0  11.93  0.0  0.573  6.030  ...  1  273.0  21.0  396.90  7.88  11.9

[505 rows x 14 columns]
"""

Column_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]


file_5 = pd.read_csv('housing_data.csv', names=Column_names)
print(file_5)

