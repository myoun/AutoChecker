import hcskr
import yaml
import os
import datetime
import random

class LogMaker:

  def __init__(self):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    sec = now.second
    rn = random.randint(0, 9)
    if (month < 10):
        month = f'0{month}'
    if (day < 10):
        day = f'0{day}'
    if (hour < 10):
        hour = f'0{hour}'
    if (sec < 10):
        sec = f'0{sec}'
    self.filename = f'{year}{month}{day}{hour}{minute}{sec}{rn}.log'
  
  def makeErrorLog(self,reason):
    print(reason)
    with open(self.filename,"w",encoding="utf8") as file:
      file.write("오류 여부 : O\n")
      file.write(f"이유 : {reason}")
      file.close()

  def makeLog(self, data,yml):
    try:
      with open(self.filename,"w",encoding="utf8") as f:
          f.write(f"에러 = {data['error']}\n")
          f.write(f"성공 여부 = {data['code']}\n")
          f.write(f"세부 결과 = {data['message']}\n")
          f.write(f"성공 시간 = {data['regtime']}")
          f.close()
    except KeyError:
      print(yml)
      print(data)
    print("로그를 확인해주세요")

class Util:

  def __init__(self):
    pass

  def checkFileExist(self,filename):
    return os.path.exists(filename)

  def writeBasicInfoYaml(self):
    with open("개인정보.yml", "w", encoding='utf8') as f:
      f.write("이름 : #이름\n")
      f.write("생년월일 : #예)010203\n")
      f.write("학교 종류 : #초등학교, 중학교, 고등학교\n")
      f.write("학교 이름 : #ㅇㅇ중학교\n")
      f.write("지역 : #예) 서울, 경기...\n")
      f.write("비밀번호 : #예) '1234'\n")
      f.close()

  def readYaml(self, filename):
    with open(filename,"r",encoding="utf8") as f:
      yamlfile = yaml.load(f,Loader=yaml.FullLoader)
      return yamlfile

def main():

  util = Util()
  logmaker = LogMaker()
  
  if (util.checkFileExist("개인정보.yml") == False):
    util.writeBasicInfoYaml()
    logmaker.makeErrorLog("개인정보.yml이 생성되었습니다.\n개인정보.yml에 개인정보를 적어주세요.")
    return

  yml = util.readYaml("개인정보.yml")
  name = yml["이름"]
  birth = yml["생년월일"]
  level = yml["학교 종류"]
  school = yml["학교 이름"]
  region = yml["지역"]
  password = str(yml["비밀번호"])
  
  elements = [name, birth, level, school, region, password]

  for element in elements:
    if (element == None):
      logmaker.makeErrorLog("개인정보.yml에 빈칸이 있습니다.\n빈칸을 모두 채우고 다시 실행해주세요.")
      return
  data = hcskr.selfcheck(name,birth,region,school,level,password)
  logmaker.makeLog(data,yml)

main()
input("프로그램이 끝났습니다.\nENTER키를 눌러 종료해주세요")

