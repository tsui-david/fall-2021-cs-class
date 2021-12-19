import math
# Add any extra import statements you may need here

# Add any helper functions you may need here

def ex1(a, b):
    """
    return the sum of two values
    """
    return a+b

def ex2(a, b, c):
    """
    return the product of three values
    """
    return a+b+c

def ex3(a, b):
    """
    given two numbers return True if the two numbers sum to 100. False otherwise.
    """
    return a+b == 100

def ex4(a_list):
    """
    return the sum of the list of values
    """
    return sum(a_list)


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1

def check(check_title, expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' ', check_title, '- Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' ', check_title, '- Test #', test_case_number, ': Expected ', sep='', end='')
    print(expected)
    print('  Your output: ', end='')
    print(output)
  test_case_number += 1

if __name__ == "__main__":
  expected = 5
  output = ex1(2, 3)
  check("ex1", expected, output)

  expected = 103
  output = ex1(3, 100)
  check("ex1", expected, output)

  expected = 9
  output = ex2(1, 4, 4)
  check("ex2", expected, output)

  expected = 100
  output = ex2(0, 50, 50)
  check("ex2", expected, output)

  expected = True
  output = ex3(100, 0)
  check("ex3", expected, output)

  expected = False
  output = ex3(9, 10)
  check("ex3", expected, output)

  expected = 11
  output = ex4([1, 5, 5])
  check("ex4", expected, output)

  expected = 10
  output = ex4([1,2,3,4])
  check("ex4", expected, output)
  # Add your own test cases here
  