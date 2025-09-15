"""
输入 要打印的字符串 s 坏掉的键 s
输出可以打印的单词数量 不含前导空格
"""

def solve(text, brokenLetters):
    words=text.split()
    brokenLettersSet=set(brokenLetters)
    cnt=0
    for i in words:
        if i=='':
            continue
        wordSet=set(i)
        if not (wordSet&brokenLettersSet): # 如果交集为空
            cnt+=1
    return cnt


text = "hello world"
brokenLetters = "ad"
print(solve(text, brokenLetters))