# list = 식의 각 항의 계수들 (오름차순)

항정보 = []  # 출력을 위해 변환시킨 항을 저장할 곳

def 계수1_생략(list):
  for n in range(len(list)):
    if n!=0 and (list[n] == 1 or list[n] == -1):
      항정보.append(str(list[n]).replace('1',''))
    else:
      항정보.append(str(list[n]))
      
def x기호_지수_추가(list):
  for n in range(len(list)):
    항정보[n] = 항정보[n] + 'x^' + str(n)

def 제곱01_생략(list):
  항정보[0] = 항정보[0].replace('x^0','')
  if len(list)>1:
    항정보[1] = 항정보[1].replace('^1','')
  
def 계수0_생략(list):
  for n in range(len(list)):
    if 항정보[len(list)-1-n].find('0')==0:
      del 항정보[len(list)-1-n]

def Print_human_tailored_expansion(list): # 인간맞춤형 식 출력
  계수1_생략(list)
  x기호_지수_추가(list)
  제곱01_생략(list)
  계수0_생략(list)
  항정보.reverse()
  print('+'.join(항정보).replace('+-','-').replace('-',' - ').replace('+',' + ').lstrip(' '))
  del 항정보[:]