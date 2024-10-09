def get_input_data():
    get_input_file = input()

    with open(get_input_file, 'r') as input_file:
        get_data = input_file.read().strip().split('\n')
        return get_data

def get_subsequence(characters_list, length_of_subsequence):
    segments_list = []
    for i in range(0, len(characters_list), length_of_subsequence):
        #x = i
        sudsequence_list = characters_list[i: (i + length_of_subsequence)]

        subsequence = []
        for j in sudsequence_list:
            if j not in subsequence:
                subsequence.append(j)
        segments_list.append(''.join(subsequence))
    return segments_list

input_data = get_input_data()

characters = input_data[0]
length_of_subsequence = int(input_data[1])

characters_list = []

for char in characters:
    characters_list.append(char)

segments = get_subsequence(characters_list, length_of_subsequence)

for string in segments:
        print(string)
              
with open('Output.txt', 'w') as output_file:
    for k in range(len(segments)):
        output_file.write(segments[k])
              
        if k != len(segments)-1:
              output_file.write('\n')
              
