fruits = {
    "apple": 5,
    "banana": 3,
    "orange": 4,
    "mango": 7
}

fruit_name = input("Enter a fruit name: ")

if fruit_name in fruits:
    print("The price is", fruits[fruit_name])
else:
    print("Sorry, this fruit is not available")