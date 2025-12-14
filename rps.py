
import random

print("1) 🪨")
print("2) ✂️")
print("3) 📄")
print()

play_again = "yes"

while play_again.lower() == "yes":

    player_input = input("pick a number: ")
    if player_input == "":
        print("please pick a number between 1-3")
    else:
        player = int(player_input)
        
        if player < 1 or player > 3:
            print("wrong number, pick a number between 1-3: ")
        else:
            Computer = random.randint(1,3)
            
            print("you picked: ", player)
            print("computer picked: ", Computer)

            if player == Computer:
                print("Tie!")
            else:
                if player == 1 and Computer == 2:
                    print("you win")
                else:
                    if player == 2 and Computer == 3:
                        print("you win")
                    else:
                        if player == 3 and Computer == 1:
                            print("you win")
                        else:
                            print("computer wins")
                    
            play_again = input("play again? yes/no ")
            if play_again == "no":
                print("game over")





                



                










    




