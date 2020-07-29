# 본문 시작인 103줄부터 읽는 것을 추천 (102줄까지의 def구문은 모두 접었다가 하나씩 피면서 보기)

from fractions import Fraction as f
# to add fractional form
################################################################################################ 함수 정의 및 가져오기
def rational_discrimination(y):
  if y == []: return False # 입력 없음
  
  for term in y:
    conversion = str.maketrans('1234567890-/.', 'ooooooooooooo')
    for m in range(len(term)):
      rational_material = term[m].translate(conversion)
      if not 'o' in rational_material: return False
  
    if '/' in term:
      if term.count('/') != 1: return False
      if term.index('/') == 0 | term.index('/') == len(term)-1: return False
      numerator, denominator = map(float, term.split('/'))
      if denominator == 0: return False # denominator = 0
    
    if '.' in term:
      if '/' in term:
        numerator, denominator = term.split('/')
        if numerator.count('.') == 2 | denominator.count('.') == 2: return False
      else:  
        if term.count('.') != 1: return False
        if term.index('.') == 0 | term.index('.') == len(term)-1: return False      
  return True
# 입력이 없거나, denominator가 0일 때도 유리수 = False 

def Replace_Coefficients_with_Fractions(n):
  if '/' in y[n] and '.' in y[n]: # y[n] : y의 n번째 항의 계수
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
    y[n] = float(y[n])
    numerator, denominator = int(str(y[n]).replace('.','')), 10*(len(str(y[n]))-1-str(y[n]).index('.'))
  else: 
    numerator, denominator = int(y[n]), 1   

  y[n] = f(numerator, denominator)
# 항의 계수를 분수꼴로 바꾸기 

def Omit_1_Coefficient(n):
  if y[n] == 1 or y[n] == -1:
    if (c == 0 and n != len(y)-1) | (c == '1' and n != len(y)-2) | (c == '2'):
      z[n] = str(y[n]).replace('1','')
    else:
      z[n] = str(y[n])
  else:
    z[n] = str(y[n])
# 항의 계수가 1 or -1이면 1생략 (상수항 제외)

def Add_Sign_Space(n):
  z[n] = z[n].replace('-',' - ')
  if n == 0 : 
     z[n] = ' ' + z[n]
  elif (not '-' in z[n]):
     z[n] = ' + ' + z[n]
# 항의 계수에 부호, 공백 추가

def Add_VariableSymbols_Exponent(n):
  if (c==0 and n==len(y)-2) | (c=='1' and n==len(y)-3) | (c=='2' and n==len(y)-1):
    z[n] = z[n] + 'x'
  else:
    if c==0 and n!=len(y)-1:
      z[n] = z[n] + 'x^' + str(degree)
    if c=='1' and n!=len(y)-2:
      z[n] = z[n] + 'x^' + str(degree-1)
    if c=='2':
      z[n] = z[n] + 'x^' + str(degree+1)
# 계수에 변수기호, 지수 추가

def Add_Terms_Information(n):
  Omit_1_Coefficient(n)
  Add_Sign_Space(n)
  Add_VariableSymbols_Exponent(n)
# 바로 위에 있는 세개의 함수를 한줄로

def Print_Out(n):
  if (c == 0 and n != len(y)-1) | (c == '1' and n != len(y)-2) | (c == '2' and n != len(y)-1):
    print(z[n], end='')
  elif c == '2': 
    print(z[n],'+ C')
  else:
    print(z[n])
# 항들 조합해서 Print_Out

def Convertible_to_decimal(denominator): 
  for 소수 in (2, 5): 
    while denominator % 소수 == 0: 
      denominator = denominator / 소수 
  if denominator == 1:
    return True 
  else : 
    return False 
# 분수를 소수로 나타낼 수 있나 판별
################################################################################################ 입력 단계
print('Calculus Too Easy!\n')
print('Type the coefficients for each term in descending order') 
print('(Separate by spacing)')
print('(No Terms: type a coefficient of zero)')
# 설명 Print_Out

while True: # 반복
  c = 0  # 코드 진행 상태 : 입력 단계(0), 미분('1'), 부정적분('2'), 정적분('3')
  print('ㅡ' * 16) # 줄 치기
  
  y = input().split() 
  # 함수의 각 항의 계수 입력 받기

  if rational_discrimination(y) == False: continue
  # 유리수가 아니면 초기화

  z = {} # output을 위해 변환시킨 항을 저장할 곳

  print('f(x) =', end='') # 'f(x) =' Print_Out

  for n in range(len(y)): # 각 항에서
    Replace_Coefficients_with_Fractions(n)
    if y[n] == 0: # 계수가 0이면 생략
      if len(y) == 1:
        print(' 0')
      elif n == len(y)-1:
        print()
    else: # 아니면 term 정보 추가하여 Print_Out
      degree = len(y)-1-n # 내림차순
      Add_Terms_Information(n)
      Print_Out(n)

  c = input('differential(1) | integral-indef(2), def(3): ')
  # 미분, 부정적분, 정적분 중 고르기
################################################################################################ 미분
  if c == 'differential' or c == '1' :
  # 미분을 골랐을 때
    print("f'(x)=", end='') # "f'(x)=" Print_Out

    if len(y) == 1: 
      print(' 0'); continue
    # 항이 하나면 0 Print_Out

    for n in range(len(y)-1): # 각 항에서 (상수항 빼고)
      if y[n] == 0: # 계수가 0이면 생략
        if n == len(y)-2: 
          print()
      else: # 아니면 미분하여 Print_Out
        degree = len(y)-1-n
        y[n] = degree * y[n]
        Add_Terms_Information(n)
        Print_Out(n)
################################################################################################ 부정적분
  if c == 'integral-indef' or c == '2':
  # 부정적분을 골랐을 때
    print('F(x) =', end='') # 'F(x) =' Print_Out

    for n in range(len(y)): # 각 항에서
      if y[n] == 0: # 계수가 0이면 생략
        if len(y) == 1:
          print(' 0')
        elif n != len(y)-1:
          print()
      else: # 아니면 적분하여 Print_Out 
        degree = len(y)-1-n
        y[n] = y[n] / (degree+1)
        Add_Terms_Information(n)
        Print_Out(n) # 적분상수 C도 추가
################################################################################################ 정적분
  if c == 'integral-def' or c == '3' :
  # 정적분을 골랐을 때
    x = input('range [a, b] : ').split()
    # 범위 a, b 입력받기

    if len(x) != 2 :continue
    # 값을 2개를 받지 않았다면 초기화

    if rational_discrimination(x) == False: continue
    # 유리수가 아니면 초기화

    for n in range(2): 
      if '/' in x[n]:
        if '.' in str(y[n]):
          numerator, denominator = map(float, y[n].split('/'))
          decimal_digit = 0
          for m in (numerator, denominator):
              o = str(m).split('.')
              if o[1] != 0:
                decimal_digit += len(str(m))-1-str(m).index('.')
          numerator, denominator = int(10**decimal_digit*numerator), int(10**decimal_digit*denominator)
        else:
          numerator, denominator = map(int, x[n].split('/'))
        x[n] = f(numerator, denominator)
      else:
        if '.' in x[n] : 
          x[n] = float(x[n])
        else: 
          x[n] = int(x[n])
    # a, b를 분수, 소수, 정수꼴로 바꾸기 
    
    a, b = x[0], x[1]

    print('[F(x)]{},{} = '.format(a, b), end='') # '[F(x)]a, b =' Print_Out 

    value = 0
    for n in range(len(y)):
      degree = len(y)-1-n
      y[n] = y[n] / (degree+1)
      y[n] = y[n] * (b**(degree+1) - a**(degree+1))
      value = value + y[n]
    # value = 각 항을 정적분하고 모두 더한 value

    if Convertible_to_decimal(value.denominator) and value.denominator != 1: 
      print(float(value))
    else:
      print(value)
    # 값을, 소수꼴로 바꿀 수 있으면 바꾸고, Print_Out
