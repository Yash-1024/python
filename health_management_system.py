# This a health management system that records and displays Diet/Exercise routine of a patient and matches it with the one given by the doctor/phycio
from datetime import datetime


def getdate():
    import datetime
    return datetime.datetime.now()

# <-----!!!!!!!!Patient Info Section!!!!!!!!----->
textToTakeName = True
patient_name = []
with open('patient.txt', 'r') as f:
    while textToTakeName:
        textToTakeName = f.readline()
        if textToTakeName == '':
            break
        patient_name.append(textToTakeName)
        
for i in range(len(patient_name)):
    patient_name[i] = patient_name[i].replace('\n','')



# <-----@@@@@@@  DIET SECTION  @@@@@@@----->

# <-----!!!!!!!!Diet given by Doctor!!!!!!!!----->


# diet_doctor = ['','','','','']
# with open('diet given by doctor.txt', 'r') as f:
#     for i in range(5):
#         diet_doctor[i] = f.readline()
# for i in range(5):
#     diet_doctor[i] = diet_doctor[i].replace('\n','')
# # print(diet_doctor)


# # <-----!!!!!!!!diet followed by patient!!!!!!!!----->

# diet_patient = ['','','','','']
# with open('diet followed by patient.txt', 'r') as f:
#     for i in range(5):
#         diet_patient[i] = f.readline()
# for i in range(5):
#     diet_patient[i] = diet_patient[i].replace('\n','')
# # print(diet_patient)

# correct = 0
# for i in range(5):
#     if diet_patient[i] == diet_doctor[i]:
#         print(f"{patient_name[i]} has followed diet")
#         correct += 1 
#     else:
#         print(f"{patient_name[i]} has not followed diet")

# if correct != 0:
#     print(f"{correct} patient has followed the diet")
# else:
#     print("No patient has followed the diet")


# # <-----@@@@@@@  EXERSICE SECTION  @@@@@@@----->

# # <-----!!!!!!!!Exercise done by patient!!!!!!!!----->
# exercise_patient = ['','','','','']
# with open('exercise done.txt', 'r') as f:
#     for i in range(5):
#         exercise_patient[i] = f.readline()
# for i in range(5):
#     exercise_patient[i] = exercise_patient[i].replace('\n','')
# for i in range(5):
#     exercise_patient[i] = exercise_patient[i].replace('\n','')
# print(exercise_patient)

# # <-----!!!!!!!!Exercise given by Doctor!!!!!!!!----->
# exercise_doctor = ['','','','','']
# with open('exercise given.txt', 'r') as f:
#     for i in range(5):
#         exercise_doctor[i] = f.readline()
# for i in range(5):
#     exercise_doctor[i] = exercise_doctor[i].replace('\n','')
# for i in range(5):
#     exercise_doctor[i] = exercise_doctor[i].replace('\n','')
# print(exercise_doctor)

# correct = 0
# for i in range(5):
#     if exercise_patient[i] == exercise_doctor[i]:
#         print(f"{patient_name[i]} has followed Exercise routine")
#         correct += 1 
#     else:
#         print(f"{patient_name[i]} has not followed Exercise routine")

# if correct != 0:
#     print(f"{correct} patient has followed the Exercise routine")
# else:
#     print("No patient has followed the Exercise routine")


# <-----@@@@@@@  MAIN SECTION  @@@@@@@----->
def main_(name,input):
    if input == 1:
        with open(f'{name}_diet.txt', 'a') as f:
            f.write(f"{getdate()} -->  {input_()}\n")
            print("Diet registered sucessfully")
    elif input == 2:
        with open(f'{name}_exercise.txt', 'a') as f:
            f.write(f"{getdate()} -->  {input_()}\n")
            print("Exercise registered sucessfully")
    elif input == 3:
        get_(f'{name}',f'{name}_diet.txt')
    elif input == 4:
        get_(f'{name}',f'{name}_exercise.txt')
    else:
        print("Error occured")

def input_():
    diet_taken = input("Enter what u had: ")
    return diet_taken

def get_(name,file_name):
    with open(f'{file_name}', 'r') as f:
        textToTakeDiet = True
        if f.read() == '':
            print(f"No record found for {name}")
        while textToTakeDiet:
            textToTakeDiet = f.readline()
            time = textToTakeDiet[0:26:1]
            diet = textToTakeDiet[32::1] 
            if textToTakeDiet == '':
                break
            print(f"{name} had {diet} at {time}")
    

# <-----@@@@@@@  USER SECTION  @@@@@@@----->

Doctor_or_viewer = input("Are u a Doctor(d) or Patient(p): ")

print("Choose from a patients given name given below:")
for i in range(len(patient_name)):
    print(f"{i+1}--> {patient_name[i]}")
try:
    patient = int(input())
except ValueError as e:
    print("Enter a valid value in Integer in the given range")

if Doctor_or_viewer == 'd':
    pass
else:
    try:
        diet_Or_Exercise = int(input("What do u wish to do\n1-->Register Diet\n2-->Register Exercise\n3-->Get diet information\n4-->Get exercise information\n"))
    except ValueError as e:
        print("Enter a valid value in Integer in the given range")

    if patient == 1:
        main_(f'{patient_name[0]}',diet_Or_Exercise)
    elif patient == 2:
        main_(f'{patient_name[1]}',diet_Or_Exercise)
    elif patient == 3:
        main_(f'{patient_name[2]}',diet_Or_Exercise)
    elif patient == 4:
        main_(f'{patient_name[3]}',diet_Or_Exercise)
    elif patient == 5:
        main_(f'{patient_name[4]}',diet_Or_Exercise)
    else:
        print("Error")

# print(getdate())