def ex1(d1, d2):
    """
    Merge two dictionaries as one

    ex:
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

    return (note that keys don't have to be in this order)
    {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    """
    return

def ex2(dict):
    """
    Given a dictionary of different stuents with the format:
    {
      <name>: {
        "age": <value>,
        "gender": <value>,
        "height": <value>
      }
    }

    ex: 

    {
      "bob": {
        "age": 22,
        "gender": "m",
        "height": 100
      },
      "alice": {
        "age": 22,
        "gender": "f",
        "height": 100
      }
    }

    return the age of the student with the name "dorothy"
    """
    return

def ex3(dict):
    """
    Given a dictionary of different stuents with the format:
    {
      <name>: {
        "age": <value>,
        "gender": <value>,
        "height": <value>
      }
    }

    delete all the age and gender values of the dictionary and return the dictionary

    ex:
    {
      "bob": {
        "age": 22,
        "gender": "m",
        "height": 100
      },
      "alice": {
        "age": 22,
        "gender": "f",
        "height": 100
      }
    }

    return

    {
      "bob": {
        "height": 100
      },
      "alice": {
        "height": 100
      }
    }
    """


    return

def ex4(dict):
    """
    Get the name of a minimum height student the dictionary

    ex:

    {
      "bob": {
        "height": 90
      },
      "alice": {
        "height": 100
      }
    }

    return "bob"
    """
    return


#######################
# Do not modify below #
#######################
test_case_number = 1
def check(check_title, expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' ', check_title, ' - Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' ', check_title, ' - Test #', test_case_number, ': Expected ', sep='', end='')
    print(expected)
    print('  Your output: ', end='')
    print(output)
  test_case_number += 1

if __name__ == "__main__":

  dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
  dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
  dict3 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

  students =  {
      "bob": {
        "age": 20,
        "gender": "m",
        "height": 99
      },
      "alice": {
        "age": 21,
        "gender": "f",
        "height": 100
      },
      "charlie": {
        "age": 22,
        "gender": "m",
        "height": 101
      },
      "dorothy": {
        "age": 23,
        "gender": "f",
        "height": 102
      },
    }

  students2 =  {
      "bob": {
        "height": 99
      },
      "alice": {
        "height": 100
      },
      "charlie": {
        "height": 101
      },
      "dorothy": {
        "height": 102
      },
    }

  expected = dict3
  output = ex1(dict1, dict2)
  check("ex1", expected, output)

  expected = 23
  output = ex2(students)
  check("ex2", expected, output)

  expected = students2
  output = ex3(students)
  check("ex3", expected, output)

  expected = "bob"
  output = ex4(students2)
  check("ex4", expected, output)

  