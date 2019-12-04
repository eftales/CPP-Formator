# 目前本程序只支持将数据类型和变量名分离
# types 表示支持的数据类型
types = ["int","char","double","return","struct","case",
        "const","using","namespace","string","else",
        "ifstream","ofstream","void","float","long","longlong",
        "unsigned","static",r"#ifndef",r"#define","class",
        "typedef","enum","operator","friend"]

not_begin_with = [r"#include"]

tab_count = 0
case_diff = 0

MAX_LEN = 100000
# 较为大胆的尝试，认为变量名不会包含类型字符串，增加了排除字符串的操作，增加了自动识别类名的操作
def add_space_v4(line):

    new_line = list(line)

    # 遇到以 ** 开头的就直接返回，不进行操作
    for each_begin in not_begin_with:
        if (line[0:len(each_begin)] == each_begin):
            return new_line

    start_index = -1
    end_index = MAX_LEN
    for each_type in types:
        start_index = line.find(each_type)
        if start_index != -1:
            end_index = min(start_index + len(each_type),end_index)

    if (end_index != MAX_LEN):
        if line[0:end_index] == "class": # class 必须写在行首
            types.append(line[end_index:-1].replace(" ",""))
        new_line[end_index:] = add_space_v4(''.join(new_line[end_index:]))
        new_line.insert(end_index,' ')
    return new_line

with open("new.cpp","w",encoding='UTF-8') as nf:

    with open("old.cpp","r",encoding='UTF-8') as f:
        for line in f:
            
            new_line = add_space_v4(line)



            tab_diff = line.count("{") - line.count("}")
            if (tab_diff <= 0):
                tab_count = tab_count + tab_diff
                write_line = "\t"*(tab_count) + "".join(new_line)
            else:
                write_line = "\t"*(tab_count) + "".join(new_line)
                tab_count = tab_count + tab_diff
                
            nf.write(write_line)