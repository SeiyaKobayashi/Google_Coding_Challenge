# Decompress the given sequence of numbers and characters
def Decompress(sequence):
    """
    offset: Where you are in the given sequence
    ret: Resulting string
    offset_and_ret: List consists of offset and ret that each recursive function returns
    ret_nest: Resulting string from a recursive call
    digits: Number of digits before each "["
    num_rep: Number of times each string should repeat
    """
    ret, num_rep = "", ""
    offset_and_ret, ret_nest = [], []
    offset, digits = 0, 0

    while offset < len(sequence):

        # If it's "[", call itself given the offset
        if sequence[offset] == "[":
            ret_nest = Decompress(sequence[offset+1:])
            # Calculate the number before "["
            while digits > 0:
                num_rep += sequence[offset-digits]
                digits -= 1
            # Deal with edge cases such as a[]b
            if num_rep != "":
                times = int(num_rep)
                # Update ret given the number of repetitions
                ret += ret_nest[1] * times
            # Update the offset (+1 is for "]")
            offset += ret_nest[0] + 1
            # If the sequence ends with "]"
            if offset == len(sequence)-1:
                return ret
            # Otherwise, reset each variable
            else:
                ret_nest = []
                digits = 0
                num_rep = ""

        # If it's "]", return ret
        elif sequence[offset] == "]":
            # Set first element of returning list to offset
            offset_and_ret.append(offset)
            # Set second element of returning list to string
            offset_and_ret.append(ret)
            return offset_and_ret

        # If it's a number, update digits.
        # --> e.g.) If the given sequence is "10[abc]," digits has to be "2" before the recursive call
        elif sequence[offset].isnumeric():
            digits += 1

        # If it's a character, append it to the returning string
        else:
            ret += sequence[offset]
            # Deal with a sequence that ends with a character (e.g. "abc" or 3[xy]z)
            if offset == len(sequence)-1:
                return ret

        # Update offset
        offset += 1

def main():

    # Read from txt file
    f = open('sample_input.txt', 'r')
    list = f.readlines()
    list_new = []
    for line in list:
        list_new.append(line.strip('\n'))

    # Iterate through the list of sequences
    for i in range(len(list_new)):
        print("-------------------------------------------------------------\n")
        print("Input(Compressed string)#" + str(i+1) + ": " + list_new[i])
        print("Output(Decompressed string)#" + str(i+1) + ": " + Decompress(list_new[i]))

main()
