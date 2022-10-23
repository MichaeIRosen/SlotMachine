import random

##########################################
##--------- Slot Machine class ---------##
##########################################

class SlotMachine:
    leftSymbol = ""
    middleSymbol = ""
    rightSymbol = ""



    def spin(self):
        self.leftSymbol = self.getSymbol(random.randint(1, 156))
        self.middleSymbol = self.getSymbol(random.randint(1, 156))
        self.rightSymbol = self.getSymbol(random.randint(1, 156))



    def sameSymbols(self):
        if(self.leftSymbol == self.middleSymbol == self.rightSymbol):
            return True
        return False



    def getSymbol(self, n):
        if(0 < n <= 50):
            return Symbols[0]
        if(50 < n <= 90):
            return Symbols[1]
        if(90 < n <= 120):
            return Symbols[2]
        if(120 < n <= 140):
            return Symbols[3]
        if(140 < n <= 150):
            return Symbols[4]
        if(150 < n <= 155):
            return Symbols[5]
        if(n == 156):
            return Symbols[6]


##########################################
##--------------- Tuples ---------------##
##########################################

Symbols = ("#", "&", "@", "!", "€", "£", "$")
Values = (5, 10, 20, 70, 200, 1000, 100000)


##########################################
##---------- Printing methods ----------##
##########################################

def printSlotMachine(l, m, r):
    print("  +--------+")
    print("  | CASINO |")
    print("  |--------| *")
    print("  |" + l + " |" + m + " |" + r + " | |")
    print("  |--------|/")
    print("  |    [_] |")
    print("  +--------+\n")

#----------------------------------------#

def printCreditsRemaining(credits):
    print("Credits remaining: ", credits, " credits\n")

#----------------------------------------#

def printTitle():
    print("\n")
    print("                                       $$$$$$\  $$\       $$$$$$\ $$$$$$$$\       $$\      $$\  $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$\ $$\   $$\ $$$$$$$$\\ ")
    print("                                       $$  __$$\ $$ |     $$  __$$\\__$$  __|      $$$\    $$$ |$$  __$$\ $$  __$$\ $$ |  $$ |\_$$  _|$$$\  $$ |$$  _____|")
    print("                                      $$ /  \__|$$ |     $$ /  $$ |  $$ |         $$$$\  $$$$ |$$ /  $$ |$$ /  \__|$$ |  $$ |  $$ |  $$$$\ $$ |$$ |       ")
    print("                                      \$$$$$$\  $$ |     $$ |  $$ |  $$ |         $$\$$\$$ $$ |$$$$$$$$ |$$ |      $$$$$$$$ |  $$ |  $$ $$\$$ |$$$$$\     ")
    print("                                       \____$$\ $$ |     $$ |  $$ |  $$ |         $$ \$$$  $$ |$$  __$$ |$$ |      $$  __$$ |  $$ |  $$ \$$$$ |$$  __|    ")
    print("                                      $$\   $$ |$$ |     $$ |  $$ |  $$ |         $$ |\$  /$$ |$$ |  $$ |$$ |  $$\ $$ |  $$ |  $$ |  $$ |\$$$ |$$ |       ")
    print("                                      \$$$$$$  |$$$$$$$$\ $$$$$$  |  $$ |         $$ | \_/ $$ |$$ |  $$ |\$$$$$$  |$$ |  $$ |$$$$$$\ $$ | \$$ |$$$$$$$$\  ")
    print("                                       \______/ \________|\______/   \__|         \__|     \__|\__|  \__| \______/ \__|  \__|\______|\__|  \__|\________| ")
    print("")
    print("                                                   $$\       $$\       $$\                                     $$\       $$\       $$\\                  ")
    print("                                                 $$$$$$\   $$$$$$\   $$$$$$\\                                $$$$$$\   $$$$$$\   $$$$$$\\                ")
    print("                                                $$  __$$\ $$  __$$\ $$  __$$\\                              $$  __$$\ $$  __$$\ $$  __$$\\               ")
    print("                                                $$ /  \__|$$ /  \__|$$ /  \__|                              $$ /  \__|$$ /  \__|$$ /  \__|               ")
    print("                                                \$$$$$$\  \$$$$$$\  \$$$$$$\\                               \$$$$$$\  \$$$$$$\  \$$$$$$\\                ")
    print("                                                 \___ $$\  \___ $$\  \___ $$\\                               \___ $$\  \___ $$\  \___ $$\\               ")
    print("                                                $$\  \$$ |$$\  \$$ |$$\  \$$ |                              $$\  \$$ |$$\  \$$ |$$\  \$$ |               ")
    print("                                                \$$$$$$  |\$$$$$$  |\$$$$$$  |                              \$$$$$$  |\$$$$$$  |\$$$$$$  |               ")
    print("                                                 \_$$  _/  \_$$  _/  \_$$  _/                                \_$$  _/  \_$$  _/  \_$$  _/                ")
    print("                                                   \ _/      \ _/      \ _/                                    \ _/      \ _/      \ _/                  ")
    print("   _____                       _                  _ _   _                         _ _ _            _____                                   _              _ _   _                              _ ")
    print("  / ____|                     (_)                (_) | | |                       | (_) |          / ____|                                 | |            (_) | | |                            | |")
    print(" | |     ___  _ __ ___   ___   _ _ __   __      ___| |_| |__     ___ _ __ ___  __| |_| |_ ___    | |     ___  _ __ ___   ___    ___  _   _| |_  __      ___| |_| |__    _ __   ___  _ __   ___| |")
    print(" | |    / _ \| '_ ` _ \ / _ \ | | '_ \  \ \ /\ / / | __| '_ \   / __| '__/ _ \/ _` | | __/ __|   | |    / _ \| '_ ` _ \ / _ \  / _ \| | | | __| \ \ /\ / / | __| '_ \  | '_ \ / _ \| '_ \ / _ \ |")
    print(" | |___| (_) | | | | | |  __/ | | | | |  \ V  V /| | |_| | | | | (__| | |  __/ (_| | | |_\__ \_  | |___| (_) | | | | | |  __/ | (_) | |_| | |_   \ V  V /| | |_| | | | | | | | (_) | | | |  __/_|")
    print("  \_____\___/|_| |_| |_|\___| |_|_| |_|   \_/\_/ |_|\__|_| |_|  \___|_|  \___|\__,_|_|\__|___( )  \_____\___/|_| |_| |_|\___|  \___/ \__,_|\__|   \_/\_/ |_|\__|_| |_| |_| |_|\___/|_| |_|\___(_)")
    print("                                                                                             |/                                                                                                  ")
    print("\n\n")

##########################################
##-------- Complementary methods -------##
##########################################

def getMultiplicationIndex(symbol):
    index = 0
    for x in Symbols:
        if (x == symbol):
            return Values[index]
        index += 1
 
#----------------------------------------#

def sumUsedCreditsWithTotal(credits, spinningCredits):
    return credits + spinningCredits

#----------------------------------------#

def wishToStop():
    while True:
        option = input("Wish to continue? [y/n] ")

        if (option == "n" or option == "N"):
            return True
        elif(option == "y" or option == "Y"):
            return False
        elif (option != "y", "Y", "n", "N"):
            print("just y/Y and n/N.\n")

#----------------------------------------#

def gainOrLostCredits(machine, spinningCredits):
    if (machine.sameSymbols()):
        spinningCredits *= getMultiplicationIndex(machine.leftSymbol)
        print("Congratualtions! You just won ", spinningCredits, " credits.")
        return spinningCredits
    else:
        print("Well... this is how it starts. You just lost ", spinningCredits, " credits.")
        return -spinningCredits


##########################################
##------------ Main methods ------------##
##########################################

def creditsToBeDeposited():
    while True:
        credits = input("How many credits do you wish to deposit? ")

        if(credits.isdigit() and int(credits) > 0):
            return int(credits)
        print("Nope... what I need is a number. Oh, and positive!\n")

#----------------------------------------#

def creditsToBeUsed(credits):
    while True:
        spinningCredits = input("How many credits do you wish to use? ")

        if(spinningCredits.isdigit() and int(spinningCredits) > 0):
            spinningCredits = int(spinningCredits)
            if(spinningCredits > credits):
                print("'Migo... não tens tanto guito. Escolhe lá um número mais fofinho. Ah, e positivo.")
            else:
                return spinningCredits
        else:
            print("Nope, gimme a number lad! Preferably positive. (And you can't spin for free)")

#----------------------------------------#

def machineSpinning(spinningCredits):
        machine = SlotMachine()
        machine.spin()
        printSlotMachine(machine.leftSymbol, machine.middleSymbol, machine.rightSymbol)
        spinningCredits = gainOrLostCredits(machine, spinningCredits)

        return spinningCredits

#----------------------------------------#

def spin(credits):
    while True:
        spinningCredits = machineSpinning(creditsToBeUsed(credits))
        credits = sumUsedCreditsWithTotal(credits, spinningCredits)
        printCreditsRemaining(credits)

        if (credits <= 0):
            if (credits == 0):
                print("See... you just lost everything. Told you.")
            else:
                print("Congratulations! You not only managed to lose it all, but you are now in debt!!")
            raise SystemExit

        if(wishToStop()):
            break

    return credits


##########################################
##---------------- Main ----------------##
##########################################

printTitle()
 
credits = creditsToBeDeposited()
printCreditsRemaining(credits)

while True:
    print("1 - Start spinning")
    print("2 - Show remaining credits")
    print("3 - Quit\n")

    option = input("What will it be?[1/2/3] ")

    if(option == "1"):
        credits = spin(credits)
    elif(option == "2"):
        printCreditsRemaining(credits)
    elif(option == "3"):
        raise SystemExit
    else:
        print("You gotta choose 1, 2 or 3. No way around that.\n")