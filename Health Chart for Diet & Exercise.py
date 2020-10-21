import datetime

print("Please Enter: \n\n1 for Harry-\n"
      "2 for Hammad-\n"
      "3 for Rohan-")
n1=int(input())

def getdate():
    if n1 == 1:
        print("enter 1 for diet \n 2 for exercise ")
        n2 = int(input())
        if n2 == 1:
            print("1 for write and 2 for retrieve")
            n3=int(input())
            if n3==1:
                f = open("harry_diet.txt", "w")
                print("enter diet")
                diet = input()
                f.write(diet)
                return datetime.datetime.now()
            if n3==2:
                f = open("harry_diet.txt")
                content=f.read()
                print(content)
                return datetime.datetime.now()

        if n2 == 2:
            print("1 for write and 2 for retrieve")
            n3 = int(input())
            if n3 == 1:
                f = open("harry_exercise.txt", "w")
                print("enter exercise")
                exercise = input()
                f.write(exercise)
                return datetime.datetime.now()
            if n3 == 2:
                f = open("harry_exercise.txt")
                content = f.read()
                print(content)
                return datetime.datetime.now()
    if n1 == 2:
        print("enter 1 for diet \n 2 for exercise ")
        n2 = int(input())
        if n2 == 1:
            print("1 for write and 2 for retrieve")
            n3 = int(input())
            if n3 == 1:
                f = open("hammad_diet.txt", "w")
                print("enter diet")
                diet = input()
                f.write(diet)
                return datetime.datetime.now()
            if n3 == 2:
                f = open("hammad_diet.txt")
                content = f.read()
                print(content)
                return datetime.datetime.now()

        if n2 == 2:
            print("1 for write and 2 for retrieve")
            n3 = int(input())
            if n3 == 1:
                f = open("hammad_exercise.txt", "w")
                print("enter exercise")
                exercise = input()
                f.write(exercise)
                return datetime.datetime.now()
            if n3 == 2:
                f = open("hammad_exercise.txt")
                content = f.read()
                print(content)
                return datetime.datetime.now()

    if n1 == 3:
        print("enter 1 for diet \n 2 for exercise ")
        n2 = int(input())
        if n2 == 1:
            print("1 for write and 2 for retrieve")
            n3 = int(input())
            if n3 == 1:
                f = open("rohan_diet.txt", "w")
                print("enter diet")
                diet = input()
                f.write(diet)
                return datetime.datetime.now()
            if n3 == 2:
                f = open("rohan_diet.txt")
                content = f.read()
                print(content)
                return datetime.datetime.now()

        if n2 == 2:
            print("1 for write and 2 for retrieve")
            n3 = int(input())
            if n3 == 1:
                f = open("rohan_exercise.txt", "w")
                print("enter exercise")
                exercise = input()
                f.write(exercise)
                return datetime.datetime.now()
            if n3 == 2:
                f = open("rohan_exercise.txt")
                content = f.read()
                print(content)
                return datetime.datetime.now()

print(getdate())