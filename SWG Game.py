import random

total_chance=10
you_point=0
computer_point=0
no_of_chances_left=0

three_things = ["s", "w", "g"]

while no_of_chances_left<total_chance:

    choose_by_computer = random.choice(three_things)
    print("enter only one from these: \nenter g for gun,\nenter s for snack,"
          "\nenter w for water")
    input_by_user = input()

    if choose_by_computer == input_by_user:
        print("try again!","total chance left",total_chance-no_of_chances_left)
        print("computer has choosen", choose_by_computer)

    else:
        if choose_by_computer =="s" and input_by_user =="w":
            computer_point += 1
            print(f"your guess is {input_by_user} and computer guess is {choose_by_computer}")
            print("computer wins point 1\n")
            print(f"computer wins! and your points {you_point} and "
                  f"computer points {computer_point}")
        elif choose_by_computer == "w" and input_by_user =="s":
            you_point+=1
            print(f"your guess is {input_by_user} and computer guess is {choose_by_computer}")
            print("you win point 1\n")
            print(f"you win! and your points {you_point} and "
                  f"computer points {computer_point}")

        elif choose_by_computer =="w" and input_by_user =="g":
            computer_point += 1
            print(f"your guess is {input_by_user} and computer guess is {choose_by_computer}")
            print("computer wins point 1\n")
            print(f"computer wins! and your points {you_point} and "
                  f"computer points {computer_point}")
        elif choose_by_computer =="g" and input_by_user =="w":
            you_point += 1
            print(f"your guess is {input_by_user} and computer guess is {choose_by_computer}")
            print("you win point 1\n")
            print(f"you win! and your points {you_point} and "
                  f"computer points {computer_point}")

        elif choose_by_computer =="g" and input_by_user =="s":
            computer_point += 1
            print(f"your guess is {input_by_user} and computer guess is {choose_by_computer}")
            print("computer wins point 1\n")
            print(f"computer wins! and your points {you_point} and "
                  f"computer points {computer_point}")
        elif choose_by_computer =="s" and input_by_user =="g":
            you_point += 1
            print(f"your guess is {input_by_user} and computer guess is {choose_by_computer}")
            print("you win point 1\n")
            print(f"you win! and your points {you_point} and "
                  f"computer points {computer_point}")

        print("total no of chances left", total_chance-no_of_chances_left-1, "out of ", total_chance,"\n")
        no_of_chances_left += 1

if computer_point>you_point:
    print(f"Result :"
          f"computer wins with {computer_point} points")

elif computer_point<you_point:
    print(f"Result:"
          f"you win with {you_point} points")

else:
    print(f"tie ! your points{you_point} and computer points{computer_point}")


