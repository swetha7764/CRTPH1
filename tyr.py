def f(n):
    if n==2:
        return 0
    if n==3:
        return 1
    return f(n-2)+f(n-3)
a=f(5)
print(a)

def p(n,m):
    if m==0:
        return 1
    return n*p(n,m-1)
a=p(n,m)
print(a)
        
