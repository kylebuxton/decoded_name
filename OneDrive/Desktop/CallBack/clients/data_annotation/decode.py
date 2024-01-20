def decode(message_file):
    with open(message_file, "r") as file:
        lines = file.readlines()

    word_sets = []
    message = ""
    current_line = 1
    words_in_line = 1

    for line in lines:
        number, word = line.strip().split()
        number = int(number)
        word_sets.append((number, word))

    # Sort word sets based on numbers
    word_sets.sort(key=lambda item: item[0])

    # Iterate through sorted word sets and add words to message
    for number, word in word_sets:  
        if number == words_in_line:
            message += word + " "
            current_line += 1
            words_in_line += current_line

    return message.strip()

print(decode("coding_qual_input.txt"))