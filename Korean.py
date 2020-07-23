from fractions import Fraction as f
# 분수꼴 추가히기
print('미적분 너무 쉬워!\n')
print('각 항의 계수를 내림차순으로 쓰시오')
print('(띄어쓰기로 구분)')
print('(중간에 없는 항도 0을 써서 표시)')
# 설명 출력
################################################################################################
while True:
  print('ㅡ' * 16)
  y = input().split()
  # 줄 치고, 함수 입력 받기

  if y == []: continue 
  # 입력 받은 게 없으면 초기화

  숫자 = True
  for n in range(len(y)):
    if y[n].isalpha(): 숫자 = False
  if 숫자 == False: continue
  # 각 항중 하나라도 알파벳만 있으면 초기화

  for n in range(len(y)): 
    if '/' in y[len(y)-1-n]:
      분자, 분모 = map(int, y[len(y)-1-n].split('/'))
    else:
      분자, 분모 = int(y[len(y)-1-n]), 1
    y[len(y)-1-n] = f(분자, 분모)
  # 각 항을 분수꼴로 바꾸기 ( len(y)-1-n : 차수 )

  print('f(x) =', end='') 
  for n in range(len(y)):
  # 입력받은 항들을 변수, 차수도 넣어 다시 출력

    if (y[n] == f(1, 1)) & (n != len(y) - 1):
      y[n] = ''
    # 계수가 1인 항은 1생략

    if n == len(y)-1:
      항 = str(y[n])
    elif n == len(y)-2:
      항 = str(y[n]) + 'x'
    else :
      항 = str(y[n]) + 'x^' + str(len(y)-1-n)
    # 변수기호, 그 변수의 지수 추가

    항 = 항.replace('-',' - ')
    if n == 0 : 
        항 = ' ' + 항
    elif (not '-' in 항):
      항 = ' + ' + 항
    # 부호, 공백 추가

    항분리 = 항.split('x')
    if n == 0 :
      if 항분리[0] == ' 0':
        continue
    if n != len(y)-1: 
      if 항분리[0] == ' + 0':
        continue
      else: 
        print(항, end='')
    else:
      if 항분리[0] == ' + 0': 
        print()
      else:
        print(항)
    # 문자를 붙여서 출력 (항이 0이면 생략)

    if y[n] == '':
      y[n] = f(1, 1)
    # 위에서 생략한 계수 1을 다시 1로 만들기

  c = input('미분(1) | 부정적분(2) | 정적분(3) : ')
  # 미분, 부정적분, 정적분 중에 고르기
################################################################################################
  if c == '미분' or c == '1' :
    # 미분을 골랐을 때

    print("f'(x)=", end='')
    # "f'(x)=" 출력
  
    for n in range(len(y)):
    # 각 항에서

      y[n] = (len(y)-1-n) * y[n]
      # 새 계수 = 차수 * 계수

      if y[n] == 0: 
        if len(y) == 1: 
          print(' 0'); continue
        else: 
          if n == len(y)-1: 
            print()
            continue
          else: 
            continue
      # 계수가 0이면 그 항은 생략

      if (y[n] == f(1, 1)) & (n != len(y) - 1):
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
  elif c == '부정적분' or c == '2':
  # 정적분을 골랐을 때

    print('F(x) =', end='')
    # 'F(x) =' 출력

    for n in range(len(y)):
    # 각 항에서

      y[n] = y[n] / (len(y)-1-n+1)
      # 새 계수 = 계수 / 차수 + 1

      if y[n] == 0: 
        if len(y) == 1: 
          print(' 0'); continue
        else: 
          if n == len(y)-1: 
            print()
            continue
          else: 
            continue
      # 계수가 0이면 그 항은 생략

      if (y[n] == f(1, 1)) & (n != len(y) - 1):
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
  elif c == '정적분' or c == '3' :
  # 정적분을 골랐을 때

    x = input('범위 [a, b] : ').split()
    # 범위 a, b 입력받음

    if len(x) != 2 :continue
    elif x[0].isalpha() | x[1].isalpha():continue
    # 입력받은 값이 3개거나 알파벳만 있으면 초기화

    for n in range(2): 
      if '/' in x[n]:
        분자, 분모 = map(int, x[n].split('/'))
        x[n] = f(분자, 분모)
      else:
        if '.' in x[n] : 
          x[n] = float(x[n])
        else: 
          x[n] = int(x[n])
    # 입력받은 값을 분수, 실수, 정수꼴로 바꾸기

    print('[F(x)]{},{} = '.format(x[0], x[1]), end='')
    # '[F(x)]a, b =' 출력 

    값 = 0
    for n in range(len(y)):
      y[n] = y[n] / (len(y)-1-n+1)
      y[n] = y[n] * (x[1]**(len(y)-1-n+1) - x[0]**(len(y)-1-n+1))
      값 = 값 + y[n]
    # 값 = 각 항을 정적분하고 더한 값

    def 소수변환가능(n): 
      for 소수 in (2, 5): 
        while 몫%소수 == 0: 
          몫=int(몫/소수) 
      if 몫==1:
        return True 
      else : 
        return False 
    # 분수를 소수로 나타낼 수 있나 판별하는 함수 정의

    if 소수변환가능(값.denominator) & 값.denominator!=1 : 
      print(float(값))
    else :
      print(값)
    # 값을, 소수로 변환할 수 있으면 하고, 출력
