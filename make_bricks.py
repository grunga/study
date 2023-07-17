'''
CodingBat code practice
Logic-2 > make_bricks

We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.

source: https://codingbat.com/prob/p118406
'''

# Solution

def make_bricks(small, big, goal):
  if (goal - big*5) == 0 or small >= goal:
    return True
  elif big*5 > goal:
    if goal % 5 == 0:
      return True
    elif goal % 5 > 0 and (goal - (goal//5)*5) <= small:
      return True
    else:
      return False
  elif big*5 < goal:
    if big*5 + small >= goal:
      return True
    else:
      return False
  else:
    return False

