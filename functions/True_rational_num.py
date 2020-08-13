def True_rational_num(string): # 유리수 판별
  if string == '': return False # 입력 없음

  변환 = str.maketrans('1234567890-/.', 'ooooooooooooo')
  for element in string:
    유리수_재료 = element.translate(변환)
    if not 'o' in 유리수_재료: return False

  if '/' in string:
    if string.count('/')!=1: return False
    if '.' in string:
      분자, 분모 = string.split('/')
      if 분자.count('.')>1 or 분모.count('.')>1: return False
    else:
      if string.index('/')==0 | string.index('/') == len(string)-1: return False
      분자, 분모 = map(float, string.split('/'))
      if 분모 == 0: return False # 분모 = 0
  elif '.' in string:
    if string.count('.')!=1: return False
    if string.index('.')==0 or string.index('.') == len(string)-1: return False  
  return True
# 입력이 없거나, 분모가 0일 때도 유리수 = False 

# 응용 1
def True_rational_num_list(list): # list의 각 원소에서 유리수 판별
  if list == []: return False # 입력 없음

  for string in list:
    if True_rational_num(string) == False: return False
  return True