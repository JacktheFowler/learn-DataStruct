"""
给定一个正整数n，将其切分为至少两个正整数的和，求切分后所有整数的乘积最大是多少
考虑最小拆分为2 2*(n-2)>=n n>=4可以拆分 拆分因子只可能含2, 3
对于 3+3=2+2+2 但3*3>2*2*2 尽可能拆为3
拆为3 余数可能为 0 1{ans*3*1<ans*(3+1) 最后一个3如果余数为1 拆分为2*2} 2
"""
import math

def maxProductCut(num):
    if num<4:
        return num-1
    a, b=num//3, num%3
    if b==1:
        return math.pow(3, a-1)*4
    else:
        return math.pow(3, a)*b

