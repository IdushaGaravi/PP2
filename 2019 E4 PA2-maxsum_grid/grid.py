get_input_file_name = input()

def get_horizontal_sum(no_of_lines, grid):
    horizontal_sum_list = []
    for l in range(no_of_lines):
        for num in range(no_of_lines-2):
            total = 0
            total = int(grid[l][num]) + int(grid[l][num+1]) + int(grid[l][num+2])
            horizontal_sum_list.append(total)
    return horizontal_sum_list

def get_vertical_sum(no_of_lines, grid):
    vertical_sum_list = []
    for l in range(no_of_lines-2):
        for num in range(no_of_lines):
            total = 0
            total = int(grid[l][num]) + int(grid[l+1][num]) + int(grid[l+2][num])
            vertical_sum_list.append(total)
    return vertical_sum_list

with open(get_input_file_name, 'r') as input_file:
    get_data = input_file.read().strip().split('\n')
    no_of_lines = int(get_data[0])
    get_grid_data = get_data[1:]

    grid = []
    for data in get_grid_data:
        grid_data = data.split(' ')
        grid.append(grid_data)

    horizontal_list = get_horizontal_sum(no_of_lines, grid)
    vertical_list = get_vertical_sum(no_of_lines, grid)
    final_list = horizontal_list + vertical_list
    
with open('output.txt', 'w') as output_file:
    maximum_sum = str(max(final_list))
    output_file.write(maximum_sum)
