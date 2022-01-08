import re
# Getting Candidate's Response 
# applying lower function to avoid any case sensitivity issue
candidateResponse=input("Enter candidate's response").lower()
# Getting Correct Answer
correctAnswer=input("Enter Correct answer").lower()

# Removing all characters except a-z , 0-9 and white space
candidateResponse=re.sub("[^a-z0-9\s]","",candidateResponse)
correctAnswer=re.sub("[^a-z0-9\s]","",correctAnswer)

# Convert all the input to list from string
correctAnswer=correctAnswer.split(" ")
candidateResponse=candidateResponse.split(" ")
# Create a empty list to store Candidate's Correct Answer
candidateCorrectResponse=[]

# Creating a function to calculate marks from a given list based on criteria
def calculateMarks(correctAnswer):
    totalNumber=0
    for word in correctAnswer:
        if (word.isdigit()):
            totalNumber+=4
        elif (len(word)>7):
            totalNumber+=3
        elif (len(word)<5):
            totalNumber+=0
        else:
            totalNumber+=1
    return totalNumber


# Adding Candidate's Correct words in the candidateCorrectResponse list
correctAnswerCopy=correctAnswer.copy()
for word in candidateResponse:
    if word in correctAnswer:
        candidateCorrectResponse.append(word)
        correctAnswer.remove(word)

# Calculating result
maximumPossibleScore=calculateMarks(correctAnswerCopy)
pointsScored=calculateMarks(candidateCorrectResponse)
# print(maximumPossibleScore,pointsScored)
result=(pointsScored/maximumPossibleScore)*100
print(f"Candidate got {result:.2f}% in the exam")


