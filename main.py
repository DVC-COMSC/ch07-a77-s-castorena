
num1 = list(map(int, input("Enter the first list: ").split()))
num2 = list(map(int, input('Enter second list: ').split()))

# ******************************
# Make your Code
# ******************************
num3 = []
for i in range(len(num1)):
    num3.append(num1[i])
    num3.append(num2[i])
for i in range(len(num1),len(num2)):
    num3.append(num2[i])

print (num3) 
