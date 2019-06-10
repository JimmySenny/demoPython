#在屏幕上显示跑马灯文字

import os
import time

def main():
    content = "Hello Worle!";
    while True:
        #os.system('cls'); #
        os.system('clear');
        print(content);
        time.sleep(1);
        content = content[1:] + content[0];

if __name__ == '__main__':
    main();
