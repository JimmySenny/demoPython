
import time

def main():
    #一次性读取
    with open('readlines.py','r',encoding='utf-8') as f:
        print(f.read());

    #逐行读取
    with open('readlines.py','r',encoding='utf-8') as f:
        for line in f:
            print(line,end='');
            time.sleep(0.2);

    print();

    #读取文件按行读取
    with open('readlines.py','r',encoding='utf-8') as f:
        lines = f.readlines();
    print(lines);

if __name__ == '__main__':
    main();
