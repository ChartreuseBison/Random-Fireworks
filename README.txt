# Random-Fireworks
I wrote and tested with python version 3.6 
This script generates a mcfunction file to to place a randomized fireworks show
I just have it set to run the script in your function directory

The default function is for the script to ask you to enter the X, Y, and Z for the launch position of the rockets. I recommend editing the script and hardcoding these values so you don't have to type them each time. Just comment out the coordinate prompts and then uncomment the hardcoded coordinate lines. Then you can add your coordinates.
I did this rather than relative coordinates so you can stick the circuit wherever you have the space, and the show can be in a different location. 
Rockets will fire a random distance of 10 blocks horizontally from this position. 

The script asks you for how long the show should be, this is the number of fireworks groups.
Each group has 1 to 5 fireworks, biased towards lower numbers. 
The delay between each group is 9 to 12 ticks, even with this the FPS kinda sucks.

Command blocks will be placed for each random rocket, rockets can be randomized with:
 -X,Z start position 
-random life of the rocket
-random speed of the rocket
-random shape of the firework, biased towards round ones
-random flicker or not
-random colors, up to 3 of them
-up to 2 random fade colors 

Once you have run the script, reload in minecraft and you can run the function.
The command blocks place out in the positive X Direction (Red line in F3 view mode)
-The length will be the length of the show you entered times 4 (plus 6 for start/end)
The circuit will be up to 8 blocks wide in the positive Z direction (Blue line in F3 mode)
The circuit is only one block high, although it does place its own floor
Be careful if you run it underground, water or lava might hit the circuit. 

I also added a linking function to the end of the show, so you can group multiple shows if you have limited X space, or want a really big number that a single function can’t place. 
(I only tested with show length in the double digits, I take no responsibility if you enter big numbers)
The link function places a redstone block off to the right to start another show.
To link another show:
-run the script again (unless you want duplicates) 
-stand in front of the quartz block that was placed to the right of the circuit
-reload and run the function again

If you are getting unknown function, your functions might not be in the right folders, or you entered a value minecraft can't read 

