
def getInput(moves,room):
    directions = ["North","South","East","West"]
    destinations = moves[room]
    possiblemoves = []
    index = 0
    print "Rooms:",
    for i in destinations:
        if i!=-1:
            print directions[index],
            possiblemoves.append(directions[index])
        index +=1
    print "\n"
    userinput=""
    while userinput not in possiblemoves:
        userinput=raw_input("Where do you want to go? ")
        print  "                             ______________    "
        print  "                            |              |    "
        print  "                            |     Gate     |    "
        print  "                            |______________|    "
        print  "                           /     |   |      \    " 
        print  "                          /Guards| 1 |Guards \   "
        print  "                         / place[]   []place  \    "
        print  "                        /________|_[]|_________\    "
        print  "                       /        /  2  \         \     "
        print  "                      /Weaponry[]      \         \     "
        print  "                     /________/___[]____\  Hall   \              /\    "
        print  "                    |Guest's  |  Main   |          |             ||     "
        print  "                    |room    []  Hall   []         |           NORTH     "
        print  "                    |_________|___[]____|__________|     <=WEST#####EAST=>     "
        print  "                    |      |  \    3    /          |           SOUTH       "
        print  "                    |Safe  |  []       []          |             ||    "
        print  "                    |room [] 4  \_[]__/    Horse   |             \/      "
        print  "                     \     |    /| 5 |\    Stable  /   "
        print  "                      \     \  / |   | \          /     "
        print  "                       \     \/__|[]_|__\        /     "
        print  "                        \    |           |      /     "
        print  "                         \   |  #Frozen# |     /     "
        print  "                          \  |  #Sword#  |    /    "
        print  "                           \_|___________|___/     "
        print  "                      Copyright DeadElectron 2012 "
    return directions.index(userinput)

def main():

    rooms = [ "The Old Gate....last time I saw it, it was locked.....now it's open.",
              "Well, two guard's rooms",
              "Only bones and skulls have left. I better be careful for goblins...",
              "Ohh there is a goblin(level 1) inside!!!",
              "The first entrance of the Castle.",
              "These weapons are old and dusty. An elixir is on the table",
              "The big Main Hall. It's not what it used to be...",
              "These people are dead since that night. All of them...or maybe not...a zombie(level 1) just attacked you!!!",
              "The Hall is empty.",
              "The last entrance of the castle.",
              "Ohhh dear Lord of Ice!!! Spider(level 10) just attacked you!!!",
              "Goblins(level 2) are guarding the safe room!!!",
              "The GOLD KEY for the Sword room is found!!!",
              "Spiders(level 2) guards are attacking you!!!",
              "I found the Sword!!!This Sword will help me to save my people from these evil creatures!!!Let the battle begin!!!"]             

    #
    # The following list contains lists :)
    # The list's index denotes the current room.
    # Each single list contains four numbers:
    # First number -> Destination room if North (0)
    # Second number -> Destination room if South(1)
    # Third number -> Destination room if East (2)
    # Fourth number -> Destination room if West (3)
    #
    # Destination is set to -1 if it does not exist
    #

    moves = [   [-1,1,-1,-1],
                [0,4,3,2],
                [-1,-1,1,-1],
                [-1,-1,-1,1],
                [1,6,-1,5],
                [-1,-1,4,-1],
                [4,9,8,7],
                [-1,-1,6,-1],
                [-1,-1,-1,6],
                [6,13,10,11],
                [-1,-1,-1,9],
                [-1,-1,9,12],
                [-1,-1,11,-1],
                [9,14,-1,-1],
                [13,-1,-1,-1]]

   
    winrooms = [ 14 ]

    silver_keyroom =  [ 7 ]

    gold_keyroom = [ 12 ]

    goblins_rooms = [ 3,7,11,13,10 ]

    level_1 = [ 3,7 ]

    level_2 = [ 11,13 ]

    level_10 = [ 10 ]

    elixir_room = [ 5 ]

    room = 0
   
    silver_key = 0
    gold_key = 0

    King_life = 100
    King_exp = 0
    King_level = 1
    
    
    print "King Trabber GAME"
    print "=============="

    print "Ten years have passed, since the evil creatures invaded our homeland."
    print "The killed villagers, men, women and children."
    print "They killed our King, my father."
    print "A completely massacre. Their goal was to steal the Frozen Sword."
    print "I remember the night when they attacked and tried to take the Sword from our peaceful castle."
    print "They managed to enter the sacred room, but when they touched the sword suddenly the ultimate power of ice woke up and a huge and bright lightning killed them all."
    print "After that, we were forced to abandon our land."
    print "It is said that, today it is captured by goblins and other beasts."
    print "Now it’s time to save my own kingdom and fight against the evil."
    print "I, King Trabber, have to take the Frozen Sword and protect my people!!!\n"
    
    
    while True:
        #print rooms[room]
        
        if room in winrooms:
            if gold_key == 1:
                print rooms[room]
                print "You found the sword!!\nYou won!"
                return
            else:
                print "The door is locked. You must find the key."
                print "King's life: ",King_life,"%"
                print "King's level: ",King_level
                

        elif room in elixir_room:
            print rooms[room]
            if rooms[room] != "Cleared":
                King_life = King_life + 50
                King_exp = King_exp + 30
                print "You found a health potion!!!"
                rooms[room] = "Cleared"
            
        elif room in goblins_rooms:
            print rooms[room]
            if King_life >=1:
                if room in level_1:
                    King_exp = King_exp + 30
                    King_life = King_life - 10
                elif room in level_2:
                    King_exp = King_exp + 40
                    King_life = King_life - 20
                else:
                    King_life = King_life - 500

                if King_exp >=25 and King_exp <= 50:
                    King_level = King_level + 1
                    print "You gained level!!!"
                elif King_exp >=51 and King_exp <= 80:
                    King_level = King_level + 1
                    print "You gained level!!!"
                elif King_exp >=81 and King_exp <= 110:
                    King_level = King_level + 1
                    print "You gained level!!!"
                rooms[room] = "Cleared"
                goblins_rooms.remove(room)
                
        elif room in gold_keyroom:
            print rooms[room]
            print "King's life: ",King_life,"%"
            print "King's level: ",King_level
            rooms[room] = "Cleared"
            gold_key = 1
            
        else:
            print rooms[room]
            
            print "King's life: ",King_life,"%"
            print "King's level: ",King_level
            rooms[room] = "Cleared"
            
        if King_life <=0:
                print "Your king is DEAD!!!"
                return

        direction = getInput(moves, room)
        destinations = moves[room]
        room = destinations[direction]

            
# Start program
if __name__ == "__main__":
    main()
        


