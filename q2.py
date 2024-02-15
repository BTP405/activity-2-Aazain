import matplotlib.pyplot as plt

def graphSnowfall(t):
    """
    snowfall ranges stored in a dictionary with starting values of 0
    """
    snowfall_ranges = {
        '0-10': 0,
        '11-20': 0,
        '21-30': 0,
        '31-40': 0,
        '41-50': 0
    }

    with open(t, 'r') as file:
        """
        opens a file(t) as file. Loops through each line
        and deletes white spaces around each value. If the line
        exists, using if else statements, the range that the value
        belongs in is incremented by 1.
        """
        for line in file:
            line = line.strip()
            if line:
                try:
                    snow = int(line)
                    if snow >= 0 and snow <= 10:
                        snowfall_ranges['0-10'] += 1
                    elif snow >= 11 and snow <= 20:
                        snowfall_ranges['11-20'] += 1
                    elif snow >= 21 and snow <= 30:
                        snowfall_ranges['21-30'] += 1
                    elif snow >= 31 and snow <= 40:
                        snowfall_ranges['31-40'] += 1
                    elif snow >= 41 and snow <= 50:
                        snowfall_ranges['41-50'] += 1
                except ValueError:
                    print("Data Invalid")

    """
    Create variables ranges and occurences which store the
    keys(range) and values from snowfall_range
    """
    ranges = list(snowfall_ranges.keys())
    occurences = list(snowfall_ranges.values())

    """
    x and y values for each bar is set. The title, and labels for the
    x and y axis are set, then the chart is show.
    """
    plt.bar(ranges, occurences)
    plt.title('Snowfall Accumulation')
    plt.xlabel('Range (cm)')
    plt.ylabel('Occurrences')
    plt.show()

"""call function and provide file name"""
graphSnowfall('snowfall.txt')
