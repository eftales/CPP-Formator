# 目前本程序只支持将数据类型和变量名分离
# types 表示支持的数据类型
types = ["int","char","double","return","struct","case",
        "constint","usingnamespace","string","elseif",
        "ifstream","ofstream","void","float","long","long long",
        "unsigned","static",r"#ifndef",r"#define","class","std::",
        "(","typedef"]

tab_count = 0
case_diff = 0

# 加空格
def add_space_v2(line):
    new_line = list(line)
    current_type = None
    for each_type in types:
        if (line[0:len(each_type)] == each_type):
            current_type = each_type

    if (current_type != None):
        new_line[len(current_type):] = add_space_v2(''.join(new_line[len(current_type):]))
        new_line.insert(len(current_type),' ')
    return new_line

with open("new.cpp","w",encoding='UTF-8') as nf:

    with open("old.cpp","r",encoding='UTF-8') as f:
        for line in f:
            
            new_line = add_space_v2(line)



            tab_diff = line.count("{") - line.count("}")
            if (tab_diff <= 0):
                tab_count = tab_count + tab_diff
                write_line = "\t"*(tab_count) + "".join(new_line)
            else:
                write_line = "\t"*(tab_count) + "".join(new_line)
                tab_count = tab_count + tab_diff
                
            nf.write(write_line)