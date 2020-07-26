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

  rational_num = True

  if y == []: rational_num = False

  for n in range(len(y)):
    conversion = str.maketrans('1234567890/.', '111111111111')
    for m in range(len(y[n])):
      rational_material = y[n][m].translate(conversion)
      if not '1' in rational_material: rational_num = False

    if '/' in y[n]:
      if y[n].count('/') != 1: rational_num = False
      if y[n].index('/') == 0 | y[n].index('/') == len(y[n])-1: rational_num = False
      if rational_num:
        numerator, denominator = map(float, y[n].split('/'))
        if denominator == 0: rational_num = False
    
    if '.' in y[n]:
      if ('/' in y[n]) & rational_num:
        a, b = y[n].split('/')
        for m in (a, b):
          if m.count('.') > 1: rational_num = False
      else:  
        if y[n].count('.') != 1: rational_num = False
        if y[n].index('.') == 0 | y[n].index('.') == len(y[n])-1: rational_num = False

  if rational_num == False: continue
  # 입력x | 계수 하나라도 (유리수x | denominator=0) :초기화

  for n in range(len(y)): 
    if '/' in y[n] and '.' in y[n]:
      numerator, denominator = map(float, y[n].split('/'))
      decimal_digit = 0
      for m in (numerator, denominator):
          o = str(m).split('.')
          if o[1] != 0:
            decimal_digit += len(str(m))-1-str(m).index('.')
      numerator, denominator = int(10**decimal_digit*numerator), int(10**decimal_digit*denominator)
    elif '/' in y[n]:
        numerator, denominator = map(int, y[n].split('/'))
    elif not '.' in y[n]:
        numerator, denominator = int(y[n]), 1
    else: 
        denominator = 10*(len(str(y[n]))-1-str(y[n]).index('.'))
        numerator = int(y[n].replace('.',''))
    y[n] = f(numerator, denominator)
  # 각 항의 계수를 분수꼴로 바꾸기 

  print('f(x) =', end='') 
  # 'f(x) =' 출력

  for n in range(len(y)):
  # 각 항의 계수에서
    if (y[n] == f(1, 1)) & (n != len(y) - 1):
      y[n] = ''
    # 계수가 1인 항은 1생략 (len(y)-1 : 상수항)

    if n == len(y)-1:
      term = str(y[n])
    elif n == len(y)-2:
      term = str(y[n]) + 'x'
    else :
      term = str(y[n]) + 'x^' + str(len(y)-1-n)
    # 변수기호, 그 변수의 지수 추가 (len(y)-1-n : 내림차순)

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

  c = input('differential(1) | integral-indef(2), def(3): ')
  # 미분, 부정적분, 정적분 중 고르기
################################################################################################
  if c == '1' :
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
  elif c == '2':
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
  elif c == '3' :
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
    # 분수를 소수로 나타낼 rational_number 있나 판별하는 함수 정의

    if Convertible_to_decimal(value.denominator) & value.denominator != 1: 
      print(float(value))
    else :
      print(value)
    # 값을, 소수꼴로 바꿀 rational_number 있으면 바꾸고, 출력
