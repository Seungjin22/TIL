"""
아래처럼 리스트에 단일 값을 넣는 add() 메서드와
값을 두 번 넣어주는 add_twice() 메서드를 가진 Bag 클래스를 작성하시오.
bag = Bag()
bag.add(1)
bag.add_twice(5)
bag.data
>> [1, 5, 5]
"""

class Bag:

    def __init__(self):
        self.data = []

    def add(self, x):
        self.x = x
        self.data.append(x)
        return self.data

    def add_twice(self, x):
        self.x = x
        self.data.append(x)
        self.data.append(x)
        return self.data

bag = Bag()
bag.add(1)
bag.add_twice(5)
print(bag.data)

