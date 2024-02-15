def stats_decorator(func):
    """"Decorator function handles all math to be processed and prints results"""
    def wrapper(numbers):
        count = len(numbers)
        total = sum(numbers)
        average = total / count
        maximum = max(numbers)

        print("Numbers Read:", numbers)
        print("Count of the Numbers Read:", count)
        print("Average of the Numbers:", average)
        print("Maximum of the Numbers:", maximum)
    return wrapper

"""Decorate the function that handles numbers list"""
@stats_decorator
def decorate(numbers):
    pass


def printStats(t):
    """Read datat from text file"""
    with open(t, 'r') as file:
        """Iterate through each line of the text file"""
        for line in file:
            """
            Create a numbers list for the line in the text file, 
            then call the decorator function
            """
            numbers = [int(num) for num in line.strip().split()]
            decorate(numbers)


"""Provide the filename and call the function"""
filename = 'numbers.txt'
printStats(filename) 
