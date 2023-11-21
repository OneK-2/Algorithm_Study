# 거듭제곱구하기 A를 B번 곱하기
def power(A, B, C):
    if B == 1: #지수가 1
        return A % C
    else:
        tmp = power(A, B//2, C) 
        if B%2 == 0: #짝수일떄 지수 식 C^n/2 * C^n/2
            return (tmp*tmp) % C 
        else: #홀수 지수 식  C^n-1/2 * C^n-1/2 * C
            return (tmp*tmp*A) % C

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

print(power(A,B,C))
