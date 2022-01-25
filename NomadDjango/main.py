class Car():
  # wheels = 4
  # doors = 4
  # windows = 4
  # seats = 4

  def __init__(self, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black")  # kwargs로 color가 지정되지 않았다면 color="black"
    self.price = kwargs.get("price", "$100")  # kwargs로 price가 지정되지 않았다면 price="$100"

  def __str__(self):  # instance Car를 print하려고 할 때 호출되는 메소드지만, 이렇게 재정의 가능.
    return f"Car with {self.wheels} wheels"

  def start(self):  # 이건 method
    print(self.doors)
    print("I started")


def sample():  # 이건 function
  print("Just sample")

porche = Car(color="green", price="$4000")
print("porche", porche.color, porche.price)

ferrari = Car()
print("ferrari", ferrari.color, ferrari.price)

mini = Car()
mini.color = "White"
print("mini", mini)

print(dir(Car))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'doors', 'seats', 'start', 'wheels', 'windows']


# Django, Python은 객체지향 프로그래밍

# 1. 모든 메소드는 첫번째 인자로 instance가 자동적으로 부여된다.
# 2. 따라서 메소드를 작성할때 첫번째 인자를 관례적으로 self로 넣어주어야만한다. (다른 것으로 대체해도 되지만 Convention을 따르자)