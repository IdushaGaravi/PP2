def get_input_data():
    get_input_file = input()
    with open(get_input_file, 'r') as input_file:
        get_data = (input_file.read().split('\n'))
    return get_data

def get_rearrange_list(num_list, x, y):
    x_index = []
    for i in range(len(num_list)):
        if num_list[i] == x:
            x_index.append(i)
    #return x_index

    y_index = []
    for i in range(len(num_list)):
        if num_list[i] == y:
            y_index.append(i)

    for j in range(len(x_index)):
        if x_index[j] > y_index[j]:
            x_j = int(x_index[j])
            y_j = int(y_index[j])
            d = x_j - y_j
            #print(j, d)

            num_list[x_j-d], num_list[x_j+1] = num_list[x_j+1], num_list[x_j-d]
        else:
            x_j = int(x_index[j])
            y_j = int(y_index[j])
            d = y_j - x_j

            num_list[x_j+d], num_list[x_j+1] = num_list[x_j+1], num_list[x_j+d]
    return num_list
                

input_data = get_input_data()

final_list = []
for data in input_data:
    get_input = data.split(' ')
    get_data = get_input[0]
    get_data = get_data[1:-1]
    num_list = []
    for num in get_data.split(','):
       num_list.append(int(num))
    #print(num_list)
    x = int(get_input[1])
    y = int(get_input[2])

    rearrange_list = get_rearrange_list(num_list, x, y)
    final_list.append(rearrange_list)

for rearrange_list in final_list:
    print(rearrange_list)

with open('Ouput.txt', 'w') as output_file:
    for k in range(len(final_list)):
        output_file.write(str(final_list[k]))
        if k != len(final_list)-1:
            output_file.write('\n')

