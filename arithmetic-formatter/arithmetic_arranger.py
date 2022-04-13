def arithmetic_arranger(problems, show_result = False):

  arranged = ''
  loop = 1
  
  if len(problems) > 5:
    return 'Error: Too many problems.'

  for problem in problems:
    split = problem.split()

    if not split[1] == '+':
      if not split[1] == '-':
        return 'Error: Operator must be \'+\' or \'-\'.'
      
    try:
      int1 = int(split[0])
      int2 = int(split[2])
    except:
      return 'Error: Numbers must only contain digits.'

    if len(split[0]) > 4 or len(split[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    if len(split[0]) > len(split[2]):
      len_dash = len(split[0]) + 2
    else:
      len_dash = len(split[2]) + 2
    
    arranged += split[0].rjust(len_dash)
    
    if not loop == len(problems):
      arranged += '    '
    else:
      arranged += '\n'

    loop += 1

  loop = 1
  
  for problem in problems:
    split = problem.split()

    if len(split[0]) > len(split[2]):
      len_dash = len(split[0]) + 2
    else:
      len_dash = len(split[2]) + 2

    arranged += split[1]
    arranged += split[2].rjust(len_dash - 1)
    
    if not loop == len(problems):
      arranged += '    '
    else:
      arranged += '\n'

    loop += 1

  loop = 1

  for problem in problems:
    split = problem.split()

    if len(split[0]) > len(split[2]):
      len_dash = len(split[0]) + 2
    else:
      len_dash = len(split[2]) + 2
      
    arranged += '-' * len_dash
    
    if not loop == len(problems):
      arranged += '    '

    loop += 1
  
  if show_result == True:
    arranged += '\n'
    loop = 1
    for problem in problems:
      split = problem.split()

      if len(split[0]) > len(split[2]):
        len_dash = len(split[0]) + 2
      else:
        len_dash = len(split[2]) + 2

      if split[1] == '+':
        sum = int(split[0]) + int(split[2])
      elif split[1] == '-':
        sum = int(split[0]) - int(split[2])
  
      arranged += str(sum).rjust(len_dash)

      if not loop == len(problems):
        arranged += '    '

      loop += 1
  
  return arranged