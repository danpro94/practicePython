# # 문자열 처리
# sentence = '나는 남자입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 남자이고,
# 파이썬은 쉬워요.
# """
# print(sentence3)

# # 슬라이싱
# jumin="940702-1234567"
# print("성별: " + jumin[7])
# print("연: " + jumin[0:2]) #0부터 2직전까지 가져옴
# print("월: " + jumin[2:4])
# print("일: " + jumin[4:6])
# print("생년월일: " + jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리: " + jumin[7:])
# print("뒤 7자리 (뒤에부터): " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지 (참고사항: 맨 뒤는'-1' 이다.)

# #문자열 처리함수
# python="Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) #0번째 문자가 대문자인가? 참/거짓 반환
# print(len(python)) #문자열의 총길이 반환
# print(python.replace("Python", "CloudNative")) #문자열 포함 내용을 대체
# index = python.index("n") #첫번째 n의 위치값 반환
# print(index)
# index = python.index("n", index + 1) #두번째 n의 위치값 반환
# print(index) 
# print(python.find("Java")) #문자열에 값이 없으면 find는 -1, index는 error 반환.
# print(python.count("n")) #문자열에서 n이 몇개 있는지

# #문자열 포맷
# #방법1
# print("나는 %d살입니다." % 32) #정수
# print("나는 %s을 좋아해요." % "파이썬") #문자열
# print("Apple 은 %c로 시작해요." % "A") #문자
# print("나는 %s년생이고, %s색을 좋아합니다." % ("94", "초록"))
# #방법2.format
# print("나는 {}살입니다.".format(32))
# print("나는 {0}년생이고, {1}색을 좋아합니다.".format("94", "초록"))
# print("나는 {1}색과 {0}색을 좋아합니다.".format("파랑", "초록"))
# #방법3 .format 지정
# print("나는 {birth}년생이고, {color}색을 좋아합니다.".format(birth=1994, color="파랑"))
# #방법4 f-string
# age = 32
# color = "초록"
# print(f"나는 {age}살이며, {color}을 좋아합니다.")

# #탈출 문자
# print("백문이 불여일견\n백견이 불여일타") #문장내에서 줄바꿈
# print("저는 \"윤두용\" 입니다.")
# print("역슬래시 하나 \\ 를 쓰기 위해서는 역슬래시 두개를 쓰고 \n 두개 \\\ 를 쓰기위해서는 세개 쓰자.")
# print("Green Apple\rGoood") # \r : 커서를 맨 앞으로 이동
# print("Redd\bApple") # \b : 백스페이스
# print("Green\tApple") # \t : 탭

#Quiz 사이트별로 비밀번호를 만들어주는 프로그램
#내 답변
site = "http://naver.com"
passwordrule1 = site[7:]
passwordrule2 = passwordrule1.replace(".com", "")
pr3name=passwordrule2[:3]
pr3count = len(passwordrule2)
pr3ecount=passwordrule2.count("e")

print(f"생성된 비밀번호: {pr3name}{pr3count}{pr3ecount}!")

#강사 답변
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(f"{url}의 비밀번호는 {password} 입니다.")