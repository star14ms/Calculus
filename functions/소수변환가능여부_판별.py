def Convertible_to_decimal(denominator): # 소수변환가능(분모):
  for prime in (2, 5): 
    while denominator % prime == 0: 
      denominator = denominator / prime 
  if denominator == 1:
    return True 
  else : 
    return False 
    
# 분수를 소수로 나타낼 수 있나 판별