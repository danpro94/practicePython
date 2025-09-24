### glob: 경로 내의 폴더나 파일 목록 조회
# import glob
# print(glob.glob("*.py")) #확장자가 py인 파일 도출


### 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) #현재 디렉토리

# forder = "testsample_dir"

# if os.path.exists(forder):
#     print("폴더가 이미 존재합니다.")
#     os.rmdir(forder) #폴더 삭제
#     print("폴더가 삭제되었습니다.")
# else:
#     os.makedirs(forder) #폴더 생성
# print(os.listdir())


### time : 시간 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%M-%D %H:%M:%S")) #연-월-일 시:분:초를 출력

## import datetime
# #print("오늘 날짜: ", datetime.date.today())

# timedelta: 두 날짜 사이 간격

# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("100일후는", today + td)