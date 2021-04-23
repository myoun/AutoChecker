import hcskr
import yaml
import os
import datetime
import random

def errorLog(name,reason):
    with open(name,"w",encoding='utf8') as f:
        f.write("에러 : True\n")
        f.write(f"이유 : {reason}\n")
        f.close()


def main():

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    sec = now.second
    rn = random.randint(1000, 10000)
    if (month < 10):
        month = f'0{month}'
    if (day < 10):
        day = f'0{day}'
    if (hour < 10):
        hour = f'0{hour}'
    if (sec < 10):
        sec = f'0{sec}'
    formated = f'{year}{month}{day}{hour}{minute}{sec}{rn}.log'

    
    if (os.path.exists("개인정보.yml") == False):
        with open("개인정보.yml", "w", encoding='utf8') as f:
            f.writelines("이름 : #이름\n")
            f.writelines("생년월일 : #예)010203\n")
            f.writelines("학교 종류 : #초등학교, 중학교, 고등학교\n")
            f.writelines("학교 이름 : #ㅇㅇ중학교\n")
            f.writelines("지역 : #예) 서울, 경기...\n")
            f.writelines("비밀번호 : #예) 1234\n")
            f.close()
            print("개인정보.yml 파일을 수정해주세요")
            input("프로그램을 종료하려면 ENTER 키를 눌러주세요.")
            errorLog(formated,'''
개인정보.yml이 생성되었습니다.
개인정보.yml에 정보를 입력하고, 다시 실행시켜주세요.
''')
            return

    with open("개인정보.yml", "r", encoding='utf8') as f:
        yamlfile = yaml.load(f, Loader=yaml.FullLoader)
        print(yamlfile)

        name = yamlfile["이름"]
        birth = yamlfile["생년월일"]
        level = yamlfile["학교 종류"]
        school = yamlfile["학교 이름"]
        region = yamlfile["지역"]
        password = str(yamlfile["비밀번호"])

        lists = [name, birth, level, school, region, password]

        for param in lists:
            if (param == None):
                input("개인정보.yml에 빈칸이 있습니다.\n프로그램을 종료하려면 ENTER 키를 눌러주세요")
                errorLog(formated,'''
개인정보.yml에 빈칸이 있습니다.
빈칸을 모두 채우고 다시 실행시켜주세요.
''')
                return

        data = hcskr.selfcheck(name, birth, region, school,
                               level, password)



        with open(formated, "w", encoding='utf8') as f:
            f.write(f"에러 = {data['error']}\n")
            f.write(f"성공 여부 = {data['code']}\n")
            f.write(f"세부 결과 = {data['message']}\n")
            f.write(f"성공 시간 = {data['regtime']}")
            f.close()
        input("ENTER를 눌러 종료하기")


main()


