# 目前本程序只支持将数据类型和变量名分离
# types 表示支持的数据类型
types = ["int","char","double","return","struct","case",
        "constint","usingnamespace","string","elseif",
        "ifstream","ofstream","void","float","long","long long",
        "unsigned"]

tab_count = 0
case_diff = 0

def add_space(line):
    new_line = list(line)
    current_type = None

    if (line[0] == 'c'):
        if (line[0:len("char")] == "char" ): 
            current_type = "char"
        if (line[0:len("case")] == "case"):
            current_type = "case"

        elif (line[0:len("const")] == "const"):
            current_type = "const"

    elif (line[0] == 'd'):
        if (line[0:len("double")] == "double"):
            current_type = "double"

    elif (line[0] == 'e'):
        if (line[0:len("elseif")] == "elseif"):
            current_type = "elseif"

    elif (line[0] == 'f'):
        if (line[0:len("float")] == "float"):
            current_type = "float"
        elif (line[0:len("for(")] == "for("):
            current_type = "for("

    elif (line[0] == 'i'):
        if (line[0:len("int")] == "int"):
            current_type = "int"    
        if (line[0:len("ifstream")] == "ifstream"):
            current_type = "ifstream"       

    elif (line[0] == 'l'):
        if (line[0:len("long")] == "long"):
            current_type = "long"    


    elif (line[0] == 'n'):
        if (line[0:len("namespace")] == "namespace"):
            current_type = "namespace"   

    elif (line[0] == 'o'):
        if (line[0:len("ofstream")] == "ofstream"):
            current_type = "ofstream"   

            
    elif (line[0] == 'r'):
        if (line[0:len("return")] == "return"):
            current_type = "return"   


    elif (line[0] == 's'):
        if (line[0:len("struct")] == "struct"):
            current_type = "struct"   
        if (line[0:len("string")] == "string"):
            current_type = "string" 

    elif (line[0] == 'u'):
        if (line[0:len("using")] == "using"):
            current_type = "using" 
        if (line[0:len("unsigned")] == "unsigned"):
            current_type = "unsigned" 

    elif (line[0] == 'v'):
        if (line[0:len("void")] == "void"):
            current_type = "void" 

    if (current_type != None):
        new_line[len(current_type):] = add_space(''.join(new_line[len(current_type):]))
        new_line.insert(len(current_type),' ')
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