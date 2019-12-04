# CPP-Formator
When the code is pasted from the PDF, the indentation and the space are often gone. This code can fix this problem to some extent.

当从 PDF 中把代码粘贴过来的时候，往往缩进空格什么的都没了，本代码可以在一定程度上修复这个问题。

目前可以修复的有：各种类型，各种关键字，自定义类。

# How to use
## requests
- python3.*
## steps
1. Paste the messy code into the old.cpp

2. Run
```bash
python cppformator.py
```
3. Then you will find beautiful(to some extend) code in new.cpp

# others
This project will be maintained for a long time.

本项目将长期维护。

# 之后的工作
多文件处理。

# 不足
每一行都需要遍历一次 types 的 list，效率过低。暂时没有想过要改进，因为目前处理一个文件需要的时间可能只有几十毫秒吧，没有改进的必要。