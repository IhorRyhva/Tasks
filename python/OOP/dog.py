class Dog:
    name = None
    age = None
    isHappy = None
    
    def __init__(self, name = 'Bob', age = 1, isHappy = True):
        self.set_data(name, age, isHappy)
        self.get_data()
    
    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy
        
    def get_data(self):
        print("Name:",self.name, "Age:", self.age, "Is happy?",self.isHappy)


dog1 = Dog("Scubi", 3, True)
dog2 = Dog("Bob", 2, False)
dog3 = Dog("July")
dog4 = Dog(age=1.2)