

import json

def main():
    mydict = {
        'name':'Jimmy',
        'age':'30',
        'tel':18993049930,
        'cars':[
            {'brand':'BYD','max_speed':180},
            {'brand':'Audi','max_speed':250},
            {'brand':'Benz','max_speed':300}
            ]
        };
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict,fs);
    except IOError as e:
        print(e);
    print('Write Done');

    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f);
    except IOError as e:
        print(e);
    print(data);

if __name__ == '__main__':
    main();
