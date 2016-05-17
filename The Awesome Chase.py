import random
import time



class Settings:
    def __init__(self, name, left, right, jump, dodge):
        self.name = name
        self.left = left
        self.right = right
        self.jump = jump
        self. dodge = dodge
   
        
             
                       
#----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------        



score = 0
timer = time.clock()
lives = 3

while timer < 60 and lives  > 0 and score < 100:
    if score >= 18:
        x = random.randint(-125,125)
        y = random.randint(-125,125)
        answer = int((raw_input("What is %d + %d? " % (x,y))))
        if answer == x + y:
            print "Correct!"
            score += 1
        else:
            print "Wrong!"
            lives -= 1
    elif score >= 15:
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        answer = int(raw_input("What is %d + %d? " % (x,y)))
        if answer == x + y:
            print "Correct!"
            score += 1
        else:
            print "Wrong!"
            lives -= 1
    elif score >= 12:
        x = random.randint(-75,75)
        y = random.randint(-75,75)
        answer = int(raw_input("What is %d + %d? " % (x,y)))
        if answer == x + y:
            print "Correct!"
            score += 1
        else:
            print "Wrong!"
            lives -= 1
    elif score >= 9:
        x = random.randint(-50,50)
        y = random.randint(-50,50)
        answer = int(raw_input("What is %d + %d? " % (x,y)))        
        if answer == x + y:
            print "Correct!"
            score += 1
        else:
            print "Wrong!"
            lives -= 1
    elif score >= 6:
        x = random.randint(-25,25)
        y = random.randint(-25,25)
        answer = int(raw_input("What is %d + %d? " % (x,y)))
        if answer == x + y:
            print "Correct!"
            score += 1
        else:
            print "Wrong!"
            lives -= 1
    elif score >= 3:
        x = random.randint(-10,10)
        y = random.randint(-10,10)
        answer = int(raw_input("What is %d + %d? " % (x,y)))
        if answer == x + y:
            print "Correct!"
            score += 1
        else:
            print "Wrong!"
            lives -= 1
    elif score >= 0:
        x = random.randint(-5,5)
        y = random.randint(-5,5)
        answer = int(raw_input("What is %d + %d? " % (x,y)))
        if answer == x + y:
            print "Correct!"
            score += 1
        else:
            print "Wrong!"
            lives -= 1
if lives == 0:
    print "Oh no! You ran out of lives! Your score was %d." % score
if timer == 60:
    print "Time's up! Your score is %d." % score
else:
    print "Goodbye!"
if score == 100:
    print "Congragulations!!! You have caught your target! Your score is %d." % score






#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       




class thief:
    def __init__(self, name = 'Thief', distance = 50):
        self.name = name
        self.distance = distance  #Thief (The person being chased. The player is a shop owner whos store just got shoplifted.)                               
    def throw_object(self):
        items = ['Log', 'Shopping Cart', 'Hot Dog Stand']
        print "The thief has thrown a", (random.choice(items)),". Try Jumping over it."




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
  
        
              
                          
class alfie:
    def __init__(self, name = 'Alfie', distance = 50):
        self.name = name
        self.distance = distance #Alfie is the second character that is being chased. The player will play as a bully.
    def throw_object(self):
        items = ['rolled a Log in the way.', 'rolled a Shopping Cart in the way.', 'rolled a Hot Dog Stand in the way.', 'knocked over a Trash can.']
        print "Alfie has", (random.choice(items)),"Try Jumping over it." 
        
        



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  
  
  
class lassie:
    def __init__(self, name = 'Lassie', distance = 50):
        self.name = name
        self.distance = distance
    def throw_object(self):
        items = ['rolled a Log in the way.', 'rolled a Shopping Cart in the way.', 'rolled a Hot Dog Stand in the way.', 'knocked over a Trash can.']
        print "Lassie has", (random.choice(items)),"Try Jumping over it."   
        a = raw_input()
        if a not in 'jump':
            self.distance +=10
            print "distance =", self.distance
        if self.distance == 100:                    
            print "Ha Ha, You lost!"   
        if self.distance == 110:                    
            print "Why are you still chasing Lassie? She's gone forever!"  
            
            
  
            
                                
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



class lil_ol_miss_miriam:
    def hangman():
        allwords = "mouse", "laptop", "espanol", "fire", "mr", "ms", "mrs", "test", "taking", "take", "tips", "congruent", "protractor", "step", "steps", "sign", "exit", "enter", "not", "who", "you", "are", "that", "gaming", "question", "questions", "holds", "you", "back", "think", "thought", "games", "game", "fabric", "cloth", "screw", "nail", "hammer", "squirt", "picture", "frame", "pictureframe", "for", "it", "is", "tape", "box", "phone", "cellphone", "user", "username", "password", "pass", "ruler", "measure", "comfortable", "the", "a", "alright", "day", "days", "bench", "brick", "bricks", "earaser", "pad", "panel", "tempeture", "blackborad", "chalk", "cube", "statue", "january", "febuary", "march", "april", "may", "june", "july", "august", "october", "november", "december", "month", "months", "ice", "door", "drawing", "liberty", "well", "good", "qiuz", "objective", "geometry", "math", "english", "spanish", "video", "food", "case", "water", "soda", "pyramid", "overhead", "projector", "umbrella", "textbook", "text", "bookcase", "tacos", "burritos", "wiebe", "kyle", "volume", "control", "error", "whipe", "pen", "trash", "gear", "clock", "stool", "chair", "desk", "grease", "bread", "motor", "marker", "monitor", "wire", "input", "fit", "cane", "stack", "weed", "drugs", "printer", "back", "whiteboard", "wood", "metal", "code", "Bible", "binder", "paper", "hilighter", "pencil", "bucket", "round", "circular", "hangman", "bottle", "nag", "expo", "green", "all", "word", "cabinet", "banner", "turtle", "mouse", "jellyfish", "peanuts", "whale", "tiger", "panther", "couger", "words", "flag", "chair", "triangle", "circle", "square", "trapaziod", "hexagon", "blue", "orange", "purple", "brown", "black", "white", "red", "moroon", "gold", "silver", "bronze", "medallion", "medal", "book", "movie", "trip", "car", "bike", "trike", "tricycle", "moped", "I", "ice", "idea", "ideal", "identical", "identification", "identify",  "bye", "hi", "if", "ignore", "ill", "illegal", "illness", "illustrate", "image", "imaginary", "imagination", "imaginative", "imagine", "imitate", "immediate", "immigrant", "immoral", "impact", "impatience", "impatient", "import", "stuff", "all", "cool", "nice", "zero", "zone", "zoo", "dog", "cat", "chat", "illuminati", "computer", "hello", "yard", "yawn", "year", "yearly", "yell", "yellow", "yes", "yesterday", "yet", "you", "young", "your", "yours", "yourself", "loooooser", "winner", "alligator", "llama", "comotellamas", "supercalifragilisticexpialidocious", "table", "tactful", "tactless", "tail", "take", "takeoff", "talent", "talk", "tall", "tank", "tap", "tape", "target", "task", "taste", "tax", "taxi", "tea", "teach", "teacher", "team", "teammate", "tear", "technical", "technique" #this is the list of possible words
        bank = random.choice(allwords)  #this chooses a random word from the "allwords"
        guesses = ""                    #this is an empyty list that adds every guess you guessed to it
        turns = 5                       #this is varaible that is how many turns to get to play hangman. 
        
    
        while turns > 0:                #while you still have turns left...
            wrong = 0                   #you have 0 wrong guesses. (No letters left to guess)
            for char in bank:          #for every character in the bank
                if char in guesses:    #if the character is part of the guesses...
                    print char,        #then it prints the character you guesses in place of the underscore...
                else:                  #otherwise....
                    print "_",         #it prints an underscore
                    wrong += 1          #and your wrong goes up one. 
            if wrong == 0:             #if you have no wrongs(no letters left to guess)...
                print ""               #this is a blank line
                print "You Won!"       #it'll print that you won
                print ""               #this is a blank line
                break
        
            guess = raw_input("Guess a letter: ")  #this is actually where you guess a letter
            guesses += guess             #and it adds it to the guess list
        
            if guess not in bank:       #if your guess is not in the bank then it ...
                turns -= 1               #takes one turn away
                print ""
                print "Wrong Letter"    #and tells you it was wrong
                print ""                #this is a blank line
                print "You have", turns, "turns left!"   #and it tells you how many turns you have left. 
                print ""                #this is a blank line
            
        if turns == 0:                   #if you used all your turns 
            print "Ha Ha, You lost!"     #it prints that you lost
            print "The word was", bank  #and tells you what the word was
            print ""                    #this is a blank line
        
        print "Did you like the game?"    #asks if you like the game
        a = raw_input()                 #you write your awnser. 
        aff = ['yes']                   #if it was yes...
        if a in aff:
            print "You are awesome, amazing and cool! Thanks, play agian!!!"   #it says that 
        else:
            print "You suck, you know that right? Just so you know."          #if not it says that. 
        
        
