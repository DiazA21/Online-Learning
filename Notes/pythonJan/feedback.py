import os
from datetime import date
#Get List of users
numberOfStudents = int(input("How many students are on the course: "))
studentList = [0] * numberOfStudents


scoreMap = {
    '1': "poor",
    '2': "fair",
    '3': "good",
    '4': "very good",
    '5': "excellent"
}


directoryName = input("Folder name: ")


# Check studentList has been populated then create folder for feedback on todays date
if len(studentList) > 0 and not os.path.exists(directoryName):
    try:
        os.makedirs(directoryName)
    except PermissionError:
        print(f"Permission denied: Unable to create '{directoryName}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


i=0
while i < numberOfStudents:
    studentList[i] = input("Student name: ")
    
    #Create File or return error if already exists
    try:
        studentFile = open(f"{directoryName}/{studentList[i]}Feedback.txt", 'x')
    except FileExistsError as error:
        print(error)
        print("\n\nFile already exists, check if this student's feedback has already been created previously or has a duplicate name")
        continue
    except Exception as error:
        print(f"an error has occurred: {error}")


    #Get values for feedback (1-5)
    understandingLevel = input("Understanding level (1 poor to 5 excellent): ")
    contributionLevel = input("Contribution level: ")
    labCompletionLevel = input("Lab Completion level: ")
    engagementLevel = input("Engagement level: ")
    punctualityLevel = input("Punctuality level: ")


    #Define templates
    generalComment = f"General Comments:\n\n{studentList[i]} demonstrated {scoreMap[understandingLevel]} understanding throughout the course, reflecting their grasp of the material and the subject.\n {studentList[i]}'s completion of labs was {scoreMap[labCompletionLevel]}.\n\n"
    engagementComment = f"Learner Punctuality and Engagement:\n\n{studentList[i]} showed {scoreMap[punctualityLevel]} punctuality and {scoreMap[engagementLevel]} engagement with the material. {studentList[i]} gave {scoreMap[contributionLevel]} amounts of contribution to group discussions."


    #Write to file
    try:
        studentFile.write(generalComment)
        studentFile.write(engagementComment)
        studentFile.close()
    except Exception as error:
        print(error)


    #Open File
    os.startfile(f"{directoryName}\{studentList[i]} Feedback.txt")
    i = i + 1