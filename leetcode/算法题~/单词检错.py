"""
拼写检测

输入
wordlist 正确单词表
query 带查询单词

规则
完全匹配 返回相同单词
忽略大小写 返回匹配第一个
原因错误 返回替换原因第一个
完全不匹配 返回""

返回 answer 单词列表

最佳方式采用hash查找 非循环
"""
def MapLow(word):
    a='aeiou'
    res=[]
    for i in word:
        if i in a:
            res.append('a')
        else:
            res.append(i)
    return ''.join(res)

def solve(wordlist, queries):
    a='aeiou'
    res=[0]*len(queries)
    for idx, i in enumerate(queries):
        # 检验完全匹配
        for j in wordlist:
            if i==j:
                res[idx]=j
                break
        else:
            # 检验大小写匹配
            for j in wordlist:
                if i.lower()==j.lower():
                    res[idx]=j
                    break
            else:
                # 检验元音匹配
                for j in wordlist:
                    if MapLow(j.lower())==MapLow(i.lower()):
                        res[idx]=j
                        break
                else:
                    res[idx]=''
    return res

if __name__=='__main__':
    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    res=solve(wordlist, queries)
    print(res)
    