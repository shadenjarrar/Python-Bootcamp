apps = [
    ["Ahmed", "2025-08-30", "09:00 AM"],
    ["Laila", "2025-09-01", "11:30 AM"],
    ["Mohammed", "2025-09-02", "02:00 PM"],
    ["Sara", "2025-09-05", "04:15 PM"]
]

while True:
    print("1- Add")
    print("2- Show")
    print("3- Delete")
    print("4- Exit")
    x = input("Choose: ")

    if x == "1":
        n = input("Name: ")
        d = input("Date: ")
        t = input("Time: ")
        apps.append([n, d, t])
        print("Added!\n")

    elif x == "2":
        if len(apps) == 0:
            print("No apps\n")
        else:
            for i in range(len(apps)):
                print(i+1, apps[i][0], apps[i][1], apps[i][2])
            print()

    elif x == "3":
        if len(apps) == 0:
            print("No apps\n")
        else:
            for i in range(len(apps)):
                print(i+1, apps[i][0], apps[i][1], apps[i][2])
            y = int(input("Number to delete: "))
            if 1 <= y <= len(apps):
                apps.pop(y-1)
                print("Deleted!\n")
            else:
                print("Wrong number\n")

    elif x == "4":
        break
    else:
        print("Wrong choice\n")