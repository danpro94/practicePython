###예외처리
## 나누기 계산기 만들기
# try:
#     print("나누기 계산기")
#     num1 = int(input("첫번째 숫자를 입력하세요: "))
#     num2 = int(input("두번째 숫자를 입력하세요: "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러가 발생했습니다. 잘못된 값('ValueError')을 입력했어요!")
# except ZeroDivisionError as err:
#     print("에러가 발생했습니다. 정수는 0으로({0}) 나눌수 없습니다!".format(err))

##에러1
# try:
#     print("나누기 계산기")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요: ")))
#     nums.append(int(input("두번째 숫자를 입력하세요: ")))
#     nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러가 발생했습니다. 잘못된 값('ValueError')을 입력했어요!")
# except ZeroDivisionError as err:
#     print("에러가 발생했습니다. 정수는 0으로({0}) 나눌수 없습니다!".format(err))
# except Exception as err:
#     print("알 수 없는 에러가 발생했습니다.")
#     print(err)
# except:
#     print("알 수 없는 에러가 발생했습니다.")


###에러 발생 시키기
## 한자리 숫자용 나누기 계산기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자 입력: "))
#     num2 = int(input("첫번째 숫자 입력: "))
#     if num1 >=10 or num2 >=10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력했습니다 한자리 숫자만 입력하세요.")


### 사용자 정의 예외처리
# class BigNumError(Exception):
#     pass

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자 입력: "))
#     num2 = int(input("첫번째 숫자 입력: "))
#     if num1 >=10 or num2 >=10:
#         raise BigNumError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력했습니다 한자리 숫자만 입력하세요.")
# except BigNumError:
#     print("에러가 발생했습니다. 한가지 숫자만 입력해주세요(사용자 정의 에러)")
# finally: #반드시 실행됨
#     print("계산기를 이용해 주셔서 감사합니다.")


###Quiz 

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try: 
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문하겠습니까?"))
        if order < 1 or order != int(order):
            raise ValueError
        if order > chicken:
            print("치킨이 부족합니다.")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료됐습니다.".format(waiting,order))
            waiting +=1
            chicken -=order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break