

Studens =[]

while True:
    print("Enter The Information of Student")
    name=input("Enter Name Student: ")
    age=int(input("Enter Age Student: "))
    major=input("Enter Major Student: ")
    student = (name,age,major)
    Studens.append(student)


    another= input("Do you want to enter another student information (y/N)?")
    if another.lower() !='y':
        break

print("\nStudens:")
for x in Studens:
    print(f"Name: {x[0]},Age: {x[1]},Major : {x[2]}")
