from adafruit_circuitplayground import cp
import time
import random

T1 = 5
TimeLimit = T1
high_score = 0  # Variable to track the highest score

# The main actions of the game
actions = ["A", "B", "pad", "shake"]

# Lights the LEDs with the designated color
def lights(color, t=0.5):
    cp.pixels.fill(color)
    time.sleep(t)
    cp.pixels.fill((0, 0, 0))

# Gives a prompt (from the actions list)
def instruction(action):
    if action == "A":
        cp.play_tone(440, 0.2)
        print("PRESS A")
    elif action == "B":
        cp.play_tone(660, 0.2)
        print("PRESS B")
    elif action == "pad":
        cp.play_tone(880, 0.2)
        print("TOUCH A PAD")
    elif action == "shake":
        cp.play_tone(1040, 0.2)
        print("SHAKE IT")

# The main game function
def maingame():
    global totpoints, TimeLimit, high_score
    totpoints = 0  # Reset total points for a new game
    TimeLimit = T1  # Reset time limit for a new game
    playing = True

    while playing:
        action = random.choice(actions)
        instruction(action)
        starttime = time.monotonic()

        while time.monotonic() - starttime < TimeLimit:
            if action == "A" and cp.button_a:
                lights((0, 255, 0))
                print("CORRECT")
                totpoints += 1
                TimeLimit = max(1, TimeLimit * 0.9)
                break
            elif action == "B" and cp.button_b:
                lights((0, 255, 0))
                print("CORRECT")
                totpoints += 1
                TimeLimit = max(1, TimeLimit * 0.9)
                break
            elif action == "pad" and (cp.touch_A1 or cp.touch_A2 or cp.touch_A3 or cp.touch_A4 or cp.touch_A5 or cp.touch_A6):
                lights((0, 255, 0))
                print("CORRECT")
                totpoints += 1
                TimeLimit = max(1, TimeLimit * 0.9)
                break
            elif action == "shake" and cp.shake(shake_threshold=10):  # Adjusted threshold for higher sensitivity
                lights((0, 255, 0))
                print("CORRECT")
                totpoints += 1
                TimeLimit = max(1, TimeLimit * 0.9)
                break
        else:
            lights((255, 0, 0))
            print("GAME OVER")
            cp.play_file("gameover.wav")
            playing = False

    if totpoints > high_score:  # Update high score if necessary
        high_score = totpoints
        print("NEW HIGH SCORE!")

    print(f"FINAL SCORE: {totpoints}")
    print(f"HIGH SCORE: {high_score}")

# Plays audio files before and after the game starts
print("Welcome to the Bop It: CPX Edition! Press A to Start.")
cp.play_file("start.wav")
while True:
    if cp.button_a:
        print("Game Started!")
        cp.play_file("gamestarted.wav")
        maingame()
        print("Do you want to try again? A for Yes and B for No")
    if cp.button_b:
        print("Ending the game. Goodbye!")
        cp.play_file("goodbye.wav")
        break
