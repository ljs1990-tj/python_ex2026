# [파이썬 기초: 클래스와 상속 실습 예제]

# ---------------------------------------------------------
# 1. 기본 클래스 정의 (Robot)
# ---------------------------------------------------------
class Robot:
    # [클래스 변수] 
    # 모든 Robot 인스턴스가 공유합니다. (자바의 static 변수와 유사)
    population = 0

    def __init__(self, name):
        # [인스턴스 변수]
        # self.name은 자바의 this.name과 같습니다.
        self.name = name
        Robot.population += 1
        print(f"{self.name} 로봇이 생성되었습니다.")

    def say_hello(self):
        """인스턴스 메서드: 로봇이 인사를 합니다."""
        print(f"안녕! 내 이름은 {self.name}이야.")

    def destroy(self):
        """로봇이 파괴될 때 인구수를 줄입니다."""
        print(f"{self.name} 로봇을 파괴합니다.")
        Robot.population -= 1

# ---------------------------------------------------------
# 2. 클래스 사용(객체 생성)
# ---------------------------------------------------------
print("--- [1. 객체 생성 및 인스턴스 메서드] ---")
bot1 = Robot("R2D2")
bot2 = Robot("C3PO")

bot1.say_hello()
bot2.say_hello()

print(f"현재 총 로봇 수: {Robot.population}") # 클래스 변수 접근
print()


# ---------------------------------------------------------
# 3. 상속 (Inheritance)
# ---------------------------------------------------------
print("--- [2. 클래스 상속] ---")

# Robot 클래스를 상속받는 CombatRobot (전투용 로봇)
class CombatRobot(Robot):
    def __init__(self, name, weapon):
        # 부모 클래스의 생성자를 호출하여 name을 초기화합니다.
        super().__init__(name)
        self.weapon = weapon # 자식 클래스만의 새로운 속성

    def attack(self):
        """자식 클래스에만 있는 새로운 메서드"""
        print(f"{self.name}이(가) {self.weapon}(으)로 공격합니다!")

    # [메서드 오버라이딩] 부모의 메서드를 재정의합니다.
    def say_hello(self):
        print(f"나는 전투 로봇 {self.name}이다. 무기는 {self.weapon}이다.")

# 자식 클래스 객체 생성
warrior = CombatRobot("Gundam", "레이저 빔")
warrior.say_hello() # 오버라이딩된 메서드 호출
warrior.attack()    # 자식 전용 메서드 호출

print(f"최종 총 로봇 수: {Robot.population}")
print()

# ---------------------------------------------------------
# [초보자 꿀팁]
# 1. 파이썬 메서드의 첫 번째 인자는 무조건 'self'입니다. 호출할 때는 안 써도 됩니다.
# 2. 클래스 내부에서 클래스 변수를 쓸 때는 'ClassName.variable' 형태로 쓰는 것이 명확합니다.
# 3. 상속 시 super()를 쓰면 부모의 기능을 그대로 쓰면서 새로운 기능만 추가할 수 있습니다.
# ---------------------------------------------------------