
print("Hello user please enter your name"); #Problem 1
x = input();
print("Greetings " + x + ".");


print("Please enter an integer value"); #Problem 2
y = input();
if ((int(y) % 2) == 0):
    print("EVEN");
else:
    print("ODD");


list = [];
print("Enter 10 integer values"); #Problem 3
for i in range(0,10):
    print("Enter an integer");
    list.append(input());
z = list[0];
for i in range(0,len(list)):
    if (int(list[i]) > int(z)):
        z = list[i];
print("The largest integer you entered was " + z);


olist = [];
print("Enter 10 integer values"); #problem 4
for i in range(0,10):
    print("Enter an integer")
    olist.append(input());
a = False;
b = olist[0];
for i in range(0, len(olist)):
    if ((int(olist[i]) % 2) == 1):
        b = olist[i];

for i in range(0, len(olist)):
    if ((int(olist[i]) % 2) == 1):
        a = True;
        if (int(olist[i]) > int(b)):
            b = olist[i]
if (a == True):
    print("The largest odd integer entered was " + b)
else:
    print("No odd numbers were entered")










