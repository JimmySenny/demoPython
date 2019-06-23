
def main():
    f = None
    try:
        #f = open('file_open.py', 'r', encoding='utf-8');
        f = open('file_open.py1', 'r', encoding='utf-8');
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()
