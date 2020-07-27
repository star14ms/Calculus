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

  for term in y:
    conversion = str.maketrans('1234567890-/.', 'ooooooooooooo')
    for m in range(len(term)):
      rational_material = term[m].translate(conversion)
      if not 'o' in rational_material: rational_num = False

    if '/' in term:
      if term.count('/') != 1: rational_num = False
      if term.index('/') == 0 | term.index('/') == len(term)-1: rational_num = False
      if rational_num:
        numerator, denominator = map(float, term.split('/'))
        if denominator == 0: rational_num = False
    
    if '.' in term:
      if ('/' in term) & rational_num:
        a, b = term.split('/')
        if numerator.count('.') == 2 | denominator.count('.') == 2: rational_num = False
      else:  
        if term.count('.') != 1: rational_num = False
        if term.index('.') == 0 | term.index('.') == len(term)-1: rational_num = False

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
    elif '.' in y[n]:
        numerator, denominator = int(y[n].replace('.','')), 10*(len(str(y[n]))-1-str(y[n]).index('.'))
    else: 
        numerator, denominator = int(y[n]), 1

    y[n] = f(numerator, denominator)
  # 각 항의 계수를 분수꼴로 바꾸기 

  print('f(x) =', end='') 
  # 'f(x) =' 출력

  for n in range(len(y)):
  # 각 항의 계수에서
    if float(y[n]) == 0:
      if n != len(y)-1:
        continue
      else:
        if len(y) == 1:
          print(' 0')
          continue
        else: 
          print()
          continue
    # 항이 0이면 생략

    z = {}
    # 출력을 위해 변환시킨 항을 저장할 곳

    if (y[n] == 1 or y[n] == -1) & (n != len(y) - 1):
      z[n] = str(y[n]).replace('1','')
    else:
      z[n] = str(y[n])
    # 계수가 1 or -1이면 1생략 (상수항 제외)

  def adding_sign_space(n):
    z[n] = z[n].replace('-',' - ')
    if n == 0 : 
      z[n] = ' ' + z[n]
    elif (not '-' in z[n]):
      z[n] = ' + ' + z[n]
  # to definite a fuction adding sign & space
 
    adding_sign_space(n)
    if n == len(y)-2:
      term = term + 'x'
    elif n != len(y)-1:
      term = term + 'x^' + str(len(y)-1-n)
    # 변수기호, 그 변수의 지수 추가 (len(y)-1-n : 내림차순 차수)

    if n != len(y)-1: 
      print(term, end='')
    else:
      print(term)
    # 출력

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
      if y[n] == 0:   
          if n != len(y)-2: 
            continue
          else: 
            print()
            continue
      # 계수가 0이면 그 항은 생략

      degree = len(y)-1-n
      y[n] = degree * y[n]
      # 새 계수 = 차수 * 계수

      if (y[n] == 1 or y[n] == -1) & (n != len(y)-2):
        z[n] = str(y[n]).replace('1','')
      else: 
        z[n] = str(y[n])
      # 계수가 1 or -1이면 1생략 (상수항 제외)

      adding_sign_space(n)
      if n == len(y)-3:
        z[n] = z[n] + 'x'
      elif n != len(y)-2:
        z[n] = z[n] + 'x^' + str(degree-1)
      # 부호 & 공백 & 변수기호 & -1한 지수 추가

      if n != len(y)-2:
        print(z[n], end='')
      else: 
        print(z[n])
      # 출력
################################################################################################
  elif c == '2':
  # 부정적분을 골랐을 때
    print('F(x) =', end='')
    # 'F(x) =' 출력

    if (len(y) == 1) & (y[0] == 0):
      print(' 0'); continue
    # 항이 0 하나면 0 출력

    for n in range(len(y)):
    # 각 항의 계수에서
      if y[n] == 0: 
        if n != len(y)-1: 
          continue
        else: 
          print()
          continue
      # 계수가 0이면 그 항은 생략

      degree = len(y)-1-n
      y[n] = y[n] / (degree+1)
      # 새 계수 = 계수 / (차수 + 1)

      if y[n] == 1 or y[n] == -1:
        z[n] = str(y[n]).replace('1','')
      else: 
        z[n] = str(y[n])
      # 계수가 1 or -1이면 1생략
        
      adding_sign_space(n)
      if n == len(y)-1:
        z[n] = z[n] + 'x'
      else :
        z[n] = z[n] + 'x^' + str(degree+1)
      # 부호 & 공백 & 변수기호 & +1한 지수 추가

      if n != len(y)-1:
        print(z[n], end='')
      else: 
        print(z[n],'+ C')
      # 출력 (적분상수 포함)
################################################################################################
  elif c == '3' :
  # 정적분을 골랐을 때
  
    x = input('range [a, b] : ').split()
    # 범위 a, b 입력받음
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

    a, b = x[0], x[1]
    print('[F(x)]{},{} = '.format(a, b), end='')
    # '[F(x)]a, b =' 출력 

    value = 0
    for n in range(len(y)):
      degree = len(y)-1-n
      y[n] = y[n] / (degree+1)
      y[n] = y[n] * (b**(degree+1) - a**(degree+1))
      value = value + y[n]
    # value = 각 항을 정적분하고 더한 value

    def Convertible_to_decimal(Share): 
      for prime_number in (2, 5): 
        while Share % prime_number == 0: 
          Share = Share / prime_number
      if Share == 1:
        return True 
      else : 
        return False 
    # 분수를 소수로 나타낼 rational_number 있나 판별하는 함수 정의
    
    if Convertible_to_decimal(value.denominator) & (value.denominator != 1): 
      print(float(value))
    else :
      print(value)
    # 값을, 소수꼴로 바꿀 rational_number 있으면 바꾸고, 출력
