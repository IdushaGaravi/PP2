get_input_file_name = input()

def get_denominator_and_numerator(number):
    denominator_numereator = number.split('/')
    return denominator_numereator

def get_GCD(a, b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

def get_LCM(a, b):
    LCM_of_a_b = (a * b) / get_GCD(a, b)
    return LCM_of_a_b

def calculate_LCM(denominators):
    if len(denominators) == 2:
        LCM = get_LCM(denominators[0], denominators[1])
        return LCM
    else:
        for i in range(2, len(denominators)):
            LCM = get_LCM(get_LCM(denominators[0], denominators[1]), denominators[i])
        return LCM

def calculate_GCD(denominators):
    if len(denominators) == 2:
        GCD = get_GCD(denominators[0], denominators[1])
        return GCD
    else:
        for i in range(2, len(denominators)):
            GCD = get_GCD(get_GCD(denominators[0], denominators[1]), denominators[i])
        return GCD

with open(get_input_file_name, 'r') as input_file:      # open file, read and close it
    get_data = input_file.read().strip().split('\n')
    fraction_list = get_data[1:]
    denominators = []
    numerators = []
    for fraction in fraction_list:
        num = get_denominator_and_numerator(fraction)
        denominators.append(int(num[1]))
        numerators.append(int(num[0]))

    calculated_gcd = calculate_GCD(denominators)
    calculated_lcm = int(calculate_LCM(denominators))
    
    total = 0
    multiply_list = []
    for i in denominators:
        x = int(calculated_lcm / i)
        multiply_list.append(x)

    for j in range(len(multiply_list)):
        total += numerators[j] * multiply_list[j]

    final_list = [total] + [calculated_lcm]
    gcd_to_minimal_form = calculate_GCD(final_list)

    final_total = int(total/gcd_to_minimal_form)
    final_calculated_gcd = int(calculated_lcm/gcd_to_minimal_form)

with open('Output.txt', 'w') as output_file:
    if final_total == final_calculated_gcd:
        output_file.write('1')
    elif final_total == (-1) * final_calculated_gcd:
        output_file.write('-1')
    else:
        output_file.write(f'{final_total}/{final_calculated_gcd}')

        
