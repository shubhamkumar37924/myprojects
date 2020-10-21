
number= 25
no_of_guesses = 10

i=1
while 1:
    inp_number = int(input("enter the number for guess\n"))

    if inp_number == number:
        print("you have entered the correct number and you won\n ")
        print("number of guesses left", no_of_guesses - i)
        print("you won in", i,"attempt")
        break

    elif inp_number>number:
        print("input small number than the inputed number\n ")
        print("number of guesses left", no_of_guesses - i)
    else:
        print("input big number than the inputed number\n ")
        print("number of guesses left", no_of_guesses - i)

    i+=1