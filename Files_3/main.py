import os 

files_list = []
current_dir = os.getcwd()
files_list += [file for file in os.listdir(current_dir) if file.endswith('.txt')]
if 'result.txt' in files_list:
    files_list.remove('result.txt')

data = {}

for file in files_list:
    with open(file, encoding='utf8') as f:
        count_lines = len(f.readlines())
        f.name
        data.setdefault(f.name, count_lines)

result_file = os.path.join(current_dir, 'result.txt')

with open(result_file, 'w', encoding='utf8') as f:
    for txt in sorted(data.items(), key=lambda item: item[1]):
        f.write(txt[0])
        f.write('\n')
        f.write(str(txt[1]))
        f.write('\n')
        with open(txt[0], 'r', encoding='utf8') as f2:
            data = f2.readlines()
        f.writelines(data)  
        f.write('\n')