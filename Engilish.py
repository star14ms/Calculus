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
    if n == len(y)-1:
      clause = str(y[n])
    elif n == len(y)-2:
      clause = str(y[n]) + 'x'
    else :
      clause = str(y[n]) + 'x^' + str(len(y)-1-n)

    clause = clause.replace('-',' - ').replace('1x','x').replace('1x','11x')
    if n == 0 : 
        clause = ' ' + clause
    elif (not '-' in clause):
      clause = ' + ' + clause

    clause_Separation = clause.split('x')
    if n == 0 :
      if clause_Separation[0] == ' 0': continue
    elif clause_Separation[0] == ' + 0': continue
    if n != len(y)-1: 
      print(clause, end='')
    else:
      print(clause)

  c = input('differential(1) | indefinite_integral(2) | definite_integral (3) : ')
################################################################################################
  if c == 'differential' or c == '1' :
   
    print("f'(x)=", end='')
    for n in range(len(y)):
      y[n] = (len(y)-1-n) * y[n]
      
      if y[n] == 0: 
        if len(y) == 1: 
          print(' 0'); continue
        else : 
          continue

      if n == len(y)-2:
        y[n] = str(y[n])
      elif n == len(y)-3:
        y[n] = str(y[n]) + 'x'
      else :
        y[n] = str(y[n]) + 'x^' + str(len(y)-2-n)

      y[n] = y[n].replace('-',' - ').replace('1x','x').replace('1x','11x')
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

      if n == len(y)-1:
        y[n] = str(y[n]) + 'x'
      else :
        y[n] = str(y[n]) + 'x^' + str(len(y)-n)

      y[n] = y[n].replace('-',' - ').replace('1x','x').replace('1x','11x')
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

    x = input('Range [a, b] : ').split()
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
    Value = 0
    for n in range(len(y)):
      y[n] = y[n] / (len(y)-n)
      y[n] = y[n] * (x[1]**(len(y)-n) - x[0]**(len(y)-n))
      Value = Value + y[n]
    
    def Convertible_to_decimal(n): 
      for i in (2, 5): 
        while n%i == 0: 
          n=int(n/i) 
      if n==1: 
        return True 
      else : 
        return False 

    if Convertible_to_decimal(Value.denominator) & Value.denominator!=1 : 
      print(float(Value))
    else :
      print(Value)
