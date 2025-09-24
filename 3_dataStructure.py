#리스트 []

# #지하철 칸별로 10, 20, 30명
# subway = [10, 20, 30]
# print(subway)

# #0번칸 / 1번칸/ 2번칸
# subway = ["승객1", "승객2", "승객3"]
# print(subway)

# print(subway.index("승객2"))
# subway.append("new승객")
# print(subway)

# subway.insert(1, "new승객1-1")
# print(subway)

# #한명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# #같은 이름 사람 확인
# subway.append("승객3")
# print(subway)
# print(subway.count("승객3"))

# #정렬
# num_list = [2, 3, 4, 1, 5]
# num_list.sort()
# print(num_list)

# #순서 뒤집기
# num_list.reverse()
# print(num_list)

# #모두 지우기(=빈 리스트 만들기)
# num_list.clear()
# print(num_list)

# #다양한 자료형과 함께 사용
# anylist =["Dan", 32, True]
# newnum_list =[1,2,3,4,5]
# print(anylist)

# #리스트 확장
# anylist.extend(newnum_list)
# print(anylist)


# #사전
# game = {3:"3번", 100:"100번", 456:"성기훈"}
# print(game[3]) #값이없는 경우 오류 발생후 프로그램을 종료 시킴 
# print(game[100])
# print(game.get(456)) #값이없는 경우 None를 출력

# print(3 in game) # True
# print(5 in game) # False

# #새로운 참가자
# game["A-1"] = "이병헌"
# game[100] = "임시완"
# print(game)

# #탈락자
# del game[456]
# print(game)

# #key들만 출력
# print(game.keys())
# #Value들만 출력 
# print(game.values())
# #Key, Value 쌍으로 출력
# print(game.items())
# #게임 종료
# game.clear()
# print(game)


# #튜플
# menu = ("돈까스", "떡볶이")
# print(menu[0])
# print(menu[1])

# (name, age, hobby) = ("Dan", 32, "Running")
# print(name, age, hobby)


# #세트
# my_set = {1,2,3,3,3}
# print(my_set) #중복된 3은 출력이 되지 않음

# java = {"가", "나", "다"}
# python = set(["가", "라"])
# #교집합
# print(java & python)
# print(java.intersection(python))
# #합집합
# print(java | python)
# print(java.union(python))
# #차집합
# print(java-python)
# print(java.difference(python))
# #python 할 줄 아는 사람 늘어남
# python.add("다")
# print(python)
# #java 까먹음
# java.remove("나")
# print(java)


# #자료구조의 변경
# menu  = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


from random import *
#Quiz) 학교에서 파이썬 코딩 대회 주최
# 댓글 이벤트 진행
# 댓글 작성자 중 추첨을 통해 1명 치킨, 3명은 커피 쿠폰
# 추첨 프로그램 작성 (댓글 작성자 20명 제한, 아이디는 1~20, 무작위 추첨, 중복 불가)

users = range(1,21)
users = (list(users))
shuffle(users)

winners = sample(users, 4)

print(f''' 
        -- 당첨자 발표 --
            치킨 당첨자: {winners[0]} 
            커피 당첨자: {winners[1:]}
        -- 축하합니다. --
            ''')


# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))