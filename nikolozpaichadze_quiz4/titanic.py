# N1 females gamotvla


female = 0

with open("titanic.txt") as f1:
    next(f1)
    for line in f1:

        sex = line.strip().split(",")[4]

        if sex == "female":
            female += 1




print(female)

# N2 male

male = 0

with open("titanic.txt") as f1:
    next(f1)
    for line in f1:
        sex = line.strip().split(",")[4]

        if sex == "male":
            male += 1

print(male)

# N3 female not survived

female = 0
not_survive = 0
survived1 = 0


with open("titanic.txt") as f1:
    next(f1)
    for line in f1:
        sex = line.strip().split(",")[4]
        survived = line.strip().split(",")[1]

        if sex == "female":
            female += 1
            if survived == "0":
                not_survive += 1
            elif survived == "1":
                survived1 += 1



print(not_survive, survived1,)

# N4

male = 0
not_survive = 0
survived1 = 0

with open("titanic.txt") as f1:
    next(f1)
    for line in f1:
        sex = line.strip().split(",")[4]
        survived = line.strip().split(",")[1]

        if sex == "male":
            male += 1
            if survived == "0":
                not_survive += 1
            elif survived == "1":
                survived1 += 1


print(not_survive, survived1)

# N5

pcclass_1 = 0
pcclass_2 = 0
pcclass_3 = 0


with open("titanic.txt") as f1:
    next(f1)
    for line in f1:
        Class = line.split(",")[2]
        if Class == "1":
            pcclass_1 += 1
        elif Class == "2":
            pcclass_2 += 1
        elif Class == "3":
            pcclass_3 += 1

print(pcclass_1, pcclass_2, pcclass_3)

# N6
# pcclass_1 = 0
# pcclass_2 = 0
# pcclass_3 = 0
#
#
# with open("titanic.txt") as f1:
#     next(f1)
#     for line in f1:
#         Class = line.split(",")[2]
#         fare =
#         if Class == "1":
#             pcclass_1 += 1
#
#         elif Class == "2":
#             pcclass_2 += 1
#         elif Class == "3":
#             pcclass_3 += 1
#
# print(pcclass_1, pcclass_2, pcclass_3)


# dict = {
#         'passenger_ammount':{
#             'female': 314
#
#             }
#
#         }


# teoria

# 1) read mode, write mode, append mode, read/write mode, append/read mode
# 2) ახალი ფაილი შეიქმნება








