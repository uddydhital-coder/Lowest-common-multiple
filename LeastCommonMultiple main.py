numberSmallest = int(input("Enter Smallest number: "))
numberLargest = int(input("Enter Largest number "))

num1 = numberSmallest
num2 = numberLargest

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

gcd = numberLargest
lcm = (num1 * num2) // gcd

print("Lowest common multiple is : ", lcm)