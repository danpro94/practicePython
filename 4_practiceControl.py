## if 조건 제어문
# weather = "미세먼지"
# if weather == "rainy":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없습니다.")

# tem = int(input("기온은 어때요?"))  # 사용자에게 입력을 받음
# if tem >= 36:
#     print("너무 더워요. 나가지 마세요")
# elif 30 >= tem and tem >= 10:
#     print("괜찮은 날씨에요")
# elif tem < 9:
#     print("너무 추워요. 나가지 마세요")
# else:
#     print("기온을 모르시나요?")


## for 반복 제어문
# for waiting in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting))

# for waiting in range(5): # 0, 1, 2, 3, 4
#     print("대기번호 : {0}".format(waiting))

# for waiting in range(1, 7): # 1, 2, 3, 4, 5, 6
#     print("대기번호 : {0}".format(waiting))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# ## while 반복 제어문
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.") 

#반복문 무한 루프
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")


## continue, break
# absent = [2, 5] # 결석
# no_book = [7] # 책을 안가져온 학생
# for student in range(1, 11): # 1 ~ 10까지의 출석번호
#     if student in absent:
#         continue #밑에 있는 코드 실행하지 않고 다음 반복으로 넘어감
#     elif student in no_book: # 책을 안가져온 학생
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))


# ## 한 줄 for문
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i + 100 for i in students] # 학생들 번호 100번씩 올리기
# print(students)

# # 학생 이름을 길이로 변환
# students = ["아이언맨", "토르", "그루트"]
# students = [len(i) for i in students]
# print (students)

# # 학생 이름을 대문자로 변환
# students = ["ironman", "thor", "groot"]
# students = [i.upper() for i in students]
# print(students)


## 퀴즈
# 1. 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
# 2. 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 합니다.

#출력문 예제
#[O] 1번째 손님 (소요시간 : 15분)
#[] 2번째 손님 (소요시간 : 50분)
#[O] 3번째 손님 (소요시간 : 5분)

#총 탑승 승객 : 2분

from random import *

cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50 이라는 승객
    time = randrange(5, 51) # 5 ~ 50분 소요 시간
    if 5 <= time <= 15: # 매칭 성공한 경우
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1 # 총 탑승 승객 수 증가 처리
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0}명".format(cnt))
