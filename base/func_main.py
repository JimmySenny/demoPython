from func_foo import *;

def foo(x, y):
    if( x > y ):
        (x, y) = (y, x);
    print('main_foo[%d][%d]'%(x,y));

def main():
    foo(x, y);
    print('func[%d][%d]'%(x,y));
    

if __name__ == '__main__':
    x = 10;
    y = 5;
    print('call[%d][%d]'%(x,y));
    foo(x, y);
    print('call[%d][%d]'%(x,y));
    x,y = foo2(x, y);
    print('call[%d][%d]'%(x,y));
