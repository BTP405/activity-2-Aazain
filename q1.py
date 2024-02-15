
def getPrimeNumbers(n):
    """
    Function returns a list of integers that are prime numbers. 
    This is calculated using the provided int n and prime numbers are 
    checked using the check_prime function
    """
    return [n for n in range(2, n+1) if check_prime(n)]


def check_prime(n):
    """
    Function checks if int n is a prime number through if statements
    then checks using a for loop to check each number within a given range(n)
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


"""
num variable takes a integer input from the user then calls and prints the function 
getPrimeNumbers with the input as the parameter
"""
num = int(input("Enter a number to find all prime numbers up to it: "))
prime_list = getPrimeNumbers(num)
print("Prime numbers: ", prime_list)

