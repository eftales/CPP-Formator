# 目前本程序只支持将数据类型和变量名分离
# types 表示支持的数据类型

# cd "/mnt/d/share/实验楼/C++ Primer Plus/练习题源代码/chapter13"



types = [

        "bool",
        "char","case","const","class",
        "double",
        "else","explicit","enum",
        "float","friend",



        "ifstream","int",


        "long","longlong",

        "namespace","new",
        "ofstream","operator",


        "return",
        "struct","string","static",
        "typedef",
        "using","unsigned",
        "void","virtual",
        
        
        

        ":",
        r"#ifndef",r"#define"
        
        ]

your_type = [] # 这里加你需要分割的语句，比如说自定义的类等
types = types + your_type



need_enter = []
not_begin_with = [r"#include"]


tab_count = 0
case_diff = 0

MAX_LEN = 100000
# 较为大胆的尝试，认为变量名不会包含类型字符串，增加了排除字符串的操作，增加了自动识别类名的操作
def add_space_v4(line):

    new_line = list(line)

    # 遇到以 not_begin_with 中元素开头的就直接返回，不进行操作
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
            self_defined_class_name_list = []
            for each in line[end_index:-1]:
                if 'a' <= each <= 'z' or 'A' <= each <= 'Z':
                    self_defined_class_name_list.append(each)
                else:
                    break
            types.append("".join(self_defined_class_name_list))
        new_line[end_index:] = add_space_v4(''.join(new_line[end_index:]))
        new_line.insert(end_index,' ')
    return new_line

with open("new.cpp","w",encoding='UTF-8') as nf:

    with open("old.cpp","r",encoding='UTF-8') as f:
        for line in f:
            
            new_line = add_space_v4(line)# list 类型
            new_line = "".join(new_line) # str 类型
            for each_need_enter in need_enter:
                new_line = new_line.replace(each_need_enter,each_need_enter+"\n")

            tab_diff = line.count("{") - line.count("}")
            if (tab_diff <= 0):
                tab_count = tab_count + tab_diff
                write_line = "\t"*(tab_count) +new_line
            else:
                write_line = "\t"*(tab_count) + new_line
                tab_count = tab_count + tab_diff
                
            nf.write(write_line)