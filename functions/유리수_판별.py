def Discrime_rational_num(list): # 유리수 판별
  if list == []: return False # 입력 없음
  
  for 항 in list:
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