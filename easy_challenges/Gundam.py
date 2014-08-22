#object = [x, y, z, name, armor rating, weapon 1]

user= [100, 100, 100, "Wing Zero", 250, 50]

mothership=[100, 100, 50, 'mothership']
enemy1 = [100, 100, 105, "leo1", 100, 20]
enemy2 = [100, 100, 110, "leo2", 100, 20]
enemy3 = [100, 100, 115, "leo3", 100, 20]


nearbyships=[] #List of ships by player for printing purposes
truenearbyships=[]#List of ships near player for calculating purposes
listofships=[mothership, enemy1, enemy2, enemy3] #Overall ships in game

target = 'r'#Placecholder var

def radar(listofships, user):
                for i in listofships:
                    if user[0] + 50 > i[0] and user[1] + 50 > i[1] and user[2] + 50 > i[2]:
                        nearbyships.append("space object (%s) detected at coordinates (%s, %s, %s)" % (i[3], i[0], i[1], i[2]))
                        truenearbyships.append(('%s') % (i[3]))
                    else:
                        print('no ships detected')
                        


def target(ship, user):
    print("You target ship")



while(True):
    print('\n Current coordinates: (%s, %s, %s)' % (user[0], user[1], user[2]))

    i=str(raw_input())
    if i == 'radar':
        radar(listofships, user)
        for i in nearbyships:
            print(i)
        nearbyships=[]
        

    elif i == 'l':
        print("You are sitting in a Leo cockpit")

    elif i == 'nearby':
        print(truenearbyships)

    elif 'target' in i:
        radar(listofships, user)
        targetlist=i
        targetlist=targetlist.split()
        
      #  target list is text taken from player input 'target object'. targetlist[-1] is the space object in game

      

        if targetlist[-1] in truenearbyships:
            print("You begin locking in on %s space object" % (i[-1]))
            print('target confirmed')
            currenttarget=targetlist[-1]
        else:
            print('ship not detected')


    elif i == 'fire weapon1':
        if currenttarget:
             print("You fire your buster rifle at %s and hit it directly" %(currenttarget)) #Insert probability of hit and damage
        
        else:#Check if there is a target set
            print("You are not targeting anything")
            


    else:
        print("Please input a valid command from the manual below \n'radar'\n'target (object)'")


#Movement system? Timed flight
#Combat
#Hyperspace
#multiple people
#Docking
