#!/usr/bin/env python3

def happy_new_year():
   countdown = 10
   while countdown > 0:
    print(countdown)
    countdown -=1
   print("Happy New Year!") 

def square_integers(int_list):
    return [x ** 2 for x in int_list]

def fizzbuzz():
    for numbers in range(1,101):
    

      if numbers % 3 == 0 and numbers % 5 != 0 :
        print("Fizz")
      elif numbers % 3 != 0 and numbers % 5 == 0 :
        print("Buzz")    
      elif numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")    
      else:
        print(numbers)    
