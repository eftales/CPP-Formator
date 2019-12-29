# CPP-Formator
When the code is pasted from the PDF, the indentation and the space are often gone. This code can fix this problem to some extent.

当从 PDF 中把代码粘贴过来的时候，往往缩进空格什么的都没了，本代码可以在一定程度上修复这个问题。

目前可以修复的有：各种类型，各种关键字，自定义类。

推荐搭配 iStylePDF 使用，虽然我觉得 Oxdo PDF 很好用。。
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

# feature work
多文件处理。

# bugs
1. 每一行都需要遍历一次 types 的 list，效率过低。暂时没有想过要改进，因为目前处理一个文件需要的时间可能只有几十毫秒吧，没有改进的必要。

2. 有误识别的情况，康你会把变量名错误的分开。但是这种错误可以只用用 `ctrl+H` 来一键解决，因此也暂时没有修复这个问题。