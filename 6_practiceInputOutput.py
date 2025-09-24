### 표준 입출력
# print("Python", "Java", sep=",", end="?") #sep는 사이에 들어가는 문자, end는 마지막에 들어가는 문자
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) #표준 출력
# print("Python", "Java", file=sys.stderr) #표준 에러

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust는 왼쪽 정렬, rjust는 오른쪽 정렬

# 은행 대기 순번표
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) #zfill은 0으로 채우기, 3은 총 자리수

# answer = input("아무 값이나 입력하세요 : ") #input은 사용자 입력을 받는 함수, 항상 문자열로 반환
# print("입력하신 값은 " + answer + "입니다.")


###다양한 출력 포맷
# # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<10}".format(500))
# # 3자리 마다 ,를 찍어주기
# print ("{0:,}".format(10000000))
# # 3자리 마다 ,를 찍어주기, +-부호도 붙이기
# print("{0:+,}".format(10000000))
# print("{0:+,}".format(-10000000))
# # 3자리 마다 ,를 찍어주기, +-부호도 붙이기, 자릿수 확보하기
# print("{0:^<+30,}".format(10000000000000).rjust(20))
# print("{0:+,}".format(-10000000).rjust(20))
# # 소수점 출력
# print("{0:.3f}".format(5/3)) #소수점 4째 자리에서 반올림하여 3째 자리까지 표시


### 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") #쓰기 모드, utf8 인코딩, 여기서 score_file은 파일 객체
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") #추가 모드
# score_file.write("과학 : 85")
# score_file.write("\n코딩: 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #읽기 모드
# print(score_file.read()) #전체 읽기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #줄별 읽기, 한 줄 읽은후 커서는 다음줄
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

##파일이 몇 줄인지 모를 때 무한루프+종류 구문을 활용한 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

##리스트 형태로 저장
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

### pickle : 파일 읽기, 쓰기
import pickle
# profile_file = open("profile.pickle", "wb") #wb는 바이너리 쓰기 모드
# profile = {"이름":"Dan", "나이":32, "취미":["러닝", "OTT시청", "코딩", "독서"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb") #rb는 바이너리 읽기 모드
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

### with : 파일을 자동으로 닫아줌
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

## 파일 쓰기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부중입니다.")

# 파일 읽기
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

### Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# 1. X 주차 주간보고
# 2. 부서 :
# 3. 이름 :
# 4. 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만들기.

for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf-8") as report_file:
        report_file.write("1. {0} 주차 주간보고\n2. 부서 : \n3. 이름 : \n4. 업무 요약 : ".format(i))
        