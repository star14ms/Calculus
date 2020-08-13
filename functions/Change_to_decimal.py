from fractions import Fraction as f # 분수꼴 추가

def Change_to_decimal(num): 
  if str(type(num)) == "<class 'fractions.Fraction'>": # fraction : 분수
    quotient = num.denominator # quotient : 몫, denominator : 분모
  else: 
    return num # 그대로 출력

  for prime in (2, 5): # prime( number) : 소수
    while quotient % prime == 0: 
      quotient = quotient / prime 
  if quotient == 1 and num.denominator != 1: # 분모의 약수가 2 or 5 뿐이면
    return float(num) # 소수로 변환
  else : 
    return num # 그대로 출력

# 분수만 소수로 변환가능하면 변환
# change from fraction to decimal