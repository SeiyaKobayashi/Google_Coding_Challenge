# Check if a word in dictionary is longer than the given string
def check_if_longer(word, given):
    return len(word) > len(given)

# Check if a word in dictionary is a substring of the given string
def check_if_substring(word, given):

    # Where you are in word
    count_word = -1
    # Where you are in the given string
    count_given = -1
    # Where you are in the sliced given string
    count_given_sliced = -1
    # The number of characters of the sliced given string skipped
    count_skipped = 0

    if not check_if_longer(word, given):
        # For each character in word
        for i in word:
            count_word += 1
            # Check if any charater was skipped in the following loop
            if count_skipped == 0:
                count_given += 1
            else:
                count_given += 1 + count_skipped
                count_skipped = 0
            # Unless count_given doesn't exceed the length of the given string
            if count_given < len(given):
                # For each character in the sliced given string
                for j in given[count_given:]:
                    count_given_sliced += 1
                    # If character is found in the sliced given string, try next character of word
                    if i == j:
                        # If i is the final character in word
                        if count_word == len(word)-1:
                            return True
                        else:
                            count_given_sliced = -1
                            break
                    # If character is not found in the sliced given string after the loop ends, then it's not a substring
                    elif i != j and count_given_sliced == len(given[count_given:])-1:
                        return False
                    # If character is not found in the given string before the loop ends, try next character of given
                    else:
                        count_skipped += 1
                        continue
            else:
                return False
    else:
        return False

# Find and return the longest substring, given a certain string and a set of words
def find_longest_substring (dictionary, string):

    # Variable to store the maximum length
    max_length = 0
    # List words that have tentatively maximum length (longest one might not be only one)
    longest = []

    # For each word in dictionary
    for i in range(len(dictionary)):
        # If it's a substring
        if check_if_substring(dictionary[i], string):
            if len(dictionary[i]) > max_length:
                # Update the value of max_length
                max_length = len(dictionary[i])
                # If some indices are already stored, then reinitialize list of indices
                if len(longest) != 0:
                    longest = []
                    longest.append(dictionary[i])
                else:
                    longest.append(dictionary[i])
            elif len(dictionary[i]) == max_length:
                longest.append(dictionary[i])
            else:
                continue
        # Otherwise
        else:
            continue

    return longest

def main ():

    # Read from txt file
    f = open('sample_input.txt', 'r')
    list = f.readlines()
    list_new = []
    for line in list:
        list_new.append(line.strip('\n'))

    # The first word is S, the rest are D
    S = list_new[0]
    D = list_new[1:]

    print("\nThe given string: " + S)

        # Iterate through the list of words
    for i in range(len(D)):
        print("-------------------------------------------------------------\n")
        print("Word#" + str(i+1) + ": " + D[i])
        print("Substring? --> " + str(check_if_substring(D[i], S)))

    print("-------------------------------------------------------------\n\n")
    print("The longest substring(s) of " + "'" + S + "'" + " is(are):")

    ret = find_longest_substring(D, S)
    for j in range(len(ret)):
        print(ret[j])

    f.close()

main()
