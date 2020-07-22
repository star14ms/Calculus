from fractions import Fraction as f

print('미적분 너무 쉬워!\n')
print('각 항의 계수를 내림차순으로 쓰시오\n(중간에 없는 항도 0을 써서 표시)')
while True:
  print('ㅡ' * 16)
  y = input().split()

  if y == []: continue
  숫자 = True
  for i in range(len(y)):
    if y[i].isalpha(): 숫자 = False
  if 숫자 == False: continue

  for n in range(len(y)): 
    if '/' in y[len(y)-1-n]:
      분자, 분모 = map(int, y[len(y)-1-n].split('/'))
    else:
      분자, 분모 = int(y[len(y)-1-n]), 1
    y[len(y)-1-n] = f(분자, 분모)

  print('f(x) =', end='') 
  for n in range(len(y)):
    if n == len(y)-1:
      항 = str(y[n])
    elif n == len(y)-2:
      항 = str(y[n]) + 'x'
    else :
      항 = str(y[n]) + 'x^' + str(len(y)-1-n)

    항 = 항.replace('-',' - ').replace('1x','x').replace('1x','11x')
    if n == 0 : 
        항 = ' ' + 항
    elif (not '-' in 항):
      항 = ' + ' + 항

    항분리 = 항.split('x')
    if n == 0 :
      if 항분리[0] == ' 0': continue
    elif 항분리[0] == ' + 0': continue
    if n != len(y)-1: 
      print(항, end='')
    else:
      print(항)

  c = input('미분(1) | 부정적분(2) | 정적분(3) : ')

  if c == '미분' or c == '1' :
    
    print("f'(x)=", end='')
    for n in range(len(y)):
      y[n] = (len(y)-1-n) * y[n]
      
      if y[n] == 0: 
        if len(y) == 1: 
          print(' 0'); continue
        else : 
          continue

      if n == len(y)-2:
        y[n] = str(y[n])
      elif n == len(y)-3:
        y[n] = str(y[n]) + 'x'
      else :
        y[n] = str(y[n]) + 'x^' + str(len(y)-2-n)

      y[n] = y[n].replace('-',' - ').replace('1x','x').replace('1x','11x')
      if n == 0 : 
        y[n] = ' ' + y[n]
      elif (not '-' in y[n]):
        y[n] = ' + ' + y[n]

      if n != len(y)-2:
        print(y[n], end='')
      else: 
        print(y[n])

  elif c == '부정적분' or c == '2':

    print("F(x) =", end='')
    for n in range(len(y)):
      y[n] = y[n] / (len(y)-n)

      if n == len(y)-1:
        y[n] = str(y[n]) + 'x'
      else :
        y[n] = str(y[n]) + 'x^' + str(len(y)-n)

      y[n] = y[n].replace('-',' - ').replace('1x','x').replace('1x','11x')
      if n == 0 : 
        y[n] = ' ' + y[n]
      elif (not '-' in y[n]):
        y[n] = ' + ' + y[n]

      if n != len(y)-1:
        print(y[n], end='')
      else: 
        print(y[n],'+ C')

  elif c == '정적분' or c == '3' :

    x = input('범위 [a, b] : ').split()
    if len(x) != 2 :continue
    elif x[0].isalpha() | x[1].isalpha():continue

    for n in range(2): 
      if '/' in x[n]:
        분자, 분모 = map(int, x[n].split('/'))
        x[n] = f(분자, 분모)
      else:
        if '.' in x[n] : 
          x[n] = float(x[n])
        else: 
          x[n] = int(x[n])

    print('[F(x)]{},{} = '.format(x[0], x[1]), end='')
    값 = 0
    for n in range(len(y)):
      y[n] = y[n] / (len(y)-n)
      y[n] = y[n] * (x[1]**(len(y)-n) - x[0]**(len(y)-n))
      값 = 값 + y[n]
    
    def 소수변환가능(n): 
      for i in (2, 5): 
        while n%i == 0: 
          n=int(n/i) 
      if n==1: 
        return True 
      else : 
        return False 

    if 소수변환가능(값.denominator) & 값.denominator!=1 : 
      print(float(값))
    else :
      print(값)