import hcskr
import yaml
import os
import datetime
import random


def main():
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
                return

        data = hcskr.selfcheck(name, birth, region, school,
                               level, password)

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        sec = now.second
        rn = random.randint(1000, 9999)
        formated = f'{year}{month}{day}{hour}{minute}{sec}{rn}.log'

        with open(formated, "w", encoding='utf8') as f:
            f.write(f"isError = {data['error']}\n")
            f.write(f"Result = {data['code']}\n")
            f.write(f"Message = {data['message']}\n")
            f.write(f"Time = {data['regtime']}")
            f.close()


main()

hcskr.UpdateCheck
