print("Welcome to GC mini golf!")
name = input("What is your name? ")

while True:
    holes = input('Would you like to play 3 or 6 holes today? ')
    if holes == "3" or holes == "6": break
    else:
        print("Invalid input. Please choose either 3 or 6 holes.")

num_holes = int(holes)
total_score = 0
print(f"\n{name}, get ready to play {num_holes} holes of mini golf!\n")
for hole in range(1, num_holes + 1):
    score = 0
    while True:
        try:
            score = int(input(f"How many putts for {hole}? (par is 3)"))
            if score < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    total_score += score

total_par = num_holes * 3
score_difference = total_score - total_par
print(f"\n{name}, your total score for {num_holes} holes is {total_score}!")

if score_difference > 0:
    print(f"Nice try, {name}... Your total score was: + {score_difference}.")
elif score_difference < 0:
    print(f"Great job, {name}! Your total score was: {score_difference}.")
else:
    print(f"Good game, {name}! Your total score was: {score_difference}.")


