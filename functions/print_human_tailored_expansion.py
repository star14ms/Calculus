# terms = 식의 각 항의 계수들 (오름차순, list)

항정보 = []  # 출력을 위해 변환시킨 항을 저장할 곳

def 계수1_생략(terms):
  for n in range(len(terms)):
    if n!=0 and (terms[n] == 1 or terms[n] == -1):
      항정보.append(str(terms[n]).replace('1',''))
    else:
      항정보.append(str(terms[n]))
      
def x기호_지수_추가(terms):
  for n in range(len(terms)):
    항정보[n] = 항정보[n] + 'x^' + str(n)

def 제곱01_생략(terms):
  항정보[0] = 항정보[0].replace('x^0','')
  if len(terms)>1:
    항정보[1] = 항정보[1].replace('^1','')
  
def 계수0_생략(terms):
  for n in range(len(terms)):
    if 항정보[len(terms)-1-n].find('0')==0:
      del 항정보[len(terms)-1-n]

def Print_human_tailored_expansion(terms): # 인간맞춤형 식 출력
  계수1_생략(terms)
  x기호_지수_추가(terms)
  제곱01_생략(terms)
  계수0_생략(terms)
  항정보.reverse()
  print('+'.join(항정보).replace('+-','-').replace('-',' - ').replace('+',' + ').lstrip(' '))
  del 항정보[:]
