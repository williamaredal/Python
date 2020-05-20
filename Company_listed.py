folder_location = 'C:\\Users\\willi\\Documents\\Python\\Project_Files\\' # Can be changed to input value
file = 'nasdaqlisted.txt'                         # Can be changed to input value
sorted_file = 'nasdaq_listed.txt'                 # Can be changed to input value

with open(folder_location + file, mode='r') as in_file:
    list_text = []

    for line in in_file:
        start = False
        symbol = ''
        company_name = ''

        for s in line:
            if s == '|':
                break
            else:
                symbol = symbol + s

        for c in line:
            if c ==  '.' or c == '-' or (c == '|' and start):
                break
            if c == '|':
                start = True
            elif start:
                company_name = company_name + c

        list_text.append(symbol + ';' + company_name)
        continue

    with open(folder_location + sorted_file, mode='w') as out_file:
        for element in list_text:
            out_file.write(element + '\n')
