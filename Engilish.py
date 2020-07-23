from fractions import Fraction as f

print('Calculus Too Easy!\n')
print('Type the coefficients for each clause in descending order') 
print('(Separate by spacing)')
print('(No Terms: type a coefficient of zero)')
################################################################################################
while True:
  print('ㅡ' * 16)
  y = input().split()

  if y == []: continue
  digit = True
  for i in range(len(y)):
    if y[i].isalpha(): digit = False
  if digit == False: continue

  for n in range(len(y)): 
    if '/' in y[len(y)-1-n]:
      numerator, denominator = map(int, y[len(y)-1-n].split('/'))
    else:
      numerator, denominator = int(y[len(y)-1-n]), 1
    y[len(y)-1-n] = f(numerator, denominator)

  print('f(x) =', end='') 
  for n in range(len(y)):
    if (y[n] == f(1, 1)) & (n != len(y) - 1):
      y[n] = ''

    if n == len(y)-1:
      clause = str(y[n])
    elif n == len(y)-2:
      clause = str(y[n]) + 'x'
    else :
      clause = str(y[n]) + 'x^' + str(len(y)-1-n)

    clause = clause.replace('-',' - ')
    if n == 0 : 
        clause = ' ' + clause
    elif (not '-' in clause):
      clause = ' + ' + clause

    front_of_x = clause.split('x')
    if n == 0 :
      if front_of_x[0] == ' 0':
        continue
    if n != len(y)-1: 
      if front_of_x[0] == ' + 0':
        continue
      else: 
        print(clause, end='')
    else:
      if front_of_x[0] == ' + 0': 
        print()
      else:
        print(clause)

    if y[n] == '':
      y[n] = f(1, 1)

  c = input('differential(1) | indefinite_integral(2) | definite_integral (3) : ')
################################################################################################
  if c == 'differential' or c == '1' :
    
    print("f'(x)=", end='')
    for n in range(len(y)):
      y[n] = (len(y)-1-n) * y[n]
      
      if y[n] == 0: 
        if len(y) == 1: 
          print(' 0'); continue
        else: 
          if n == len(y)-1: 
            print()
            continue
          else: 
            continue

      if n == len(y)-2:
        y[n] = str(y[n])
      elif n == len(y)-3:
        y[n] = str(y[n]) + 'x'
      else:
        y[n] = str(y[n]) + 'x^' + str(len(y)-2-n)

      y[n] = y[n].replace('-',' - ')
      if n == 0 : 
        y[n] = ' ' + y[n]
      elif (not '-' in y[n]):
        y[n] = ' + ' + y[n]

      if n != len(y)-2:
        print(y[n], end='')
      else: 
        print(y[n])
################################################################################################
  elif c == 'indefinite_integral' or c == '2':

    print("F(x) =", end='')
    for n in range(len(y)):
      y[n] = y[n] / (len(y)-n)

      if (y[n] == f(1, 1)) & (n != len(y) - 1):
        y[n] = ''

      if y[n] == 0: 
        if len(y) == 1: 
          print(' 0'); continue
        else: 
          if n == len(y)-1: 
            print()
            continue
          else: 
            continue

      if n == len(y)-1:
        y[n] = str(y[n]) + 'x'
      else :
        y[n] = str(y[n]) + 'x^' + str(len(y)-n)

      y[n] = y[n].replace('-',' - ')
      if n == 0 : 
        y[n] = ' ' + y[n]
      elif (not '-' in y[n]):
        y[n] = ' + ' + y[n]

      if n != len(y)-1:
        print(y[n], end='')
      else: 
        print(y[n],'+ C')
################################################################################################
  elif c == 'definite_integral' or c == '3' :

    x = input('range [a, b] : ').split()
    if len(x) != 2 :continue
    elif x[0].isalpha() | x[1].isalpha():continue

    for n in range(2): 
      if '/' in x[n]:
        numerator, denominator = map(int, x[n].split('/'))
        x[n] = f(numerator, denominator)
      else:
        if '.' in x[n] : 
          x[n] = float(x[n])
        else: 
          x[n] = int(x[n])

    print('[F(x)]{},{} = '.format(x[0], x[1]), end='')
    value = 0
    for n in range(len(y)):
      y[n] = y[n] / (len(y)-n)
      y[n] = y[n] * (x[1]**(len(y)-n) - x[0]**(len(y)-n))
      value = value + y[n]
    
    def Convertible_to_decimal(n): 
      for prime_number in (2, 5): 
        while Share%prime_number == 0: 
          Share=int(Share/prime_number) 
      if Share==1:
        return True 
      else : 
        return False 

    if Convertible_to_decimal(value.denominator) & value.denominator!=1 : 
      print(float(value))
    else :
      print(value)
