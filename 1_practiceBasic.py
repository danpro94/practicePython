from datetime import datetime
from math import *
from random import *

#숫자 자료형
print(1)
print(-9999)
print(10000)
print(3.141592)
print(3*3)
print(3*(10/2))
#문자열 자료형
print('딴')
print("딴딴")
print("ㅋㅋㅋ")
print("ㅋ"*10)
#boolean(참 / 거짓) 자료형
print(1 < 2)
print(10 > 100)
print(True)
print(False)
print(not True)
print(not False)
print(not 1 < 2)
#나를 소개합니다.
today_y = datetime.now().year
print(today_y)
jobdescription = "SRE/DevOps Engineer"
name="Dan Yoon"
birth=1994
age=today_y-birth
future='Very Nice'
print("저는" + jobdescription + "로 성장중인 " + name + " 입니다")
'''print("저는" + str(age) +"살 " + jobdescription + "(으)로써 효율적이고, 기본기기 탄탄한 성장을 원합니다.")'''
print(f"저는 {age}살 {jobdescription}(으)로써 효율적이고, 기본기기 탄탄한 성장을 원합니다.")
print(jobdescription + "은(는) 향후 전망이 좋나요? " + future)
#Quiz 변수를 이용하여 다음 문장을 출력하시오
station="신도림"
print(station+"행 열차가 들어오고 있습니다.")
#숫자 처리 함수
print(abs(-5)) #절대값
print(pow(4, 2)) #4의 2승)
print(max(2, 99)) #최대값 
print(min(3, 4)) #최소값
print(round(3.14)) #반올림
print(round(4.51)) #반올림
#math 라이브러리 이용
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4
#Random 라이브러리 이용 랜덤함수
print(random()) #0.0~1.0 미만의 임의의 값
print(random() * 10) #0.0~10.0 미만의 임의의 값
print(int(random() * 10)) #1~10 미만의 임의의 값
print(randrange(1,46)) #1~46 미만의 임의의 값 생성
print(randint(1, 45)) #1~45 이하의 임의의 값 생성
#Quiz 나는 최근 스터디 모임을 새로 만들었습니다.
#월 4회 스터디를 하는데 3번은 온라인 모임, 1번은 오프라인으로 하기로 했습니다.
#아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.


offline=randrange(4, 29)
print("오프라인 스터디 모임 날짜는 매월 " + str(offline) + "일로 선정되었습니다.")