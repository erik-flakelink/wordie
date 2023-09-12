import random
import time
import os
firsttime = True
wordlist = ["Ale","Zero","Hamm","Ruble","Denim","Jeans","Hexadecimal","Talkative","Crystal","Coincide","Practice","Distributor","Explain","Enthusiasm","Suffering","Decoration","Innocent","Knowledge","Infection","Traction","Innocent","Migration","Sculpture","Survival"]
wordie = wordlist[random.randint(0, len(wordlist) - 1)]
print("WORDIE")
print("SELECT A DIFFICULTY:")
print("[1] - Toddler")
print(" > Reveals the first and last letter at start, Reveals letters as you guess correctly, Infinite Tries")
print("[2] - Easy")
print(" > Reveals the first letter at start, Reveals letters as you guess correctly, Infinite Tries")
print("[3] - Normal")
print(" > Reveals a random letter at start, Reveals letters as you guess correctly, Infinite Tries")
print("[4] - Hard")
print(" > Doesn't reveal anything at start, Reveals letters as you guess correctly, 10 Tries")
print("[5] - Extreme")
print(" > Maximum is [length-of-word tries], No Reveals whatsoever.")
time.sleep(3)
choice = input()
correct_pos = []
def configure_word():
    if choice == "[1]":
        r_as_you_go = True
        correct_pos.append(1)
        correct_pos.append(len(wordie))
        pos = 0
        wordo = []
        for i in wordie:
            pos += 1
            if pos in correct_pos:
                wordo.append(i)
            else:
                wordo.append("-")
        worde = ""
        for i in wordo:
            worde += str(i)
        return worde
    elif choice == "[2]":
        r_as_you_go = True
        correct_pos.append(1)
        pos = 0
        wordo = []
        for i in wordie:
            pos += 1
            if pos in correct_pos:
                wordo.append(i)
            else:
                wordo.append("-")
        worde = ""
        for i in wordo:
            worde += str(i)
        return worde
    elif choice == "[3]":
        r_as_you_go = True
        if firsttime == True:
            correct_pos.append(random.randint(1, len(wordie)))
            firsttime = False
        pos = 0
        wordo = []
        for i in wordie:
            pos += 1
            if pos in correct_pos:
                wordo.append(i)
            else:
                wordo.append("-")
        worde = ""
        for i in wordo:
            worde += str(i)
        return worde
    elif choice == "[4]":
        r_as_you_go = True
        pos = 0
        wordo = []
        for i in wordie:
            pos += 1
            if pos in correct_pos:
                wordo.append(i)
            else:
                wordo.append("-")
        worde = ""
        for i in wordo:
            worde += str(i)
        return worde
    elif choice == "[5]":
        r_as_you_go = False
        pos = 0
        wordo = []
        for i in wordie:
            pos += 1
            if pos in correct_pos:
                wordo.append(i)
            else:
                wordo.append("-")
        worde = ""
        for i in wordo:
            worde += str(i)
        return worde
os.system('cls')
wordio = configure_word()
print(wordio)
if choice == "[1]" or choice == "[2]" or choice == "[3]":
    tries = "INFINITE"
    r_as_you_go = True
elif choice == "[4]":
    tries = 10
    r_as_you_go = True
elif choice == "[5]":
    tries = len(wordie)
    r_as_you_go = True
while tries != 0:
    pos = int(input("Letter: ")) - 1
    guess = input("Guess: ")
    if wordie[pos] == guess:
        if r_as_you_go == True:
            print("CORRECT")
            correct_pos.append(pos + 1)
    else:
        if r_as_you_go == False:
            pass
        else:
            print("INCORRECT")
    if type(tries) == 'int':
        tries -= 1
    time.sleep(1)
    os.system('cls')
    wordio = configure_word()
    print(wordio)
    if wordio == wordie:
        print("YOU WIN!")
        print("DIFFICULTY:", choice)
        print("WORD:", wordie)
        smth = input()
        exit(0)
print("GAME OVER")
print("WORD:", wordie)

    
        
    
