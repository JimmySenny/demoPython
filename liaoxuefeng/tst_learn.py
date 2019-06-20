
from datetime import datetime;

def get_name():
    today = datetime.now().strftime('%Y%m%d_%H%M%S');
    print('[%s]' %today);

def main():
    get_name();

if __name__ == '__main__':
    main();
