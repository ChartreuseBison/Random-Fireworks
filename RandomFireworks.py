#Python Version
#Written by: Chartreuse Bison

#import pyperclip #install and import this if you want to copy rocket comamnds to clipboard
import random

#function to genrate a random rocket command
def newRocket():

   firework = "/summon firework_rocket "

   randX = posX+random.randint(-10,10) #random x distance from start
   randZ = posZ+random.randint(-10,10) #random z distance from start
   randLife = random.randint(20,30) #random how long the rocket lives
   randSpeed = round(random.uniform(0.1,3.0),2) #random speed of the rocket
   randType = [0,0,0,1,1,1,2,2,3,4,4] #shape of explosion, biased towards circles
   randFlick = random.randint(0,1) #does it flicker or not
   randTrail = random.randint(0,1) #does it have a trail or not
   numColors = random.randint(1,3) #1 to 3 different colors
   numFades = random.randint(1,3) # 1 to 3 differnt fade colors
   color1 = random.randint(16700000, 16799999) #random colors
   color2 = random.randint(16700000, 16799999)
   color3 = random.randint(16700000, 16799999)
   fade1 = random.randint(16700000, 16799999)
   fade2 = random.randint(16700000, 16799999)
   fade3 = random.randint(16700000, 16799999)
   
   firework += str(randX) +" " + str(posY) +" " + str(randZ)
   firework += " {LifeTime:" + str(randLife) + ",Motion:[0.00," + str(randSpeed) + ",0.00],"
   firework += "FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Explosions:[{Type:" + str(random.choice(randType)) + ",Flicker:" + str(randFlick) + ",Trail:" + str(randTrail)
   firework += ",Colors:[I; " + str(color1)
   if numColors > 1:
      firework += ", " + str(color2)
   if numColors > 2:
      firework += ", " + str(color3)
   firework += "],FadeColors:[I;" + str(fade1)
   if numFades > 1:
      firework += ", " + str(fade2)
   if numFades > 2:
      firework += ", " + str(fade3)
   firework += "]}]}}}}"
   
   #print (firework)
   #pyperclip.copy(firework) #use thiss line to copy to clipboard if you jsut want individual commands, dont foregt to uncomment the import up top 
   return firework

# Start of Main Script

#use these 3 lines if you want to type in tour start coordinates each time
posX = int(input("What Is the X start position? >")) #<<<< Comment me out if you want to hardcode your coordinates <<<
posY = int(input("What Is the Y start position? >")) #<<<< Comment me out if you want to hardcode your coordinates <<<
posZ = int(input("What Is the Z start position? >")) #<<<< Comment me out if you want to hardcode your coordinates <<<

#un-comment these 3 lines, and comment the ones above and type in your own values if you don't want to type your start coordinates each time you run the script 
#posX = 425  #<<<<< uncomment for hardcoded position <<<<<
#posY = 22  #<<<<< uncomment for hardcoded position <<<<<
#posZ = 1382  #<<<<< uncomment for hardcoded position <<<<<

showLen = int(input("Type the length of a new function, or 0 to exit\nHow long should the show be? >"))

while showLen > 0:
   
   showList = open('firework.mcfunction', mode='w', newline='\n', encoding="utf-8") #open function file
   
   showList.write("#Clear out space, since command blocks don't replace right\nfill ~ ~ ~ ~" + str((showLen*4)+5) + " ~ ~8 minecraft:air")#clear out space
   showList.write("\n#set start button\nsetblock ~2 ~ ~ minecraft:quartz_block\nsetblock ~1 ~ ~ minecraft:stone_button[facing=west]\n#begin rocket groups")#place start block

   randDelay = [4,4,4,3,3,2,1] #random dealy between each group, biased towards 4 ticks
   numShots = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,4,4,5] #random number of shots per group, biased towards lower amounts

   for x in range(int(showLen)): #iterates through each group of fireworks
      pos = (x*4)+3 #get the offset X position of each set of firweorks
    
      showList.write("\nfill ~" + str(pos) + " ~-1 ~ ~" + str(pos+3) + " ~-1 ~1 minecraft:stone") #create a floor for the redstone
      showList.write("\nsetblock ~" + str(pos) + " ~ ~ minecraft:repeater[facing=west,delay=4]")
      showList.write("\nsetblock ~" + str(pos+1) + " ~ ~ minecraft:repeater[facing=west,delay=4]")
      showList.write("\nsetblock ~" + str(pos+2) + " ~ ~ minecraft:repeater[facing=west,delay=" + str(random.choice(randDelay)) + "]") #repeater with random delay
      pos +=3 #move to the command blocks and redstone wire
      showList.write("\nsetblock ~" + str(pos) + " ~ ~ minecraft:redstone_wire[west=side,east=side,south=side]")
      showList.write("\nsetblock ~" + str(pos) + " ~ ~1 minecraft:repeater[facing=north,delay=1]")
      #start placing command blocks  
      showList.write("\nsetblock ~" + str(pos) + " ~ ~2 minecraft:command_block[facing=south]{Command:\"" + newRocket() + "\"}") #command block with random rocket command
      randNumShots = random.choice(numShots)
      if randNumShots > 1:
         for y in range(randNumShots): #place more rockets per group
            showList.write("\nsetblock ~" + str(pos) + " ~ ~" + str(y+3) + " minecraft:chain_command_block[facing=south]{Command:\"" + newRocket() + "\"}")  #extra command block with random rocket command
      #end for loop of rocket groups
   #linking function, stand behind the quartz block to the right and run the funtion again after re-running the script and reloading
   showList.write("\n#This section links back to another show\nfill ~" + str(pos+1) + " ~-1 ~ ~" + str(pos+3) + " ~-1 ~ minecraft:stone")
   showList.write("\nsetblock ~" + str(pos+1) + " ~ ~ minecraft:repeater[facing=west,delay=1]\nsetblock ~" + str(pos+3) + " ~ ~ minecraft:repeater[facing=west,delay=1]")
   showList.write("\nsetblock ~" + str(pos+2) + " ~ ~ minecraft:command_block[facing=east]{Command:\"/setblock ~-" + str(pos) + " ~ ~8 minecraft:redstone_block\"}")
   showList.write("\nsetblock ~" + str(pos+4) + " ~ ~ minecraft:command_block[facing=east]{Command:\"/setblock ~-" + str(pos+2) + " ~ ~8 minecraft:air\"}")
   showList.write("\nsetblock ~1 ~ ~8 minecraft:quartz_block") #place start block for next function run
   #newRocket()
   showList.close() #close file
   
   print ("Function generated, remember to type /reload in Minecraft")
   showLen = int(input("\nType the length of a new function, or 0 to exit\nHow long should the show be? >"))