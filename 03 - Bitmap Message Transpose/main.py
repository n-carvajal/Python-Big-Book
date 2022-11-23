"""Bitmap Message Transpose App"""


def get_message():
    """
    Gets user input. Validates the entry is not a blank string and that
    when a string is provided it has not spaces.
    """
    while True:
        msg = input("Enter your word or message (with no spaces).\n>> ")
        if msg == "":
            print("You must enter a message to continue.\n")
        elif " " in msg:
            print("Your message must have no spaces in it.\n")
        else:
            return msg


print(
    "Bitmap Message Transpose App, by Nicolas Carvajal\n\nDisplays a bitmap "
    "image comprised of the letters from a provided word or message."
)

original_message_list = []
transposed_message_list = []
message = get_message()
message_max_index = len(message) - 1
message_index = 0

with open(
    "03 - Bitmap Message Transpose/bitmap_original.txt", "r"
) as bitmap_original:
    original_message_list = bitmap_original.readlines()

for original_line in original_message_list:
    transposed_string = ""
    for original_char in original_line:
        if original_char == " ":
            transposed_string += original_char
        elif original_char == "\n":
            transposed_string += original_char
        else:
            if message_index > message_max_index:
                message_index = 0
                original_char = message[message_index]
                message_index += 1
                transposed_string += original_char
            else:
                original_char = message[message_index]
                message_index += 1
                transposed_string += original_char

    transposed_message_list.append(transposed_string)

with open(
    "03 - Bitmap Message Transpose/bitmap_transposed.txt", "w"
) as bitmap_transposed:
    bitmap_transposed.writelines(transposed_message_list)
