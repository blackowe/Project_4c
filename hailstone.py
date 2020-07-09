# Author: Erik Blackowicz
# Date: 7/8/20
# Description: Fx take in integer and return the number of steps to reach 1 using hailstone sequence.

def hailstone(num):
 '''Input an integer. Returns the number of steps to reach 1 following the
 hailstone sequence. Hailstone sequence says: if input int. is even divide by 2,
 if input int. is odd multiply by 3 and add 1.'''
 count =0
 while num!=1:    # continues until reaches 1
  if num%2==0:     # if num is even, divide by 2
     num= num/2
  else:
     num = (num*3) + 1  # if num is odd, multiply by 3 and add 1
  count = count +1
 return(count)   # returns number of steps taken
