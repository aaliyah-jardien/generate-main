print("My weekend")
print(5 == 6)
print(5 >= 7)

num1 = 9
num2 = 8
if num1 > num2:
    print(str(num1) + " is  greater")

for i in range(100, 1, -2):
    if i == 50:
        continue
    print(i, end=", ")
print("\n")

for x in "Masimthembe":
    print(x, end="")
print("\n")

names = ["Zoe", "Lihle", "Liyah", "Masi"]
marks = [95, 63, 60, 100]
for x in range(len(names)):
    print(names[x], marks[x])


