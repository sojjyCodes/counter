number = int(input("Enter the number: "))
count = 0
while number > 0:
    count = count + 1
    number = number // 10
print("Tnumber of digit in the number are:", count)