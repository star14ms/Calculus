from functions import * # functions 폴더에서 여러 함수 가져오기

print('Calculus Too Easy!\n')
print('Type the coefficients for each term in descending order') 
print('(Separate by spacing, Scope: rational Num)')
print('(No Terms: type a coefficient of zero)')

while True: # 반복
  print('ㅡ' * 16)
################################################################################ 입력 단계
  c = 0  # 코드 진행 상태 : 입력 단계(0), 미분('1'), 부정적분('2'), 정적분('3')
  
  y = input('Coefficients : ').split()
  y.reverse()
  # 함수의 각 항의 계수 입력 받기(list), 오름차순으로 정렬
  
  if isTrue_rational_num_list(y) == False: # list 원소들의 유리수 판별(y)
    print('Error: not rational-num!'); continue 
  # 유리수가 아니면 초기화

  y = Change_strs_fractions(y) # 각 항의 계수를 분수꼴로 전환

  print('f(x) = ', end='')
  print(Change_human_tailored_expression(y))

  c = input('differential(1) | integral-indef(2), def(3): ')
  # 미분, 부정적분, 정적분 중 고르기
################################################################################ 미분
  if c == 'differential' or c == '1': # 미분을 골랐을 때

    if len(y) == 1: 
      print('0'); continue # 항이 하나면 0 출력

    for n in range(len(y)): # 각 항에서
      y[n] = n * y[n] # 새 계수 = 차수 x 계수
    del y[0] # 상수항 사라짐

    print("f'(x)= ", end='')
    print(Change_human_tailored_expression(y))
################################################################################ 부정적분
  if c == 'integral-indef' or c == '2': # 부정적분을 골랐을 때

    if y[0] == 0 and len(y) == 1: # 항이 0 하나면 0 출력
      print('0'); continue

    for n in range(len(y)): # 각 항에서
      y[n] = y[n] / (n+1) # 새 계수 = 계수 / (차수+1)
    y.reverse()
    y.append('C') # 적분상수 C 추가
    y.reverse()

    print('F(x) = ', end='')
    print(Change_human_tailored_expression(y))
################################################################################ 정적분
  if c == 'integral-def' or c == '3': # 정적분을 골랐을 때

    x = input('renge [a, b] : ').split()
    # 범위 a, b 입력받기

    if len(x) != 2 : continue
    if isTrue_rational_num_list(x) == False:
      print('Error: not rational-num!'); continue
    # 값을 2개 받지 않았거나, 유리수가 아니면 초기화

    x = Change_strs_fractions(x) # a, b를 분수꼴로 바꾸기 
    
    a, b = x[0], x[1]
    
    value = 0
    for n in range(len(y)):
      y[n] = y[n] / (n+1)
      y[n] = y[n] * (b**(n+1) - a**(n+1))
      value = value + y[n]
    # value = 각 항을 정적분하고 모두 더한 value
    
    print('[F(x)]{},{} = '.format(a, b), end='')
    print(Change_to_decimal(value))
    # 값을, prime_num꼴로 바꿀 수 있으면 바꾸고, 출력
