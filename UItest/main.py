
def print_test1():
    a = [1, 2, 3]
    b = a[:]
    c = a
    print(a is b, a is c, b is c, a == b, a == c, b == c)

def print_test2():
    a=1,2,3
    b=a[:]
    c=a
    print(a)
    print(a is b,a is c,b is c,a==b,a==c,b==c)
if __name__ == '__main__':
    print_test2()

