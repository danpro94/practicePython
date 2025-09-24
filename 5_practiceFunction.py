# ##함수의 정의와 호출
# def open_account():
#     print("신규 계좌 생성 완료")
# open_account()


##전달값과 반환값

#입금
# def deposit(balance, money):
#     print("입금이 완료됐습니다. 잔액은 {0}원 입니다.".format(balance+money))
#     return balance+money

# #출금
# def withdraw(balance, money):
#     if balance > money:
#         print("출금이 완료됐습니다. 잔액은 {0}원 입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("잔액이 부족합니다. 현재 통장 잔고는 {0}원 입니다".format(balance))
#         return balance

# #밤출금
# def withdraw_night(balance, money):
#     commission = 1000 #수수료
#     return commission, balance - money - commission

# balance = 0 #잔액
# balance = deposit(balance, 7600000000)
# # balance = withdraw(balance, 10000)

# commission, balance = withdraw_night(balance, 1000)
# print("수수료는 {0} 원 이며, 잔액은 {1} 원 입니다".format(commission, balance))


## 기본값
# def profile(name, age=32, main_lang="Python"):
#     print(f"이름: {name} 나이: {age} 주사용 언어: {main_lang}")

# profile("홍길동")
# profile("최홍만")


##키워드 값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="Kim", main_lang="Python", age="33")
# profile(main_lang="C", name="Yoon", age="29")


#가변인자
# def profile(name, age, *language):
#     print("이름: {0} \t나이: {1} \t".format(name, age), end =" ")
#     for lang in language:
#         print(lang, end="")
#     print()

# profile("Lee", 24, "C", "C++", "Java", "Python", "Go", "React") #더 필요하면 함수 일일히 수정 안하도록
# profile("Park", 22, "Go", "Swift") #"" 이것 안하도록


## 지역변수와 전역변수
# gun = 33

# def checkpoint(soldiers):
#     global gun #전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[부대 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[부대 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 3)
# print("남은 총 : {0}".format(gun))

##Quiz) 표준 체중을 구하는 프로그램
# *표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         *함수명 : std_weight
#         *전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# 출력예제 : 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height, gender):
#     if gender == "man":
#        return height*height*22
#     else:
#         return height*height*21

# height=172
# gender="man"
# weight = round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
