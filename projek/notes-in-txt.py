file = open("notes.txt","w+")
file = file.write('''Your notes:
===========\n\n''')

print('\nCreate your own notes')
print('=====================\n')

def main():
    command = ''
    while command != 'exit()':
        for i in range(1,11):
            notes = input(f'{i}. ')
            file = open("notes.txt","a")
            file.write(f'{notes}\n')
            if notes == 'exit()':
                break
        command = 'exit()'

main()

print('\nThank you!')
print('==========')
