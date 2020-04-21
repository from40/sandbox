alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"]


# decode
def decode():
    message = input("Please, input message: ")
    left_shift = int(input("Please, shift value: "))
    decoded_line = []
    for i in message:
        if i not in alphabet:
            decoded_line.append(i)
        else:
            decoded_line.append(calc_shifted_index(i, left_shift))
    new_line = "".join(decoded_line)
    print("\n", new_line, sep="")


def calc_shifted_index(letter, left_shift):
    letter_index = alphabet.index(letter)
    shifted_index = int((letter_index + left_shift) % len(alphabet))
    new_letter = alphabet[shifted_index]
    return new_letter


# code
def code():
    message = input("Please, input message: ")
    left_shift = int(input("Please, shift value: "))
    coded_line = []
    for i in message:
        if i not in alphabet:
            coded_line.append(i)
        else:
            coded_line.append(code_shifted_index(i, left_shift))
    new_line = "".join(coded_line)
    print("\n", new_line, sep="")


def code_shifted_index(letter, left_shift):
    letter_index = alphabet.index(letter)
    if letter_index < left_shift:
        shifted_index = (letter_index + (len(alphabet))) - left_shift
    else:
        shifted_index = letter_index - left_shift
    new_letter = alphabet[shifted_index]
    return new_letter


#


action = int(input(">>> '1' if code message \n>>> '2' if decode message\n\t"))
if action == 1:
    code()
elif action == 2:
    decode()
