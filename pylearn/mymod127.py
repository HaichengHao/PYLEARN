# editor 百年
# date: 2024/1/18 17:01
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multi(a,b):
    return a*b
def divn(a,b):
    try:
        return a/b
    except ZeroDivisionError :
        print('零不能作为除数')
