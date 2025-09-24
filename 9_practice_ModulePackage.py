### 모듈
# import theater_module
# theater_module.price(3) #일반인 3명 영화 가격
# theater_module.price_morning(4) #일반인 4명 조조할인 영화 가격
# theater_module.price_student(3) #학생 3명 학생할인 영화 가격

### 모듈을 mv라는 별칭으로 부르기
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_student(3)

### 모듈에 있는 모든 것을 사용하겠다.
# from theater_module import *
# price(3)
# price_morning(4)
# price_student(3)

### 모듈에 있는 것중 일부만 사용
# from theater_module import price, price_student
# price(3)
# price_student(3)

### 모듈에 있는 것중 일부만 사용하고 별칭만으로 사용 가능
# from theater_module import price_morning as price
# price(2)


### 패키지: 모듈들을 모아놓은 집합
##구문1 (패키지, 모듈만 가능)
# import pack.module1 #이 구문의 끝에는 '모듈'이나 '패키지'만 가능. 클래스(X)
# present = pack.module1.pack1()
# present.detail()

# from pack import module2
# present = module2.pack2()
# present.detail()

##구문2 (패키지, 모듈, 클래스 가능)
# from pack.module1 import pack1 #이 구문에는 클래스도 포함 가능
# present = pack1()
# present.detail()

##구문3
# from pack import *
# present = module2.pack2()
# present.detail()

# from pack import *
# # test = module1.pack1()
# # test.detail()


# ###패키지, 모듈이 어느 위치에 있는지 확인
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(module1))



### Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈
## 모듈 파일명 createdbyDan.py

import createdbyDan
createdbyDan.sign()