print("Geben sie ihren Namen ein:")
name = input()
print("Hallo " + name)

print("Wie alt sind sie?")
int(age) = input()

if age > 18:
    print("Sie sind alt genug")
    print("Wie viele Kinder haben sie?")
    int(kinder) = input()
    for i in range(kinder):
        print("Kind " + i + " Name:")
        name = input()
        print("Kind " + i + " Alter:")
        age = input()
        print("Kind " + i + " Geschlecht:")
        geschlecht = input()
        print("Kind " + i + " Name: " + name + " Alter: " + age + " Geschlecht: " + geschlecht)
    
else:
    print("Sie sind noch zu jung")
    print("Wie viele Geschwister haben sie?")
    int(geschwister) = input()
    while geschwister > 0:
        print("Geschwister " + geschwister + " Name:")
        name = input()
        print("Geschwister " + geschwister + " Alter:")
        age = input()
        print("Geschwister " + geschwister + " Geschlecht:")
        geschlecht = input()
        print("Geschwister " + geschwister + " Name: " + name + " Alter: " + age + " Geschlecht: " + geschlecht)
        geschwister -= 1

print("Danke das sie mitgemacht haben")
print("Auf wiedersehen")