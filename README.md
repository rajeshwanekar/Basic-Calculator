# Basic Calculator

A calculator that performs simple operations like addition, subtraction.

## Usage

```python

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
    result = num1 / num2 

else:
  print('Invalid operation entered')

print('The result of the operation is {}'.format(result)) 
                                                          
```

## Contributing
This project is done by Rajesh Wanekar
You can connect with me [![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/rajesh-wanekar-747b6b256)
