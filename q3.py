def wordCount(t):

    """Create an empty dictionary"""
    word_line = {}

    """Open the file and read contents line by line"""
    with open(t, 'r') as file:
        """Save line number"""
        line_number = 1

        """"Loop through lines in file"""
        for line in file:
            """"Split every word in line  and create a list of each word with whitespaces erased"""
            words = line.strip().split()
            for word in words:
                """"
                Loop through list and check if it is in the dictionary.
                If it is, add the word as a key and the line number to 
                the value list. Else if the line number is not in the
                value list for the word, add the line number to the list.
                """
                if word not in word_line:
                    word_line[word] = [line_number]
                elif line_number not in word_line[word]:
                    word_line[word].append(line_number)

            """Increment line number"""
            line_number += 1
    return word_line


"""Set the filename and call the function"""
filename = 'wordcount.txt' 
word_occurrences = wordCount(filename)

""""Loop through key value pairs in word_occurrences list and print the key, value list"""
for word, occurrences in word_occurrences.items():
    print(f"{word}: {occurrences}")
