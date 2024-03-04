import random
randnum = random.randrange(1000, 10000)
n = int(input("Enter a number:"))
if (randnum == n):
    print("You got it right at first try. You are a Mastermind")
else:
    ctr=0
    while(randnum!=n):
        ctr += 1
        cnt = 0
        randnum = str(randnum)
        n = str(n)
        correct = []
        for i in range(0,4):
            if (n[i] == randnum[i]):
                cnt += 1
                correct.append(n[i])
            else :
                continue
        if (cnt<4) and (cnt!=0):
            print("You got",cnt,"correct digits")
            print("Correct numbers are: ")
            for j in correct:
                print(j,end=" ")
            n = int(input("\nEnter the number:"))
        elif (cnt == 0):
            print("No input matched")
            n=int(input("Enter the number:"))
    if n == randnum:
        print("You are a Mastermind")
        print("It took you only ",ctr, "tries.")