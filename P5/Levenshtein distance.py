def get_input_data():
    get_input_file_name = input()
    with open(get_input_file_name, 'r') as input_file:
        get_data = input_file.read().split(' ')
        return get_data
    
def get_levelshtein_distance(word_1_letters, word_2_letters, count):
    if len(word_1_letters) > len(word_2_letters):
        for letter in word_1_letters:
            if letter not in word_2_letters:
                word_1_letters.remove(letter)
                count += 1
                
        for letter in word_2_letters:
            if letter not in word_1_letters:
                word_1_letters.append(letter)
                count += 1
        
        for l in range(len(word_1_letters)-2):
            if word_1_letters[0] != word_2_letters[0]:
                word_1_letters[0] = word_2_letters[0] 
                count += 1
            if (word_1_letters[l] == word_2_letters[l]) and (word_1_letters[l+2] == word_2_letters[l+2]) and (word_1_letters[l+1] != word_2_letters[l+1]):
                word_1_letters[l+1] = word_2_letters[l+1] 
                count += 1

    if len(word_1_letters) < len(word_2_letters):
        for l in range(len(word_1_letters)-2):
            if word_1_letters[0] != word_2_letters[0]:
                word_1_letters[0] = word_2_letters[0] 
                count += 1
                
            if (word_1_letters[l] == word_2_letters[l]) and (word_1_letters[l+2] == word_2_letters[l+2]) and (word_1_letters[l+1] != word_2_letters[l+1]):
                word_1_letters[l+1] = word_2_letters[l+1] 
                count += 1
                
        for letter in word_1_letters:
            if letter not in word_2_letters:
                word_1_letters.remove(letter)
                count += 1
                
        for letter in word_2_letters:
            if letter not in word_1_letters:
                word_1_letters.append(letter)
                count += 1

    if len(word_1_letters) == len(word_2_letters):
        for letter in word_1_letters:
            if letter not in word_2_letters:
                word_1_letters.remove(letter)
                count += 1
                
        for letter in word_2_letters:
            if letter not in word_1_letters:
                word_1_letters.append(letter)
                count += 1

    return count


word_1, word_2 = get_input_data()

word_1_letters = []
for letter in word_1:
    word_1_letters.append(letter)

word_2_letters = []
for letter in word_2:
    word_2_letters.append(letter)

count = 0
final_count = get_levelshtein_distance(word_1_letters, word_2_letters, count)
print(final_count)

with open('Output_file.txt', 'w') as output_file:
    output_file.write(str(final_count))
