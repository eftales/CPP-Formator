# 目前本程序只支持将数据类型和变量名分离
# types 表示支持的数据类型
types = ["int","char","double","return","struct","case",
        "constint","usingnamespace","string","elseif",
        "ifstream","ofstream","void","float","long","long long"]

tab_count = 0
case_diff = 0

def add_space(line):
    new_line = list(line)

    if (line[0] == 'c'):
        if (line[0:4] == "char" ): 
            new_line.insert(4,' ')
        if (line[0:4] == "case"):
            new_line.insert(4,' ')

        elif (line[0:5] == "const"):
            new_line.insert(5,' ')
            if (line[5:8] == "int"):
                new_line.insert(9,' ') # 因为已经插入一个 " " 了，所以要往后多移一位

    elif (line[0] == 'd'):
        if (line[0:6] == "double"):
            new_line.insert(6,' ')

    elif (line[0] == 'e'):
        if (line[0:6] == "elseif"):
            new_line.insert(4,' ')

    elif (line[0] == 'f'):
        if (line[0:5] == "float"):
            new_line.insert(5,' ')

    elif (line[0] == 'i'):
        if (line[0:3] == "int"):
            new_line.insert(3,' ')       
        if (line[0:8] == "ifstream"):
            new_line.insert(8,' ')       

    elif (line[0] == 'l'):
        if (line[0:4] == "long"):
            new_line.insert(4,' ')
            new_line[5:] = add_space(''.join(new_line[5:]))

    elif (line[0] == 'o'):
        if (line[0:8] == "ofstream"):
            new_line.insert(8,' ')

            
    elif (line[0] == 'r'):
        if (line[0:6] == "return"):
            new_line.insert(6,' ')





    elif (line[0] == 's'):
        if (line[0:6] == "struct"):
            new_line.insert(6,' ')
        if (line[0:6] == "string"):
            new_line.insert(6,' ')
    elif (line[0] == 'u'):
        if (line[0:14] == "usingnamespace"):
            new_line.insert(5,' ')
            new_line.insert(15,' ')



    elif (line[0] == 'v'):
        if (line[0:4] == "void"):
            new_line.insert(4,' ')

    return new_line

with open("new.cpp","w",encoding='UTF-8') as nf:

    with open("old.cpp","r",encoding='UTF-8') as f:
        for line in f:
            
            new_line = add_space(line)



            tab_diff = line.count("{") - line.count("}")
            if (tab_diff <= 0):
                tab_count = tab_count + tab_diff
                write_line = "\t"*(tab_count) + "".join(new_line)
            else:
                write_line = "\t"*(tab_count) + "".join(new_line)
                tab_count = tab_count + tab_diff
                
            nf.write(write_line)