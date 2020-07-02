import json
origin_text_file = open('assets/text.txt').readlines()
markup_words = [x.replace('\n', '') for x in origin_text_file]
dict_file = {'words':[]}
for i in markup_words:
    dict_file['words'].append(i)

with open("assets/wordos.json", 'w', encoding='utf-8') as fp:
    json.dump(dict_file, fp, ensure_ascii=False)

# file_r = open("assets/wordos.json", "w")

# result = random.choice(simple_list["abroad"])
# a = result.encode()
# print(a.decode())