
# Soldier


class Soldier:
    
    def __init__(self,health,strength): 
        
        self.health=health
        self.strength=strength
    
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self,damage):
        
        self.health-=damage

# Viking


class Viking(Soldier):
    
    def __init__(self,name,health,strength):
        
        self.name=name
        self.health=health
        self.strength=strength
        
        
    def receiveDamage(self,damage):
        
        self.health-=damage
        
        if self.health>0:
            
            return self.name+' '+'has received'+' '+str(damage)+' '+'points of damage'
        
        else:

            return self.name+' '+'has died in act of combat'

     
    def battleCry(self):
        
        return 'Odin Owns You All!'


# Saxon


class Saxon(Soldier):
    
    def __init__(self,health,strength):
        
        self.health=health
        self.strength=strength
        
    def receiveDamage(self,damage):
        
        self.health-=damage
        
        if self.health>0:
            
            return 'A Saxon has received'+' '+str(damage)+' '+'points of damage'
        
        else:

            return 'A Saxon has died in combat'



# War
import random

class War:
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        
        self.saxonArmy.append(Saxon)
            
    def vikingAttack(self):
        
        vikhit = random.choice(self.vikingArmy)
        saxhit = random.choice(self.saxonArmy)

        dam_sa = saxhit.receiveDamage(vikhit.attack())
        
        if saxhit.health <= 0:
            
            self.saxonArmy.remove(saxhit)

        return dam_sa

    def saxonAttack(self):
        
        vik1hit = random.choice(self.vikingArmy)
        sax1hit = random.choice(self.saxonArmy)

        dam_vi = vik1hit.receiveDamage(sax1hit.attack()) 

        if vik1hit.health <= 0 :
            self.vikingArmy.remove(vik1hit)

        return dam_vi

    def showStatus(self):
        
        if len(self.saxonArmy) == 0:
            
            return 'Vikings have won the war of the century!'
        
        elif len(self.vikingArmy) == 0:
            
            return 'Saxons have fought for their lives and survive another day...'
        
        else:
            
            return 'Vikings and Saxons are still in the thick of battle.'    
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
