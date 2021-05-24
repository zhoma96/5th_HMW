import json

with open('my_text_3.txt', 'r') as my_object:
    content = my_object.read()
    print(content)
    content_str = "".join(content)
    content_splitted = content_str.split()
    print(len(content_splitted))
    slovar = dict([content.split()])
