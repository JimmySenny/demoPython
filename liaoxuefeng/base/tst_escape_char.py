import sys
import os
import tempfile


TEMP = tempfile.mkdtemp(suffix='_py', prefix='learn_python_')

def main(): 
    print(r'sdfsas\fwae\t\n\wqef;"asdfsaf\\');

    print('''line1 
             line2
             line3''');

    print(r'''line1
    \edwsfw\fda"\tn\n
              line3''');

    fpath = os.path.join( TEMP );
    print('[%s]' % fpath);

if __name__ == '__main__':
    main();
