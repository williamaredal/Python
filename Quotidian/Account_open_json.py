import os
import json

json_file = 'json_account_list.json' # make this an input variable that adds '.json' at the end
file_location = 'C:\\Users\\willi\\Documents\\Python\\Project_Files\\'

with open(file_location + json_file, mode='r') as j:
    registry = json.load(j)

    for classification in registry:
        class_account = [account for account in registry.get(classification)]
        print('Press [n] for next \n', classification + ':\n')

        for element in class_account:
            print(element, '\n')
            key_input = input()
            if key_input.lower() == 'n':
                continue
            else:
                key_input = input('[n] for next')

# NB have not tested this part yet
    done = input('Finished and want to delete the list? [y/n]')
    if done.lower() = 'y':
        os.remove(file_location + json_file)
        print('Deleted')
    else:
        quit
