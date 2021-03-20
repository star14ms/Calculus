# 본문 시작인 89줄부터 읽는 것을 추천

from fractions import Fraction as f
# to add fractional form
################################################################################################ 함수 정의 및 가져오기
def Discrime_Rational_Num(y):
  if y == []: return False # 입력 없음
  
  for term in y:
    convertion = str.maketrans('1234567890-/.', 'ooooooooooooo')
    for m in range(len(term)):
      rational_material = term[m].translate(convertion)
      if not 'o' in rational_material: return False
  
    if '/' in term:
      if '.' in term:
        numerator, denominator = term.split('/')
        if numerator.count('.')>1 | denominator.count('.')>1: return False
      else:
        if term.count('/')!=1: return False
        if term.index('/')==0 | term.index('/') == len(term)-1: return False
        numerator, denominator = map(float, term.split('/'))
        if denominator==0: return False # denominator = 0
    elif '.' in term:
      if term.count('.')!=1: return False
      if term.index('.')==0 | term.index('.') == len(term)-1: return False      
  return True
# 입력이 없거나, 분모가 0일 때도 유리수 = False 

def Change_Coefficient_into_Fracion(y):
  for n in range(len(y)):
    if '/' in y[n] and '.' in y[n]: # y[n] : y의 n번째 항의 계수
      numerator, denominator = map(float, y[n].split('/'))
      digit_prime_num = 0
      for m in (numerator, denominator):
        if '.' in str(m):
          m = str(m).rstrip('0')
          digit_prime_num += len(m)-1-m.index('.')
      numerator, denominator = int(10**digit_prime_num*numerator), int(10**digit_prime_num*denominator)
    elif '/' in y[n]:
      numerator, denominator = map(int, y[n].split('/'))
    elif '.' in y[n]:
      y[n] = float(y[n])
      numerator, denominator = int(str(y[n]).replace('.','')), 10*(len(str(y[n]))-1-str(y[n]).index('.'))
    else: 
      numerator, denominator = int(y[n]), 1
    y[n] = f(numerator, denominator)

def Omit_Coefficient_1(y):
  for n in range(len(y)):
    if n!=0 and (y[n]==1 or y[n]==-1):
      info_term.append(str(y[n]).replace('1',''))
    else:
      info_term.append(str(y[n]))
      
def Add_x_exponent(y):
  for n in range(len(y)):
    info_term[n] = info_term[n] + 'x^' + str(n)

def Omit_degree_0_1(y):
  info_term[0] = info_term[0].replace('x^0','')
  if len(y)>1:
    info_term[1] = info_term[1].replace('^1','')
  
def Omit_Coefficient(y):
  for n in range(len(y)):
    if info_term[len(y)-1-n].find('0')==0:
      del info_term[len(y)-1-n]

def Print_Human_Tailored_Expansion (y):
  Omit_Coefficient_1(y)
  Add_x_exponent(y)
  Omit_degree_0_1(y)
  Omit_Coefficient(y)
  info_term.reverse()
  print('+'.join(info_term).replace('+-','-').replace('-',' - ').replace('+',' + ').lstrip(' '))
  del info_term[:]

def Convertible_to_decimal(denominator): 
  for prime_num in (2, 5): 
    while denominator % prime_num == 0: 
      denominator = denominator / prime_num 
  if denominator==1:
    return True 
  else : 
    return False 
# 분수를 prime_num로 나타낼 수 있나 판별
################################################################################################ 입력 단계
print('Calculus Too Easy!\n')
print('Type the coefficients for each term in descending order') 
print('(Separate by spacing)')
print('(No Terms: type a coefficient of zero)')
# 설명 출력

while True: # 반복
  c = 0  # 코드 진행 상태 : 입력 단계(0), 미분('1'), 부정적분('2'), 정적분('3')
  print('ㅡ' * 16) # 줄 치기
  
  y = input().split()
  y.reverse()
  # 함수의 각 항의 계수 입력 받기, 오름차순으로 정렬
  
  if Discrime_Rational_Num(y) == False: continue
  # 유리수가 아니면 초기화

  Change_Coefficient_into_Fracion(y)

  info_term = [] # 출력을 위해 변환시킨 항을 저장할 곳

  print('f(x) = ', end='') # 'f(x) =' 출력
  Print_Human_Tailored_Expansion (y)

  c = input('differential(1) | integral-indef(2), def(3): ')
  # 미분, 부정적분, 정적분 중 고르기
################################################################################################ 미분
  if c == 'differential' or c == '1' :
  # 미분을 골랐을 때

    if len(y) == 1: 
      print('0'); continue # 항이 하나면 0 출력

    for n in range(len(y)): # 각 항에서
      y[n] = n * y[n] # 새 계수 = 차수 x 계수
    del y[0] # 상수항 사라짐

    print("f'(x)= ", end='') # "f'(x)=" 출력
    Print_Human_Tailored_Expansion (y)
################################################################################################ 부정적분
  if c == 'integral-indef' or c == '2':
  # 부정적분을 골랐을 때

    if y[0] == 0 and len(y) == 1: # 항이 0 하나면 0 출력
      print('0'); continue

    for n in range(len(y)): # 각 항에서
      y[n] = y[n] / (n+1) # 새 계수 = 계수 / (차수+1)
    y.reverse()
    y.append('C') # 적분상수 C 추가
    y.reverse()

    print('F(x) = ', end='') # 'F(x) =' 출력
    Print_Human_Tailored_Expansion (y)
################################################################################################ 정적분
  if c == 'integral-def' or c == '3' :
  # 정적분을 골랐을 때
    x = input('renge [a, b] : ').split()
    # 범위 a, b 입력받기

    if len(x) != 2 :continue
    # 값을 2개를 받지 않았다면 초기화

    if Discrime_Rational_Num(x) == False: continue
    # 유리수가 아니면 초기화

    for n in range(2): 
      if '/' in x[n]:
        if '.' in x[n]:
          numerator, denominator = map(float, x[n].split('/'))
          digit_prime_num = 0
          for m in (numerator, denominator):
            if '.' in str(m):
              m = str(m).rstrip('0')
              digit_prime_num += len(str(m))-1-str(m).index('.')
          numerator, denominator = int(10**digit_prime_num*numerator), int(10**digit_prime_num*denominator)
        else:
          numerator, denominator = map(int, x[n].split('/'))
        x[n] = f(numerator, denominator)
      else:
        if '.' in x[n] : 
          x[n] = float(x[n])
        else: 
          x[n] = int(x[n])
    # a, b를 분수, prime_num, 정수꼴로 바꾸기 
    
    a, b = x[0], x[1]
    
    value = 0
    for n in range(len(y)):
      y[n] = y[n] / (n+1)
      y[n] = y[n] * (b**(n+1) - a**(n+1))
      value = value + y[n]
    # value = 각 항을 정적분하고 모두 더한 value

    print('[F(x)]{},{} = '.format(a, b), end='') # '[F(x)]a, b =' 출력 

    if Convertible_to_decimal(value.denominator) and value.denominator != 1: 
      print(float(value))
    else:
      print(value)
    # 값을, prime_num꼴로 바꿀 수 있으면 바꾸고, 출력
