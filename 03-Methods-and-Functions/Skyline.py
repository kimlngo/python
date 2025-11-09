def skyline(input):
    output = ''

    for index, letter in enumerate(input):
        if index % 2 == 0:
            output += letter.lower()
        else:
            output += letter.upper()

    return output

print(skyline('Anthropomorphism'))