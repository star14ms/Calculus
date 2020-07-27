from fractions import Fraction as f
# 분수꼴 추가히기
print('미적분 너무 쉬워!\n')
print('함수의 각 항의 계수를 내림차순으로 쓰시오')
print('(띄어쓰기로 구분)')
print('(중간에 없는 항도 0을 써서 표시)')
# 설명 출력
################################################################################################################################ 준비 작업
z = {}
# 출력을 위해 변환시킨 항을 저장할 곳
c = 0
# 선택 전(0), 미분('1'), 부정적분('2'), 정적분('3')

def 계수1_생략(n):
  if y[n] == 1 or y[n] == -1:
    if ((c == 0) & (n != len(y)-1)) | ((c == '1') & (n != len(y)-2)) | (c == '2'):
      z[n] = str(y[n]).replace('1','')
    else:
      z[n] = str(y[n])
  else:
    z[n] = str(y[n])
# 계수가 1 or -1이면 1생략 (상수항 제외)

def 부호_공백_추가(n):
  z[n] = z[n].replace('-',' - ')
  if n == 0 : 
     z[n] = ' ' + z[n]
  elif (not '-' in z[n]):
     z[n] = ' + ' + z[n]
# 계수에 부호, 공백 추가

def 출력(n):
  if ((c == 0) & (n != len(y)-1)) | ((c == '1') & (n != len(y)-2)) | ((c == '2') & (n != len(y)-1)):
    print(z[n], end='')
  elif c != '2': 
    print(z[n])
  else: 
    print(z[n],'+ C')
# 항들 조합해서 출력

def 소수변환가능(몫): 
  for 소수 in (2, 5): 
    while 몫 % 소수 == 0: 
      몫 = 몫 / 소수 
  if 몫 == 1:
    return True 
  else : 
    return False 
# 분수를 소수로 나타낼 유리수 있나 판별
################################################################################################################################ 본문(입력)
while True: # 반복
  print('ㅡ' * 16) # 줄 치기
  c = 0 # 초기화
  y = input().split()
  # 함수의 각 항의 계수 입력 받기

  유리수 = True

  if y == []: 유리수 = False # 입력 없음
  
  for 계수 in y:
    변환 = str.maketrans('1234567890-/.', 'ooooooooooooo')
    for m in range(len(계수)):
      유리수_재료 = 계수[m].translate(변환)
      if not 'o' in 유리수_재료: 유리수 = False
  
    if '/' in 계수:
      if 계수.count('/') != 1: 유리수 = False
      if 계수.index('/') == 0 | 계수.index('/') == len(계수)-1: 유리수 = False
      if 유리수:
        분자, 분모 = map(float, 계수.split('/'))
        if 분모 == 0: 유리수 = False # 분모 = 0
    
    if '.' in 계수:
      if ('/' in 계수) & 유리수:
        분자, 분모 = 계수.split('/')
        if 분자.count('.') == 2 | 분모.count('.') == 2: 유리수 = False
      else:  
        if 계수.count('.') != 1: 유리수 = False
        if 계수.index('.') == 0 | 계수.index('.') == len(계수)-1: 유리수 = False

  if 유리수 == False: continue
  # 입력이 없거나, 계수 하나라도 no유리수 또는 분모가 0이면 초기화

  for n in range(len(y)):
    if '/' in y[n] and '.' in y[n]:
      분자, 분모 = map(float, y[n].split('/'))
      소수자릿수 = 0
      for m in (분자, 분모):
          o = str(m).split('.')
          if o[1] != 0:
            소수자릿수 += len(str(m))-1-str(m).index('.')
      분자, 분모 = int(10**소수자릿수*분자), int(10**소수자릿수*분모)
    elif '/' in y[n]:
        분자, 분모 = map(int, y[n].split('/'))
    elif '.' in y[n]:
        분자, 분모 = int(y[n].replace('.','')), 10*(len(str(y[n]))-1-str(y[n]).index('.'))
    else: 
        분자, 분모 = int(y[n]), 1
        
    y[n] = f(분자, 분모)
  # 각 항의 계수를 분수꼴로 바꾸기 

  print('f(x) =', end='') 
  # 'f(x) =' 출력

  for n in range(len(y)):
  # 각 항에서
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
    # 계수가 0이면 생략

    계수1_생략(n)
    부호_공백_추가(n)
    if n == len(y)-2:
      z[n] = z[n] + 'x'
    elif n != len(y)-1:
      z[n] = z[n] + 'x^' + str(len(y)-1-n)
    # 변수기호 & 지수 추가 (len(y)-1-n : 내림차순 차수)
    출력(n)

  c = input('미분(1) | 부정적분(2) | 정적분(3) : ')
  # 미분, 부정적분, 정적분 중 고르기
################################################################################################################################ 미분
  if c == '미분' or c == '1' :
  # 미분을 골랐을 때
    print("f'(x)=", end='')
    # "f'(x)=" 출력

    if len(y) == 1: 
      print(' 0'); continue
    # 항이 하나면 0 출력

    for n in range(len(y)-1):
    # 각 항에서
      if y[n] == 0:   
        if n != len(y)-2: 
          continue
        else: 
          print()
          continue
      # 계수가 0이면 그 항은 생략 

      차수 = len(y)-1-n
      y[n] = 차수 * y[n]
      # 새 계수 = 차수 * 계수
      
      계수1_생략(n)
      부호_공백_추가(n)
      if n == len(y)-3:
        z[n] = z[n] + 'x'
      elif n != len(y)-2:
        z[n] = z[n] + 'x^' + str(차수-1)        
      출력(n)
################################################################################################################################ 부정적분
  elif c == '부정적분' or c == '2':
  # 부정적분을 골랐을 때
    print('F(x) =', end='')
    # 'F(x) =' 출력

    if (len(y) == 1) & (y[0] == 0):
      print(' 0'); continue
    # 항이 0 하나면 0 출력

    for n in range(len(y)):
    # 각 항에서
      if y[n] == 0: 
        if n != len(y)-1: 
          continue
        else: 
          print()
          continue
      # 계수가 0이면 그 항은 생략

      차수 = len(y)-1-n
      y[n] = y[n] / (차수+1)
      # 새 계수 = 계수 / (차수 + 1)

      계수1_생략(n)
      부호_공백_추가(n)
      if n == len(y)-1:
        z[n] = z[n] + 'x'
      else:
        z[n] = z[n] + 'x^' + str(차수+1)
      출력(n)
################################################################################################################################ 정적분
  elif c == '정적분' or c == '3' :
  # 정적분을 골랐을 때

    x = input('범위 [a, b] : ').split()
    # 범위 a, b 입력받음
    if len(x) != 2 :continue
    elif x[0].isalpha() | x[1].isalpha():continue
    # 값을 딱 2개만 받지 않거나, 글자만 있으면 초기화

    for n in range(2): 
      if '/' in x[n]:
        if '.' in str(y[n]):
          분자, 분모 = map(float, y[n].split('/'))
          소수자릿수 = 0
          for m in (분자, 분모):
              o = str(m).split('.')
              if o[1] != 0:
                소수자릿수 += len(str(m))-1-str(m).index('.')
          분자, 분모 = int(10**소수자릿수*분자), int(10**소수자릿수*분모)
        else:
          분자, 분모 = map(int, x[n].split('/'))
        x[n] = f(분자, 분모)
      else:
        if '.' in x[n] : 
          x[n] = float(x[n])
        else: 
          x[n] = int(x[n])
    # a, b를 분수, 실수, 정수꼴로 바꾸기 
    
    a, b = x[0], x[1]
    print('[F(x)]{},{} = '.format(a, b), end='')
    # '[F(x)]a, b =' 출력 

    값 = 0
    for n in range(len(y)):
      차수 = len(y)-1-n
      y[n] = y[n] / (차수+1)
      y[n] = y[n] * (b**(차수+1) - a**(차수+1))
      값 = 값 + y[n]
    # 값 = 각 항을 정적분하고 모두 더한 값

    if 소수변환가능(값.denominator) & (값.denominator != 1): 
      print(float(값))
    else:
      print(값)
    # 값을, 소수꼴로 바꿀 수 있으면 바꾸고, 출력
