"""
汇编指令

输入
n行汇编指令

输出
打印结果
"""

import sys

sys.stdin=open('summer_24_5_8/1.2')
def input_data():
    words=[]
    for line in sys.stdin:
        words.append(line.split())
    return words

def src_type(src, d):
    if src.isdigit():
        return int(src)
    if src.isalnum():
        return d[src]
    
def process(words):
    res={}
    for word in words:
        if word[0]=='MOV':
            res[word[1]]=src_type(word[2], res)
        elif word[0]=='ADD':
            res[word[1]]=src_type(word[2], res)+src_type(word[3], res)
        elif word[0]=='SUB':
            res[word[1]]=src_type(word[2], res)-src_type(word[3], res)
        elif word[0]=='MUL':
            res[word[1]]=src_type(word[2], res)*src_type(word[3], res)
        elif word[0]=='DIV':
            res[word[1]]=src_type(word[2], res)/src_type(word[3], res)
        elif word[0]=='PRINT':
            print(res[word[1]])
    
if __name__=='__main__':
    words=input_data()
    process(words)
