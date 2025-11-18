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
Driddy= pet("Driddy",175,50,50,50)
Driddy.buy({"title": "Pizza","hunger":10})    
print (Driddy.__dict__)
def dead():
     if Driddy.energy<=0:
         print("game over Driddy died of exhaustion")
         quit()


def play():
    while True:
        dead()
        x= input("play with driddy yes to play no to no play")
        if x.lower()== "yes": 
          Driddy.happiness+=10
          Driddy.energy-=10
        if Driddy.happiness>=100:
          Driddy.happiness=100
        print(f"driddy happy level", {Driddy.happiness})
        print(f"Energy", {Driddy.energy})
        if x.lower()== "no":
          break
        
def run():
    while True:
      dead()
      y= input("feed driddy yes to feed no to starve type continue to continue")
      if y.lower()=="yes":
        Driddy.hunger+=10
      if y.lower()=="no":
        print("The end Driddy ate you")
        quit()
      
   
      if Driddy.hunger>=100:
        Driddy.hunger=100
        print("Driddy is full")
      print("hunger", Driddy.hunger)
    
    
      if y.lower()=="continue":
         break
def aaa():
    while True:
     dead()
     sleep=input("type sleep to let driddy rest for 1 hour no to no rest")
     if sleep.lower()==("sleep"):
        Driddy.energy+=10
     print ("Energy",Driddy.energy)
     if Driddy.energy>=100:
        Driddy.energy=100
        print("driddy is energized")
        break
     if sleep.lower()=="no":
        break


def sigma():    
 while True:
  dead()
  workout=input("type workout to workout no to no workout")
  if workout.lower()=="workout":
     Driddy.energy-=25
  print("energy",Driddy.energy)
  if workout.lower()=="no":
     break


  
   
 
        
       
    

while True:
  main={
         1:"play",
         2:"feed",
         3:"sleep",
         4:"workout" }
  print(main)
  sigma==input("Choose option")
  if main=="1":
      play()
  if main=="2":
      run()
  if main=="3":
      aaa()
  if main=="4":
     sigma()


    
      
      
           