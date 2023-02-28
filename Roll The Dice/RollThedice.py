

n = random.randint(1 , 6)

i = input("For throw dice type yes:")
b = i.lower()
c= 1
if b == "yes":
    c= 1
else:
    c = 0

while c>0:
    n = random.randint(1, 6)
    print(n)

    i = input("again:")
    b = i.lower()
    c = 1
    if b == "yes":
        c = 1
    else:
        c = 0




