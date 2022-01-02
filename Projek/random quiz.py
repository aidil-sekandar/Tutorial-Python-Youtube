from random import shuffle # use this module to use shuffle function

questions = [
["What does HTML stand for?\n\na. Hyper Trainer Marking Language\nb. Hyper Text Marketing Language\nc. Hyper Text Markup Language\nd. Hyper Text Markup Leveler","c"],
["What type of data would your name be?\n\na. string\nb. boolean\nc. integer\nd. float", "a"],
["Which of the following is NOT a mathematical operator?\n\na. +\nb. -\nc. *\nd. #", "d"],
["Which of the following is a logical operator?\n\na. and\nb. then\nc. else\nd. for", "a"],
["What is a list of steps that you can follow to finish a task?\n\na. commands\nb. coding\nc. algorithm\nd. computing", "c"],
["Third Generation Programming Language also known as ...\n\na. Assembly Language\nb. Low Level Language\nc. Binary code\nd. High level Language", "d"],
["In coding terms, a placeholder for a piece of information or values from specific data types is ...\n\na. Editor\nb. Variables\nc. if statement\nd. loops", "b"],
["In coding terms, the action of doing something over and over again is ...\n\na. if statement\nb. repeating\nc. loop\nd. while", "c"]
]
# add more questions in the same format

score = 0
turn = [0,1,2,3,4,5,6,7] #add more number according to your numbers of questions
shuffle(turn)

for i in turn:
	print(questions[i][0])
	answer = input("\n> answer? = ").lower()
	if answer == questions[i][1]:
		print("That's correct!") # change to any message you like
		score += 1
		print("[Current score] =", score, "\n")
	else:
		print("That's wrong!") # change to any message you like
		print("[Current score] =", score, "\n")

print("Your final score is", score)
print("Thank You!!!")
