#2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ ყველა ლუწი რიცხვი 


num = int(input("enter a num: "))

for i in range(1, num):
    if i % 2 == 0:
        print(i)