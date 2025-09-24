# 스타크래프트에 비유한 클래스
### 클래스 미사용
# # 마린
# name = "마린" # 유닛 이름
# hp = 40 # 유닛 체력
# damage = 5 # 유닛 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {}, 공격력 {}".format(hp, damage))

# # 탱크
# tank_name = "탱크" 
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {}, 공격력 {}".format(tank_hp, tank_damage))

# # 탱크2
# tank2_name = "탱크" 
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {}, 공격력 {}".format(tank_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "2시", damage)
# attack(tank_name, "2시", tank_damage)
# attack(tank_name, "2시", tank2_damage)

### 클래스 사용
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {}, 공격력 {}".format(self.hp, self.damage))

### 클래스 (상속)
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# # 마린, 탱크는 Unit 클래스의 인스턴스(객체)
# 마린 = Unit("마린", 40, 5)
# 마린2 = Unit("마린", 40, 5)
# 탱크 = Unit("탱크", 150, 35)
# 탱크2 = Unit("탱크", 150, 35)


### 멤버 변수
# # 멤버 변수 사용
# 레이스1 = Unit("레이스", 80, 10)
# print("유닛 이름 : {0}, 공격력 : {1}".format(레이스1.name, 레이스1.damage))

# # clocking 이라는 멤버 변수를 추가하여 사용할 수 있음
# 레이스2 = Unit("빼앗은 레이스", 80, 5)
# 레이스2.clocking = True

# # 확장을 한 객체에 대해서만 멤버 변수 사용 가능 X (레이스1.clocking = True 불가)
# if 레이스2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(레이스2.name))


### 메서드란: 클래스 안에 정의된 함수
## 공격 유닛
# class AttackUnit: # 생성자 메서드
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

## 공격 유닛 (상속)
class AttackUnit(Unit): # 생성자 메서드
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage


### self는 자신을 의미, lacation은 전달받은 값을 사용.
#     def attack(self, location): #공격 메서드
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage): #피해 메서드
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 유닛이 죽었습니다.".format(self.name))

# 파이어벳1 = AttackUnit("파이어벳", 50, 16)
# 파이어벳1.attack("5시")
# 파이어벳1.damaged(25)
# 파이어벳1.damaged(25)

# 날 수 있는 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


### 다중 상속
##날 수 있고 / 공격도 가능한 유닛
class FlyableAttackUnit(AttackUnit, Flyable): # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    # 메서드 오버라이딩
    def move(self, location): # Unit(부모)클래스의 move 메서드를 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 발키리 = FlyableAttackUnit("발키리", 200, 6, 5)
# 발키리.fly(발키리.name, "7시")

##오버라이딩 구현 테스트
# 벌처 = AttackUnit("벌처", 80, 10, 20)
# 배틀크루저 = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# 벌처.move("2시")
# 배틀크루저.move("9시")


###pass
## 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 일단은 아무것도 안하고 넘어감

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

### super
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0) # ()괄호 추가 self 생략 가능
#         self.location = location