print("Welcome to my computer quiz!")

playing = str(input("Do you want to play? "))

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("Whats does CPU stand for ? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is DNS? ")
if answer.lower() == "domain name system.":
    print("Correct!")
    score += 1


print("You got " + str(score) + "questions correct")
print("You got" + str(score / 4)*100 + "%.")
