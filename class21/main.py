def ex1(key, value):
    """
    create a dictionary with its key as key, and value as value parameter 
    return the dictionary
    """
    return

def ex2(dict, key):
    """
    return the value of the given key in the dict parameter
    """
    return

def ex3(dict, key):
    """
    delete the given key in the dictionary
    return the dictionary
    """
    return

def ex4(dict, key, value):
    """
    add a new key value to dictionary
    return the dictionary
    """
    return

def ex5(str):
    """
    Create a dictionary that counts the frequency of the words in the string.

    ex: "run forrest run from forrest gump"
    
    run: 2
    forrest: 2
    from: 1
    gump: 1

    return the dictionary
    """ 
    return


#######################
# Do not modify below #
#######################
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
  expected = {"Taiwan": "Taipei"}
  output = ex1("Taiwan", "Taipei")
  check("ex1", expected, output)

  expected = "Taipei"
  output = ex2({"Taiwan": "Taipei"}, "Taiwan")
  check("ex2", expected, output)

  expected = {"a": 1, "b": 2}
  output = ex3({"a": 1, "b": 2, "c": 3}, "c")
  check("ex3", expected, output)

  expected = {"a": 1, "b": 2, "c": 3}
  output = ex4({"a": 1, "b": 2}, "c", 3)
  check("ex4", expected, output)

  expected = {"run": 2, "forrest": 2, "from": 1, "gump": 1} 
  output = ex5("run forrest run from forrest gump")
  check("ex5", expected, output)
  