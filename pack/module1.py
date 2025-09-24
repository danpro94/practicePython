class pack1:
    def detail(self):
        print("첫번째 패키지 모듈입니다. 가방, 신발이 들어있어요.")
    # __name__: str

###모듈 직접 실행
if __name__ == "__main__":
    print("module1 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행됨")
    test = pack1()
    test.detail()
else:
    print("module1 외부에서 모듈 호출")
