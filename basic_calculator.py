# -*- coding: utf-8 -*-
"""Basic Calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aheVl1cwcS3bUrZlPLjvZyDsrcWxKrjW
"""

#Basic Calculator – Create a calculator that performs simple operations like addition, subtraction

print('1 - Addition')
print('2 - Subtraction')
print('3 - Multiplication')
print('4 - Division')
Option = float(input('Choose an operation : '))
if (Option in [1,2,3,4]):
  num1 = float(input('Enter first number : '))
  num2 = float(input('Enter second number : '))

  if (Option == 1):
    result = num1 + num2
  elif (Option == 2):
    result = num1 - num2
  elif (Option == 3):
    result = num1 * num2
  elif (Option == 4):
    result = num1 / num2 # we shall use // instead of / when using int digits

else:
  print('Invalid operation entered')

print('The result of the operation is {}'.format(result)) #we use {} as a container and fullstop is used to attribute the forward text ex car.colour(colour is an attribute of the car)
                                                          #.format() is used to enter the value inside of the () into the {} from the related string

