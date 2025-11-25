
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
import random

Driddy.buy({"title": "Pizza","hunger":10})    
print (Driddy.__dict__)
def dead():
     if Driddy.energy<=0:
         print("game over Driddy died of exhaustion")
         quit()


def play():
    while True:
        dead()
        x= input("1: play 2: no play")
        if x.lower()== "1": 
          Driddy.happiness+=10
          Driddy.energy-=10
          Driddy.hunger-=25
        if Driddy.happiness>=100:
          Driddy.happiness=100
        print(f"driddy happy level", {Driddy.happiness})
        print(f"Energy", {Driddy.energy})
        print("Hunger",Driddy.hunger)
        if x.lower()== "2":
          break
        if Driddy.hunger==0:
           print("Driddy has starved")
           quit()
        
def run():
    while True:
      dead()
      y= input("1: feed 2: starve 3: continue")
      if y=="1":
        Driddy.hunger+=10
        Driddy.money-=10
        print("money",Driddy.money)
      if y=="2":
        print("The end Driddy ate you")
        quit()
      if Driddy.hunger>=100:
        Driddy.hunger=100
        print("Driddy is full")
        break
      print("hunger", Driddy.hunger)
      if y=="3":
          break 
      if Driddy.money<=0:
         print("bankrupt game over")
         quit()
   
      


def aaa():
    while True:
     dead()
     sleep=input("1: sleep 2: leave")
     if sleep==("1"):                                       
        Driddy.energy+=10
        Driddy.money+=10
     print ("Energy",Driddy.energy)
     print("money",Driddy.money)
     if Driddy.energy>=100:
       Driddy.energy=100                                    
       print("driddy is energized")
       break
     if sleep=="2":
        break


def sigma1():    
 while True:
  dead()
  workout=input("1: workout 2:leave")
  if workout=="1":
     Driddy.energy-=25
     Driddy.hunger-=25
  elif workout=="2":
     break
  if Driddy.hunger==0:
     print("Driddy has starved to death")
     quit()
  print("energy",Driddy.energy)
  print("hunger",Driddy.hunger)

def shop():
   while True:
      xyz=random.randint(0,15)
      shopa=input("1: lottery ticket $10 2: leave ")
      if shopa=="1":
         print("$",xyz,"WINNER")
         Driddy.money-=10
         Driddy.money+=xyz
      if xyz==0:
         print("loser")
      if shopa=="2":
         break
      if Driddy.money<=0:
         print("bankrupt game over")
         quit()
   

def stats():
 print (Driddy.__dict__)
 
         
     
         

while True:
  main={
         1:"play",
         2:"feed",
         3:"sleep",
         4:"workout",
         5:"quit" ,
         6:"SHOP",
         7:"stats"
           }
  print(main)
  sigma = input("Choose option")
  if sigma=="1":
      play()
  elif sigma=="2":
      run()
  elif sigma=="3":
      aaa()
  elif sigma=="4":
      sigma1()
  elif sigma=="5":
     quit()
  elif sigma =="6":
     shop()
  elif sigma=="7":
     stats()
  else:
     print("INVALID OPTION READ")


    
      
      