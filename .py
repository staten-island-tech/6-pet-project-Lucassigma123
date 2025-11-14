class pet:
    def __init__(self, name, money, happiness, hunger, energy):
        self.name=name
        self.money= int(money)
        self.happiness=happiness
        self.hunger=int(hunger) 
        self.inventory= []
        self.energy=int(energy)
        
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
    y= input("feed driddy yes to feed no to starve type continue to continue")
    if y.lower()=="yes":
      Driddy.hunger+=10
    if y.lower()=="no":
        print("The end Driddy ate you")
        quit()
      
   
    if Driddy.hunger>=100:
        Driddy.hunger=100
        print("Driddy is full")
        print("hunger",  Driddy.hunger)
        
    print("hunger", Driddy.hunger)
    
    
    if y.lower()=="continue":
        break
    

    
      
      
           