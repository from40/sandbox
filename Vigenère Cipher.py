alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"]

import sys # to exit program (line 33)




def main(): # define terminal size, user menu, promt user input and call procedure according user choice

    # define terminal size
    import os
    os.system("mode con cols=57 lines=35")
    os.system('COLOR 02')

    # user menu
    import shutil # to get size of the terminal (to center print output)
    columns = shutil.get_terminal_size().columns
    print("~"*57)
    print("~" + "Vegenere Cypher options:".center(columns-2) + "~")
    print("~" + "".center(columns-2) + "~")
    print("~   > Enter '1' to code message\t\t\t\t~")
    print("~   > Enter '2' to decode message    \t\t\t~")
    print("~   > Enter '3' to exit program\t\t\t\t~")
    print("~" + "".center(columns-2) + "~")
    print("~"*57)

    # promt user input...
    print("\n")
    action = int(input("\t> "))
    if action == 3:
        sys.exit("\n" + "See you next time".center(columns-2) +"\n\n\n")
    message = input("\n\tPlease, enter message: \n\t")
    print("\n")
    keyword = input("\tPlease, enter keyword: \n\t")

    # ...and call procedure according user choice
    if action == 1:
        coder(message, keyword)
    elif action == 2:
        decoder(message, keyword)



# ________________________________ ________________________________ #
"""                      Coding a message                         """


def coder(message, keyword):
    keyword_phrase = create_keyword_phrase(message, keyword)
    convertional_indexes = calculate_indexes(message, keyword_phrase)
    coded_message = coding_a_message(convertional_indexes)
    print("\n\tYour message now looks like here:\n\t" + coded_message + "\n\n")



def create_keyword_phrase(message: "user message to be coded", keyword: "user keyword") -> str:
    """
    Create keyword phrase by combining keyword letters under one-by-one
    to original user message letters (skipping empty spaces and non-alphabetical simbols)
    ex.: "its three words" with keyword "dog": "dog dogdo gdogd"
    """
    key_index = 0  # keep index in keword for iteration through its letters
    keyword_phrase = ""
    for element in message:
        if element in alphabet:
            keyword_phrase += keyword[key_index]
            key_index += 1
            if key_index > (len(keyword) - 1):
                key_index = 0
        else:
            keyword_phrase += (element)
    return keyword_phrase



def calculate_indexes(message, keyword_phrase) -> list:
    """
    create resulting indexes list: each element is index of coded message letter;
    if element is not a letter it copied from original message to coded_indexes string as is
    """
    convertional_indexes = []
    for i in range(len(message)):
        if message[i] in alphabet:
            calculated_index = int((alphabet.index(message[i]) +
                                    alphabet.index(keyword_phrase[i]))
                                    % len(alphabet)
                                  )
            convertional_indexes.append(calculated_index)
        else:
            convertional_indexes.append(message[i])
    return convertional_indexes



def coding_a_message(convertional_indexes) -> str:
    #create resulting coded message based on resulting indexes list
    coded_message = []
    for element in convertional_indexes:
        if isinstance(element, str):
            coded_message.append(element)
        else:
            coded_message.append(alphabet[element])
    coded_message = "".join(coded_message)
    return coded_message



# ________________________________ ________________________________ #
"""                      Decoding a message                       """


def decoder(message, keyword):
    # create keyword_phrase
    key_index = 0  # keep index in keword for iteration through its letters
    keyword_phrase = ""
    for element in message:
        if element in alphabet:
            keyword_phrase += (keyword[key_index])
            key_index += 1
            if key_index > (len(keyword) - 1):
                key_index = 0
        else:
            keyword_phrase += (element)
    #print(keyword_phrase)

    # create resulting indexes list: each element is index of coded message letter
    # if element is not a letter it copied from original message to coded_indexes string as is
    decoded_indexes = []
    for i in range(len(message)):
        if message[i] in alphabet:
            if alphabet.index(message[i]) < alphabet.index(keyword_phrase[i]):
                calculated_index = ((alphabet.index(message[i]) + len(alphabet)) -
                                     alphabet.index(keyword_phrase[i])
                                   )
            else:
                calculated_index = alphabet.index(message[i]) - alphabet.index(keyword_phrase[i])
            decoded_indexes.append(calculated_index)
        else:
            decoded_indexes.append(message[i])
    #print(decoded_indexes)

    #create resulting decoded message based on resulting indexes list
    decoded_message = []
    for element in decoded_indexes:
        if isinstance(element, str):
            decoded_message.append(element)
        else:
            decoded_message.append(alphabet[element])
    decoded_message = "".join(decoded_message)
    print("\nOriginal message looks like here: " + decoded_message)



# ________________________________ ________________________________ #
"""                      Running a program                        """

main()
