import json

email_default = input("Mail you'd like to organize for: ")
text_file = 'mail_account_list.txt' # make this an input variable that adds '.txt' at the end
json_file = 'json_account_list.json' # make this an input variable that adds '.json' at the end
file_location = 'C:\\Users\\willi\\Documents\\Python\\Project_Files\\'

with open(file_location + text_file, mode='r', newline='') as f:
    c_list = {}
    for line in f:
        print('Website: ', line.strip('\r\n'))
        w = line.strip('\r\n')
        c = input('Classification: ')
        a = input('Attached account: ')

# Hotkey classifications that make classifying quicker
        if c.lower() == 'd':
            c = 'delete'
        if c.lower() == 'k':
            c = 'keep'

# Hotkey for account if it's the same as your email
        if a.lower() == 'm' or a.lower() == 'h' or a.lower() == 'e':
            a = email_default

# Checks if the classification exist. Then it either creates a new json object or appends an existing classification object
# NB problem that needs to be fixed. Json list begins with two elements without brackets, making it awkward to use it
        if c in c_list:
            c_list[c].append([w, a])
        else:
            c_list[c] = [w, a]

with open(file_location + json_file, mode='w') as j:
    json.dump(c_list, j)
