import random
import sys
# Only Option for both player & CPU
Hand_options = ["Rock", "Paper" , "Scissors"]
print("Lets play a game of Rock Paper or scissors.")

def Play():
    CPU_option = random.choice(Hand_options)
    player_option = str(input("\nRock, paper, or scissors? (N) to exit.\n"))
    #No need for Player check. If it doesn't meet the Case, then it won't be accepted.

    #Check for shared choices by the player and CPU
    if player_option == CPU_option:
        print("Try Again , we're the same!")
        return

    # Case match player against the CPU's option. the If statement reads as follow:
    # [X will happen] if [this is True] else [the following will happen instead]
    match player_option.capitalize():
        case "Rock":
            result = "You Lose. I had Paper" if CPU_option == "Paper" else "You Win. I had Scissors"
        case "Paper":
            result = "You Lose. I had Scissors" if CPU_option == "Scissors" or "Scissor" else "You Win. I had Rock!"
        case "Scissors":
            result = "You Lose. I had Rock" if CPU_option == "Rock" else "You Win. I had Paper!"
        case "Scissor":# For the Non-Plural of Scissor(s).
            result = "You Lose. I had Rock" if CPU_option == "Rock" else "You Win. I had Paper!" 
        case "N":
            sys.exit()
        case _ :
            result = player_option + '? Try again.'
    print(result)
    return

while True:
    Play()
