#ერთიდან 100 მდე დაბეჭდეთ ყველა რიცხვი თან გვერძე მიუწერეთ ლუწია თუ კენტი  while loop ის გამოყენებით 

i = 0

while i < 101:
    if i % 2 == 0:
        print(str(i) + "even")
    else:
        print(str(i) + "odd")

    i += 1