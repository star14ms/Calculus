from fractions import Fraction as f
# to add fractional form
print('Calculus Too Easy!\n')
print('Type the coefficients for each term in descending order') 
print('(Separate by spacing)')
print('(No Terms: type a coefficient of zero)')
# To print out descriptions
################################################################################################
while True: # repeat
  print('ㅡ' * 16) # draw a line
  y = input().split()
  # Receive Input:coefficient of each terms of a function

  if y == []: continue 
  # Initialization If nothing input received

  no_letter = True
  for n in range(len(y)):
    transformation = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'aaaaaaaaaaaaaaaaaaaaaaaaaa')
    to_examine = y[n].translate(transformation)
    if 'a' in to_examine: no_letter = False
  if no_letter == False: continue
  # 각 항에서 문자가 있으면 초기화

  for n in range(len(y)): 
    if '/' in y[n]:
      numerator, denominator = map(int, y[n].split('/'))
      y[n] = f(numerator, denominator)
    elif not '.' in y[n]:
      numerator, denominator = int(y[n]), 1
      y[n] = f(numerator, denominator)
    else: y[n] = float(y[n])
  # 각 항의 계수를 분수꼴로 바꾸기 ( len(y)-1-n : 차수 )

  print('f(x) =', end='') 
  # 'f(x) =' 출력

  for n in range(len(y)):
  # 각 항의 계수에서
    if (y[n] == f(1, 1)) & (n != len(y) - 1):
      y[n] = ''
    # 계수가 1인 항은 1생략

    if n == len(y)-1:
      term = str(y[n])
    elif n == len(y)-2:
      term = str(y[n]) + 'x'
    else :
      term = str(y[n]) + 'x^' + str(len(y)-1-n)
    # 변수기호, 그 변수의 지수 추가

    term = term.replace('-',' - ')
    if n == 0 : 
        term = ' ' + term
    elif (not '-' in term):
      term = ' + ' + term
    # 부호, 공백 추가

    front_of_x = term.split('x')
    if n == 0 :
      if front_of_x[0] == ' 0':
        continue
    if n != len(y)-1: 
      if front_of_x[0] == ' + 0':
        continue
      else: 
        print(term, end='')
    else:
      if front_of_x[0] == ' + 0': 
        print()
      else:
        print(term)
    # 출력 (항이 0이면 생략)

    if y[n] == '':
      y[n] = f(1, 1)
    # 위에서 생략한 계수 1을 다시 1로 만들기

  c = input('differential(1) | indefinite_integral(2) | definite_integral (3) : ')
  # 미분, 부정적분, 정적분 중 고르기
################################################################################################
  if c == 'differential' or c == '1' :
  # 미분을 골랐을 때
    print("f'(x)=", end='')
    # "f'(x)=" 출력
  
    if len(y) == 1: 
      print(' 0'); continue
    # 항이 하나면 0 출력

    for n in range(len(y)-1):
    # 각 항의 계수에서
      y[n] = (len(y)-1-n) * y[n]
      # 새 계수 = 차수 * 계수

      if y[n] == 0:   
          if n == len(y)-1: 
            print()
            continue
          else: 
            continue
      # 계수가 0이면 그 항은 생략

      if (y[n] == f(1, 1)) & (n != len(y)-2):
        y[n] = ''
      # 계수가 1이면 1생략

      if n == len(y)-2:
        y[n] = str(y[n])
      elif n == len(y)-3:
        y[n] = str(y[n]) + 'x'
      else:
        y[n] = str(y[n]) + 'x^' + str(len(y)-1-n-1)
      # 변수기호, -1한 지수 추가

      y[n] = y[n].replace('-',' - ')
      if n == 0 : 
        y[n] = ' ' + y[n]
      elif (not '-' in y[n]):
        y[n] = ' + ' + y[n]
      # 부호, 공백 추가

      if n != len(y)-2:
        print(y[n], end='')
      else: 
        print(y[n])
      # 출력
################################################################################################
  elif c == 'indefinite_integral' or c == '2':
  # 부정적분을 골랐을 때
    print('F(x) =', end='')
    # 'F(x) =' 출력

    for n in range(len(y)):
    # 각 항의 계수에서
      y[n] = y[n] / (len(y)-1-n+1)
      # 새 계수 = 계수 / 차수 + 1

      if y[n] == 0: 
        if n == len(y)-1: 
          print()
          continue
        else: 
          continue
      # 계수가 0이면 그 항은 생략

      if y[n] == f(1, 1):
        y[n] = ''
      # 계수가 1이면 1생략
        
      if n == len(y)-1:
        y[n] = str(y[n]) + 'x'
      else :
        y[n] = str(y[n]) + 'x^' + str(len(y)-1-n+1)

      y[n] = y[n].replace('-',' - ')
      if n == 0 : 
        y[n] = ' ' + y[n]
      elif (not '-' in y[n]):
        y[n] = ' + ' + y[n]
      # 변수기호, +1한 지수 추가

      if n != len(y)-1:
        print(y[n], end='')
      else: 
        print(y[n],'+ C')
      # 출력 (적분상수 포함)
################################################################################################
  elif c == 'definite_integral' or c == '3' :
  # 정적분을 골랐을 때
    x = input('range [a, b] : ').split()
    # 범위 a, b 입력받음 ( a = x[0], b = x[1] )

    if len(x) != 2 :continue
    elif x[0].isalpha() | x[1].isalpha():continue
    # Initialization 값을 '2개' 입력받지 않거나 글자만 있으면

    for n in range(2): 
      if '/' in x[n]:
        numerator, denominator = map(int, x[n].split('/'))
        x[n] = f(numerator, denominator)
      else:
        if '.' in x[n] : 
          x[n] = float(x[n])
        else: 
          x[n] = int(x[n])
    # a, b를 분수, 실수, 정수꼴로 바꾸기 

    print('[F(x)]{},{} = '.format(x[0], x[1]), end='')
    # '[F(x)]a, b =' 출력 

    value = 0
    for n in range(len(y)):
      y[n] = y[n] / (len(y)-1-n+1)
      y[n] = y[n] * (x[1]**(len(y)-1-n+1) - x[0]**(len(y)-1-n+1))
      value = value + y[n]
    # value = 각 항을 정적분하고 더한 value

    def Convertible_to_decimal(Share): 
      for prime_number in (2, 5): 
        while Share % prime_number == 0: 
          Share = int(Share / prime_number) 
      if Share == 1:
        return True 
      else : 
        return False 
    # 분수를 소수로 나타낼 수 있나 판별하는 함수 정의

    if Convertible_to_decimal(value.denominator) & (value.denominator != 1): 
      print(float(value))
    else :
      print(value)
    # 값을, 소수꼴로 바꿀 수 있으면 바꾸고, 출력
