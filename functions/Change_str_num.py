# change_a_b() : change from a to b

from fractions import Fraction as f # 분수꼴 추가
################################################################

def Change_str_num(string): # 문자열을 형태별 수로 전환
  if '/' in string:
    if '.' in string:
      numerator, denominator = map(float, string.split('/'))
      decimal_digit = 0
      for m in (numerator, denominator):
        if '.' in str(m):
          m = str(m).rstrip('0')
          decimal_digit += len(str(m))-1-str(m).index('.')
      numerator, denominator = int(10**decimal_digit*numerator), int(10**decimal_digit*denominator)
    else:
      numerator, denominator = map(int, string.split('/'))
    return f(numerator, denominator)
  else:
    if '.' in string: 
      return float(string)
    else: 
      return int(string)
      
# +응용1
def Change_strs_nums(list): # 문자열 원소들을 형태별 수로 전환
  list2 = []
  for string in list:
    list2.append(Change_str_num(string))
  return list2

################################################################

def Change_str_fraction(string): # 문자열을 분수꼴로 전환
  if '/' in string and '.' in string:
    numerator, denominator = map(float, string.split('/'))
    decimal_digit = 0
    for m in (numerator, denominator):
      if '.' in str(m):
        m = str(m).rstrip('0')
        decimal_digit += len(m)-1-m.index('.')
    numerator, denominator = int(10**decimal_digit*numerator), int(10**decimal_digit*denominator)
  elif '/' in string:
    numerator, denominator = map(int, string.split('/'))
  elif '.' in string:
    numerator, denominator = int(string.replace('.','')), 10**(len(string)-1-string.index('.'))
  else: 
    numerator, denominator = int(string), 1
  return f(numerator, denominator)

# 응용1
def Change_strs_fractions(list): # 문자열 원소들을 각각 분수꼴로 전환
  list2 = []
  for string in list:
    list2.append(Change_str_fraction(string))
  return list2