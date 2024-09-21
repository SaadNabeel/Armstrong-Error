
def isarmstrong(num):
    order = len(str(num))
    sumofpowers = sum(int(digit) ** order for digit in str(num))
    return num == sumofpowers


try:
    number = int(input("Enter a number: "))
    
    if isarmstrong(number):
        print("The number is an Armstrong number.")
    else:
        raise ValueError("The number is not an Armstrong number.")
except ValueError as e:
    print("Error:", e)
