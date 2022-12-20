print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1=name1.lower()
name2=name2.lower()
name=name1+name2
count1=name.count("t")+name.count("r")+name.count("u")+name.count("e")
count2=name.count("l")+name.count("o")+name.count("v")+name.count("e")
lovescore=int(str(count1)+str(count2))
if lovescore<10 or lovescore>90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore<50 and lovescore>40:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")
