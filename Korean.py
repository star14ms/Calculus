# 본문 시작인 106줄부터 읽는 것을 추천

from fractions import Fraction as f
# to add fractional form
################################################################################################ 함수 정의 및 가져오기
def 유리수_판별(y):
  if y == []: return False # 입력 없음
  
  for 항 in y:
    변환 = str.maketrans('1234567890-/.', 'ooooooooooooo')
    for m in range(len(항)):
      유리수_재료 = 항[m].translate(변환)
      if not 'o' in 유리수_재료: return False
  
    if '/' in 항:
      if 항.count('/') != 1: return False
      if 항.index('/') == 0 | 항.index('/') == len(항)-1: return False
      분자, 분모 = map(float, 항.split('/'))
      if 분모 == 0: return False # 분모 = 0
    
    if '.' in 항:
      if '/' in 항:
        분자, 분모 = 항.split('/')
        if 분자.count('.') == 2 | 분모.count('.') == 2: return False
      else:  
        if 항.count('.') != 1: return False
        if 항.index('.') == 0 | 항.index('.') == len(항)-1: return False      
  return True
# 입력이 없거나, 분모가 0일 때도 유리수 = False 

def 계수_분수꼴로_바꾸기(n):
  if '/' in y[n] and '.' in y[n]: # y[n] : y의 n번째 항의 계수
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
    y[n] = float(y[n])
    분자, 분모 = int(str(y[n]).replace('.','')), 10*(len(str(y[n]))-1-str(y[n]).index('.'))
  else: 
    분자, 분모 = int(y[n]), 1   

  y[n] = f(분자, 분모)
# 항의 계수를 분수꼴로 바꾸기 

def 계수1_생략(n):
  if y[n] == 1 or y[n] == -1:
    if (c == 0 and n != len(y)-1) | (c == '1' and n != len(y)-2) | (c == '2'):
      z[n] = str(y[n]).replace('1','')
    else:
      z[n] = str(y[n])
  else:
    z[n] = str(y[n])
# 항의 계수가 1 or -1이면 1생략 (상수항 제외)

def 부호_공백_추가(n):
  z[n] = z[n].replace('-',' - ')
  if n == 0 : 
     z[n] = ' ' + z[n]
  elif (not '-' in z[n]):
     z[n] = ' + ' + z[n]
# 항의 계수에 부호, 공백 추가

def 변수기호_지수_추가(n):
  if (c==0 and n==len(y)-2) | (c=='1' and n==len(y)-3) | (c=='2' and n==len(y)-1):
    z[n] = z[n] + 'x'
  else:
    if c==0 and n!=len(y)-1:
      z[n] = z[n] + 'x^' + str(차수)
    if c=='1' and n!=len(y)-2:
      z[n] = z[n] + 'x^' + str(차수-1)
    if c=='2':
      z[n] = z[n] + 'x^' + str(차수+1)
# 계수에 변수기호, 지수 추가

def 항_정보_추가(n):
  계수1_생략(n)
  부호_공백_추가(n)
  변수기호_지수_추가(n)
# 바로 위에 있는 세개의 함수를 한줄로

def 출력(n):
  if (c == 0 and n != len(y)-1) | (c == '1' and n != len(y)-2) | (c == '2' and n != len(y)-1):
    print(z[n], end='')
  elif c == '2': 
    print(z[n],'+ C')
  else:
    print(z[n])
# 항들 조합해서 출력

def 소수변환가능(분모): 
  for 소수 in (2, 5): 
    while 분모 % 소수 == 0: 
      분모 = 분모 / 소수 
  if 분모 == 1:
    return True 
  else : 
    return False 
# 분수를 소수로 나타낼 수 있나 판별
################################################################################################ 입력 단계
print('미적분 너무 쉬워!\n')
print('함수의 각 항의 계수부분만 내림차순으로 쓰시오')
print('(띄어쓰기로 구분)')
print('(중간에 없는 항도 0을 써서 표시)')
# 설명 출력

while True: # 반복
  c = 0  # 코드 진행 상태 : 입력 단계(0), 미분('1'), 부정적분('2'), 정적분('3')
  print('ㅡ' * 16) # 줄 치기
  
  y = input().split() 
  # 함수의 각 항의 계수 입력 받기

  if 유리수_판별(y) == False: continue
  # 유리수가 아니면 초기화

  z = {} # 출력을 위해 변환시킨 항을 저장할 곳

  print('f(x) =', end='') # 'f(x) =' 출력

  for n in range(len(y)): # 각 항에서
    계수_분수꼴로_바꾸기(n)
    if y[n] == 0: # 계수가 0이면 생략
      if len(y) == 1:
        print(' 0')
      elif n == len(y)-1:
        print()
    else: # 아니면 항 정보 추가하여 출력
      차수 = len(y)-1-n # 내림차순
      항_정보_추가(n)
      출력(n)

  c = input('미분(1) | 부정적분(2) | 정적분(3) : ')
  # 미분, 부정적분, 정적분 중 고르기
################################################################################################ 미분
  if c == '미분' or c == '1' :
  # 미분을 골랐을 때
    print("f'(x)=", end='') # "f'(x)=" 출력

    if len(y) == 1: 
      print(' 0'); continue
    # 항이 하나면 0 출력

    for n in range(len(y)-1): # 각 항에서 (상수항 빼고)
      if y[n] == 0: # 계수가 0이면 생략
        if n == len(y)-2: 
          print()
      else: # 아니면 미분하여 출력
        차수 = len(y)-1-n
        y[n] = 차수 * y[n]
        항_정보_추가(n)
        출력(n)
################################################################################################ 부정적분
  if c == '부정적분' or c == '2':
  # 부정적분을 골랐을 때
    print('F(x) =', end='') # 'F(x) =' 출력

    for n in range(len(y)): # 각 항에서
      if y[n] == 0: # 계수가 0이면 생략
        if len(y) == 1:
          print(' 0')
        elif n != len(y)-1:
          print()
      else: # 아니면 적분하여 출력 
        차수 = len(y)-1-n
        y[n] = y[n] / (차수+1)
        항_정보_추가(n)
        출력(n) # 적분상수 C도 추가
################################################################################################ 정적분
  if c == '정적분' or c == '3' :
  # 정적분을 골랐을 때
    x = input('범위 [a, b] : ').split()
    # 범위 a, b 입력받기

    if len(x) != 2 :continue
    # 값을 2개를 받지 않았다면 초기화

    if 유리수_판별(x) == False: continue
    # 유리수가 아니면 초기화

    for n in range(2): 
      if '/' in x[n]:
        if '.' in x[n]:
          분자, 분모 = map(float, x[n].split('/'))
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
    # a, b를 분수, 소수, 정수꼴로 바꾸기 
    
    a, b = x[0], x[1]

    print('[F(x)]{},{} = '.format(a, b), end='') # '[F(x)]a, b =' 출력 

    값 = 0
    for n in range(len(y)):
      차수 = len(y)-1-n
      y[n] = y[n] / (차수+1)
      y[n] = y[n] * (b**(차수+1) - a**(차수+1))
      값 = 값 + y[n]
    # 값 = 각 항을 정적분하고 모두 더한 값

    if 소수변환가능(값.denominator) and 값.denominator != 1: 
      print(float(값))
    else:
      print(값)
    # 값을, 소수꼴로 바꿀 수 있으면 바꾸고, 출력
