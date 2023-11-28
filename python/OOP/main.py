class Build:
    __year = None
    __city = None
    
    
    def __init__(self, year, city):
        self.year = year
        self.city = city
        
        
    def getInfo(self):
        print("Year: ", self.year, " City: ", self.city, sep="")
        
class Shool(Build):
    __pupils = None
    
    def __init__(self, year, city, pupils=500):
        super().__init__(year, city)
        self.pupils = pupils
    
    def getInfo(self):
        super().getInfo()
        print(" Pupils: ", self.pupils)
        
class House(Build):
    pass   
     
class Shop(Build):
    pass

school = Shool(1995, "Seattle", 720)
school.getInfo()

house = House(2010, "New York")
house.getInfo()
shop = Shop(2000, "Miami")