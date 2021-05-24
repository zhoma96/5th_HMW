import json

data = ['hi', 'good2', 'bye\n', 'end\n']

with open('my_text_2.txt', 'w+') as my_object:
    json.dump(data, my_object)
    json_str = json.dumps(data)
    print(json_str)
    line_count = 0
    for line in my_object:
        line_count = line_count + 1
    print(line_count)
    print('Number of words: ', len(json_str.split()), 'words')