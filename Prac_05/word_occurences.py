dictionary = {}  # Initiates empty dictionary
text = input("Please input text you want checked cheers: ")
split_words = text.split()
for element in split_words:
    frequency = dictionary.get(element, 0)  # inputs element into empty dictionary
    dictionary[element] = frequency + 1  # add number if it happens more than once

words = list(dictionary.keys())  # change into list so max length can be evaluated
split_words.sort()  # Sorts by alphabetical order

max_length = max((len(word) for word in words))  # uses max function to evaluat length
for element in split_words:
    print("{} : {}".format(element.ljust(max_length), dictionary[element]))  # formats width and prints
