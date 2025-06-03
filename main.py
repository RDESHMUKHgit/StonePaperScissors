import random
import time
import sys

# Typing effect
def type_writer(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ASCII Art
stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_art = [stone, paper, scissors]
choices = ["Stone ✊", "Paper ✋", "Scissors ✌"]

# Game Intro
type_writer("👾 Welcome to Rock, Paper, Scissors Battle! 🎮")
print("-" * 40)

# Score Tracking
user_score = 0
computer_score = 0
rounds_played = 0

# Main Game Loop
while True:
    print("\nChoose your weapon:")
    print("0 - Stone ✊\n1 - Paper ✋\n2 - Scissors ✌")

    try:
        user_choice = int(input("Enter your choice (0/1/2): "))
        if user_choice not in [0, 1, 2]:
            raise ValueError
    except ValueError:
        print("❌ Invalid input! Please enter 0, 1, or 2.")
        continue

    computer_choice = random.randint(0, 2)
    rounds_played += 1

    print(f"\n🧍‍♂️ You chose: {choices[user_choice]}")
    print(ascii_art[user_choice])
    time.sleep(0.5)
    print(f"🤖 Computer chose: {choices[computer_choice]}")
    print(ascii_art[computer_choice])
    time.sleep(0.5)
    type_writer("Calculating the result...")
    time.sleep(2)

    # Outcome logic
    if user_choice == computer_choice:
        print("😐 It's a DRAW!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("🎉 YOU WIN this round!")
        user_score += 1
    else:
        print("💀 COMPUTER WINS this round!")
        computer_score += 1

    # Display current score
    print(f"\n🔢 SCORE after {rounds_played} round(s): You {user_score} \n {computer_score} Computer")

    # Ask to play again
    play_more = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if play_more in ["yes", "y"]:
        continue  # Go to next round
    else:
        # Exit the game
        type_writer("\n🎮 Thanks for playing!")
        type_writer(f"🏁 Final Score: You {user_score} - {computer_score} Computer")
        if user_score > computer_score:
            type_writer("🏆 YOU WIN OVERALL! 🎊")
        elif user_score < computer_score:
            type_writer("🤖 Computer wins overall! Better luck next time.")
        else:
            type_writer("It's a TIE overall! What a match. 🤝")
        break


input("Press Enter to exit...")