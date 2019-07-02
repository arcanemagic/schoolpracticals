import perfect

n = int(input("Enter number: "))
d = {1:perfect.GenerateFactors(n), 2:perfect.isPrimeNo(n), 3:perfect.isPerfectNo(n)}

try:
    choice = int(input("Choose 1 to see factors of number:\nChoose 2 to check if number is prime:\nChoose 3 to check if number is perfect:\n"))
except:
    print("Invalid choice!")

print(d[choice])
