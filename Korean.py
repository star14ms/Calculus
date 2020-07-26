from fractions import Fraction as f
# 분수꼴 추가히기
print('미적분 너무 쉬워!\n')
print('함수의 각 항의 계수를 내림차순으로 쓰시오')
print('(띄어쓰기로 구분)')
print('(중간에 없는 항도 0을 써서 표시)')
# 설명 출력
################################################################################################
while True: # 반복
  print('ㅡ' * 16) # 줄 치기
  y = input().split()
  # 함수의 각 항의 계수 입력 받기

  유리수 = True

  if y == []: 유리수 = False

  for n in range(len(y)):
    변환 = str.maketrans('1234567890/.', '111111111111')
    for m in range(len(y[n])):
      유리수_재료 = y[n][m].translate(변환)
      if not '1' in 유리수_재료: 유리수 = False

    if '/' in y[n]:
      if y[n].count('/') != 1: 유리수 = False
      if y[n].index('/') == 0 | y[n].index('/') == len(y[n])-1: 유리수 = False
      if 유리수:
        분자, 분모 = map(float, y[n].split('/'))
        if 분모 == 0: 유리수 = False
    
    if '.' in y[n]:
      if ('/' in y[n]) & 유리수:
        a, b = y[n].split('/')
        for m in (a, b):
          if m.count('.') > 1: 유리수 = False
      else:  
        if y[n].count('.') != 1: 유리수 = False
        if y[n].index('.') == 0 | y[n].index('.') == len(y[n])-1: 유리수 = False

  if 유리수 == False: continue
  # 입력x | 계수 하나라도 (유리수x | 분모=0) :초기화

  for n in range(len(y)): 
    if '/' in y[n] and '.' in y[n]:
      분자, 분모 = map(float, y[n].split('/'))
      소수자릿수 = 0
      for m in (분자, 분모):
          o = str(m).split('.')
          if o[1] != 0:
            소수자릿수 += len(str(m))-1-str(m).index('.')
      분자, 분모 = int(10**소수자릿수*분자), int(10**소수자릿수*분모)
    else:
      if '/' in y[n]:
        분자, 분모 = map(int, y[n].split('/'))
      elif not '.' in y[n]:
        분자, 분모 = int(y[n]), 1
      else: 
        분모 = 10*(len(str(y[n]))-1-str(y[n]).index('.'))
        분자 = int(y[n].replace('.',''))
    y[n] = f(분자, 분모)
  # 각 항의 계수를 분수꼴로 바꾸기 

  print('f(x) =', end='') 
  # 'f(x) =' 출력

  for n in range(len(y)):
  # 각 항의 계수에서
    if (y[n] == f(1, 1)) & (n != len(y) - 1):
      y[n] = ''
    # 계수가 1인 항은 1생략 (len(y)-1 : 상수항)

    if n == len(y)-1:
      항 = str(y[n])
    elif n == len(y)-2:
      항 = str(y[n]) + 'x'
    else :
      항 = str(y[n]) + 'x^' + str(len(y)-1-n)
    # 변수기호, 그 변수의 지수 추가 (len(y)-1-n : 내림차순)

    항 = 항.replace('-',' - ')
    if n == 0 : 
        항 = ' ' + 항
    elif (not '-' in 항):
      항 = ' + ' + 항
    # 부호, 공백 추가

    x앞쪽 = 항.split('x')
    if n == 0 :
      if x앞쪽[0] == ' 0':
        continue
    if n != len(y)-1: 
      if x앞쪽[0] == ' + 0':
        continue
      else: 
        print(항, end='')
    else:
      if x앞쪽[0] == ' + 0': 
        print()
      else:
        print(항)
    # 출력 (항이 0이면 생략)

    if y[n] == '':
      y[n] = f(1, 1)
    # 위에서 생략한 계수 1을 다시 1로 만들기

  c = input('미분(1) | 부정적분(2) | 정적분(3) : ')
  # 미분, 부정적분, 정적분 중 고르기
################################################################################################
  if c == '미분' or c == '1' :
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
  elif c == '부정적분' or c == '2':
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
  elif c == '정적분' or c == '3' :
  # 정적분을 골랐을 때
    x = input('범위 [a, b] : ').split()
    # 범위 a, b 입력받음 ( a = x[0], b = x[1] )

    if len(x) != 2 :continue
    elif x[0].isalpha() | x[1].isalpha():continue
    # 값을 '2개' 입력받지 않거나 글자만 있으면 초기화

    for n in range(2): 
      if '/' in x[n]:
        분자, 분모 = map(int, x[n].split('/'))
        x[n] = f(분자, 분모)
      else:
        if '.' in x[n] : 
          x[n] = float(x[n])
        else: 
          x[n] = int(x[n])
    # a, b를 분수, 실수, 정수꼴로 바꾸기 

    print('[F(x)]{},{} = '.format(x[0], x[1]), end='')
    # '[F(x)]a, b =' 출력 

    값 = 0
    for n in range(len(y)):
      y[n] = y[n] / (len(y)-1-n+1)
      y[n] = y[n] * (x[1]**(len(y)-1-n+1) - x[0]**(len(y)-1-n+1))
      값 = 값 + y[n]
    # 값 = 각 항을 정적분하고 더한 값

    def 소수변환가능(몫): 
      for 소수 in (2, 5): 
        while 몫 % 소수 == 0: 
          몫 = 몫 / 소수 
      if 몫 == 1:
        return True 
      else : 
        return False 
    # 분수를 소수로 나타낼 유리수 있나 판별하는 함수 정의

    if 소수변환가능(값.denominator) & (값.denominator != 1): 
      print(float(값))
    else:
      print(값)
    # 값을, 소수꼴로 바꿀 유리수 있으면 바꾸고, 출력
