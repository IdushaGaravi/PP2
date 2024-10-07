get_input_file_name = input()

def convert_bin_to_A_and_B(number):
    encrypted_bin = []
    for i in number:
        if i == '0':
            encrypted_bin.append('A')
        else:
            encrypted_bin.append('B')
    return ''.join(encrypted_bin)

with open(get_input_file_name, 'r') as input_file:
    get_data = input_file.read().strip().split('\n')
    get_message = get_data[1:]

    final_list = []
    for message in get_message:
        message = message.upper()
        encrypted_msg = []
        for letter in message:
            if letter.isalpha() == True:
                number = bin(ord(letter)-65)
                number = (number[2:]).zfill(5)
                encryption = convert_bin_to_A_and_B(number)
                encrypted_msg.append(encryption)
            elif letter == ' ':
                number = bin(26)
                number = number[2:].zfill(5)
                encryption = convert_bin_to_A_and_B(number)
                encrypted_msg.append(encryption)

        final_list.append(''.join(encrypted_msg))

with open('output.txt', 'w') as output_file:
    for final_msg in range(len(final_list)):
        output_file.write(final_list[final_msg])
        if final_msg != len(final_list)-1:
            output_file.write('\n')
        
