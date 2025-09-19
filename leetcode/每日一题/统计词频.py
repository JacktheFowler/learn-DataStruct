def maxFreqSum(self, s: str) -> int:
    word=set(s)
    a, b=0
    for i in word:
        cnt=s.count(i)
        if i in 'aeiou':
            if cnt>a:
                a=cnt
        else:
            if cnt>b:
                b=cnt
    return a+b

