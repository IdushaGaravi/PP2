def get_input_data():
    get_input_file_name = input()
    with open(get_input_file_name, 'r') as input_file:
        get_data = input_file.read().split(' ')
        return get_data

def letter_substitution(word_1_letters, word_2_letters):
    count = 0
    for l in range(len(word_1_letters)-2):
            if word_1_letters[0] != word_2_letters[0]:
                word_1_letters[0] = word_2_letters[0] 
                count += 1
            if (word_1_letters[l] == word_2_letters[l]) and (word_1_letters[l+2] == word_2_letters[l+2]) and (word_1_letters[l+1] != word_2_letters[l+1]):
                word_1_letters[l+1] = word_2_letters[l+1] 
                count += 1
    #print(word_1_letters)
    return count

def letter_deletion(word_1_letters, word_2_letters):
    count = 0
    for letter in word_1_letters:
            if letter not in word_2_letters:
                word_1_letters.remove(letter)
                count += 1
    return count

def letter_insertion(word_1_letters, word_2_letters):
    count = 0
    for letter in word_2_letters:
            if letter not in word_1_letters:
                word_1_letters.append(letter)
                count += 1

    return count

def get_levelshtein_distance(word_1_letters, word_2_letters):
    if len(word_1_letters) > len(word_2_letters):
        deletion_count = letter_deletion(word_1_letters, word_2_letters)
        insertion_count = letter_insertion(word_1_letters, word_2_letters)       
        substitutional_count = letter_substitution(word_1_letters, word_2_letters)

    elif len(word_1_letters) < len(word_2_letters):
        substitutional_count = letter_substitution(word_1_letters, word_2_letters)
        deletion_count = letter_deletion(word_1_letters, word_2_letters)
        insertion_count = letter_insertion(word_1_letters, word_2_letters)       

    elif len(word_1_letters) == len(word_2_letters):
        deletion_count = letter_deletion(word_1_letters, word_2_letters)
        insertion_count = letter_insertion(word_1_letters, word_2_letters)       

    full_count = deletion_count + insertion_count + substitutional_count
    return full_count


word_1, word_2 = get_input_data()

word_1_letters = []
for letter in word_1:
    word_1_letters.append(letter)

word_2_letters = []
for letter in word_2:
    word_2_letters.append(letter)

final_count = get_levelshtein_distance(word_1_letters, word_2_letters)
print(final_count)

with open('OUTPUT.txt', 'w') as output_file:
    output_file.write(str(final_count))
