fruits=["Strawberry","Kiwi","Mango","Apple","Banana"]
print("Fruits:",fruits)
print("First:",fruits[0])
print("Last:",fruits[-1])
fruits[1]="Peach"
print("Changed:",fruits)
fruits.insert(2,"Cherry")
print("Inserted:",fruits)
f=input("Check fruit: ")
print(f,"is in the list!" if f in fruits else f,"NOT in the list!")
fruits.sort()
print("Sorted:",fruits)
