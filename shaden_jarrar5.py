def menu():
    print("\n1- Add appointment")
    print("2- Show appointments")
    print("3- Delete appointment")
    print("4- Exit")

def add(appts):
    name = input("Enter patient name: ")
    date = input("Enter date: ")
    time = input("Enter time: ")
    appts.append((name, date, time))
    print("Added")

def show(appts):
    if len(appts) == 0:
        print("No appointments")
    else:
        for i, a in enumerate(appts, 1):
            print(i, a[0], "-", a[1], "-", a[2])

def delete(appts):
    if len(appts) == 0:
        print("No appointments to delete")
    else:
        show(appts)
        num = int(input("Enter number to delete: "))
        if 1 <= num <= len(appts):
            appts.pop(num-1)
            print("Deleted")
        else:
            print("Invalid number")

def program():
    appts = []
    while True:
        menu()
        choice = input("Choose: ")
        if choice == "1":
            add(appts)
        elif choice == "2":
            show(appts)
        elif choice == "3":
            delete(appts)
        elif choice == "4":
            break
        else:
            print("Wrong choice")

program()