import zipfile

with open('zip_ans.txt', 'w') as zip_ans:
    [zip_ans.writelines(ans + '\n') for ans in
     sorted(list(set(name_py[:name_py.rfind('/')] for name_py in zipfile.ZipFile('main.zip', 'r').namelist() if
                     name_py[-3:] == '.py')))]
