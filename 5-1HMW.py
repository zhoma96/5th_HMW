my_file = open('my_text.txt', 'w+')
content = ['Hello\n', 'My Friend\n', 'Bye\n']
my_file.writelines(content)
my_file.close()
