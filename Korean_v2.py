# 본문 시작인 89줄부터 읽는 것을 추천

from fractions import Fraction as f
# 분수꼴 추가하기
################################################################################################ 함수 정의 및 가져오기
def 유리수_판별(y):
  if y == []: return False # 입력 없음
  
  for 항 in y:
    변환 = str.maketrans('1234567890-/.', 'ooooooooooooo')
    for m in range(len(항)):
      유리수_재료 = 항[m].translate(변환)
      if not 'o' in 유리수_재료: return False
  
    if '/' in 항:
      if '.' in 항:
        분자, 분모 = 항.split('/')
        if 분자.count('.')>1 | 분모.count('.')>1: return False
      else:
        if 항.count('/')!=1: return False
        if 항.index('/')==0 | 항.index('/') == len(항)-1: return False
        분자, 분모 = map(float, 항.split('/'))
        if 분모 == 0: return False # 분모 = 0
    elif '.' in 항:
      if 항.count('.')!=1: return False
      if 항.index('.')==0 | 항.index('.') == len(항)-1: return False  
  return True
# 입력이 없거나, 분모가 0일 때도 유리수 = False 

def 계수_분수꼴로_바꾸기(y):
  for n in range(len(y)):
    if '/' in y[n] and '.' in y[n]: # y[n] : y의 n번째 항의 계수
      분자, 분모 = map(float, y[n].split('/'))
      소수자릿수 = 0
      for m in (분자, 분모):
        if '.' in str(m):
          m = str(m).rstrip('0')
          소수자릿수 += len(m)-1-m.index('.')
      분자, 분모 = int(10**소수자릿수*분자), int(10**소수자릿수*분모)
    elif '/' in y[n]:
      분자, 분모 = map(int, y[n].split('/'))
    elif '.' in y[n]:
      y[n] = float(y[n])
      분자, 분모 = int(str(y[n]).replace('.','')), 10*(len(str(y[n]))-1-str(y[n]).index('.'))
    else: 
      분자, 분모 = int(y[n]), 1
    y[n] = f(분자, 분모)

def 계수1_생략(y):
  for n in range(len(y)):
    if n!=0 and (y[n]==1 or y[n]==-1):
      항정보.append(str(y[n]).replace('1',''))
    else:
      항정보.append(str(y[n]))
      
def x기호_지수_추가(y):
  for n in range(len(y)):
    항정보[n] = 항정보[n] + 'x^' + str(n)

def 제곱01_생략(y):
  항정보[0] = 항정보[0].replace('x^0','')
  if len(y)>1:
    항정보[1] = 항정보[1].replace('^1','')
  
def 계수0_생략(y):
  for n in range(len(y)):
    if 항정보[len(y)-1-n].find('0')==0:
      del 항정보[len(y)-1-n]

def 인간맞춤형_식출력(y):
  계수1_생략(y)
  x기호_지수_추가(y)
  제곱01_생략(y)
  계수0_생략(y)
  항정보.reverse()
  print('+'.join(항정보).replace('+-','-').replace('-',' - ').replace('+',' + ').lstrip(' '))
  del 항정보[:]

def 소수변환가능(분모): 
  for 소수 in (2, 5): 
    while 분모%소수 == 0: 
      분모 = 분모/소수 
  if 분모==1:
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
  y.reverse()
  # 함수의 각 항의 계수 입력 받기, 오름차순으로 정렬
  
  if 유리수_판별(y) == False: continue
  # 유리수가 아니면 초기화

  계수_분수꼴로_바꾸기(y)

  항정보 = [] # 출력을 위해 변환시킨 항을 저장할 곳

  print('f(x) = ', end='') # 'f(x) =' 출력
  인간맞춤형_식출력(y)

  c = input('미분(1) | 부정적분(2) | 정적분(3) : ')
  # 미분, 부정적분, 정적분 중 고르기
################################################################################################ 미분
  if c == '미분' or c == '1' :
  # 미분을 골랐을 때

    if len(y) == 1: 
      print('0'); continue # 항이 하나면 0 출력

    for n in range(len(y)): # 각 항에서
      y[n] = n * y[n] # 새 계수 = 차수 x 계수
    del y[0] # 상수항 사라짐

    print("f'(x)= ", end='') # "f'(x)=" 출력
    인간맞춤형_식출력(y)
################################################################################################ 부정적분
  if c == '부정적분' or c == '2':
  # 부정적분을 골랐을 때

    if y[0] == 0 and len(y) == 1: # 항이 0 하나면 0 출력
      print('0'); continue

    for n in range(len(y)): # 각 항에서
      y[n] = y[n] / (n+1) # 새 계수 = 계수 / (차수+1)
    y.reverse()
    y.append('C') # 적분상수 C 추가
    y.reverse()

    print('F(x) = ', end='') # 'F(x) =' 출력
    인간맞춤형_식출력(y)
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
            if '.' in str(m):
              m = str(m).rstrip('0')
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
    
    값 = 0
    for n in range(len(y)):
      y[n] = y[n] / (n+1)
      y[n] = y[n] * (b**(n+1) - a**(n+1))
      값 = 값 + y[n]
    # 값 = 각 항을 정적분하고 모두 더한 값

    print('[F(x)]{},{} = '.format(a, b), end='') # '[F(x)]a, b =' 출력 

    if 소수변환가능(값.denominator) and 값.denominator != 1: 
      print(float(값))
    else:
      print(값)
    # 값을, 소수꼴로 바꿀 수 있으면 바꾸고, 출력
