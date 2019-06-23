def foo(x, y):
    if( x > y ):
        (x, y) = (y, x);
    print('foo[%d][%d]'%(x,y));


def foo2(x, y):
    if(x>y):
        return y,x;
    else:
        return x,y;
    print('foo2[%d][%d]'%(x,y));
