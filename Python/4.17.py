import random

def gather_Information():
    #User information:
    user = int(input("scissor(0), rock(1), paper(2): "))
    npc = random.randint(0,2)
    return user, npc
    
def calculate_Winner(user, npc):
  
    
    if user == 0 and npc == 0:
        print( "The computer is scissor. You are scissor too. It is a draw.")
        return 0
    elif user == 0 and npc == 1:
        print( "The computer is rock. You are scissor. You lose")
        return -1 
    elif user == 0 and npc == 2:
        print( "The computer is paper. You are scissor. You win (;")
        return 1

    
    elif user == 1 and npc == 0:
        print( "The computer is scissor. You are rock. You win")
        return 1
    elif user == 1 and npc == 1:
        print( "The computer is rock. You are rock. It is a draw.")
        return 0
    elif user == 1 and npc == 2:
        print( "The computer is paper. You are rock. You lose.")
        return -1


    elif user == 2 and npc == 0:
        print( "The computer is scissor. You are paper. You lose")
        return -1
    elif user == 2 and npc == 1:
        print( "The computer is rock. You are paper. You win")
        return 1
    elif user == 2 and npc == 2:
        print( "The computer is paper. You are paper too. Draw")
        return 0

def no_winner(user_score,npc_score):

    
    if user_score == 3:
        print("Game over\nUser wins!")
        return False
    elif npc_score == 3:
        print("Game over\nNPC wins!")
        return False
    else:
        return True
    

def main():
    
    user_score = 0
    npc_score = 0
    score = 0
    
    while no_winner(user_score,npc_score) == True:
        score = 0
        user, npc = gather_Information()
        score = calculate_Winner(user, npc)

        if score == 1:
            user_score += 1
        elif score == -1:
            npc_score +=1
        
        



if __name__ == '__main__':
    main()
