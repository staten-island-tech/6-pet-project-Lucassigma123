class pet:
    def __init__(self, name, money, happiness, hunger):
        self.name=name
        self.money= int(money)
        self.happiness=happiness
        self.hunger=int(hunger) 
        self.inventory= []
        
    def buy(self, item):
          self.inventory.append(item)
          print(self.inventory)
Driddy= pet("Driddy",175,50,50)
Driddy.buy({"title": "Pizza","hunger":10})    
print (Driddy.__dict__)
while True:
        x= input("play with driddy yes to play no to no play")
        if x.lower()== "yes":
          Driddy.happiness+=10
        if Driddy.happiness>=100:
          Driddy.happiness=100
        print(f"driddy happy level", {Driddy.happiness})
        if x.lower()== "no":
          break

while True:
    y= input("feed driddy yes to feed no to starve")
    if y.lower()=="yes":
      Driddy.hunger+=10
    print(Driddy.hunger)
    if Driddy.hunger>=100:
        Driddy.hunger=100
    if y.lower()=="no":
      Driddy.hunger-=100
      print(Driddy.hunger)
    if Driddy.hunger<=0:
        print("Driddy is dead")
        break
  
        
      
