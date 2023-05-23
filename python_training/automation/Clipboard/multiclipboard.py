import sys
import clipboard #need to import clipboard from pip (pip install clipboard)
import json

SAVED_DATA = 'clipboard.json'

def save_to_clipboard(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_from_clipboard(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_from_clipboard(SAVED_DATA)

    if command =='save':
        print('save')
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_to_clipboard(SAVED_DATA, data)
        print(f"{data[key]} saved to {SAVED_DATA}")
    elif command =='load':
        print('load')
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print(data[key])
            print(f'copied {data[key]} to clipboard')
        else:
            print('key not found')
    elif command == 'list':
        print('list')
        print(data)
    elif command == 'delete':
        print('delete')
        key = input('Enter a key: ')
        if key in data:
            del data[key]
            save_to_clipboard(SAVED_DATA, data)
            print(f'{key} key deleted')
        else:
            print('key not found')
    else:
        print('unrecognized command')
else:
    print('please enter only one of the following commands: save, load, delete, list')