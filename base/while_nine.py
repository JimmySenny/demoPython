#九九乘法表

i = 1;
j = 1;
while(i < 10):
    j = 1;
    while(j < 10):
        print('[%d]*[%d]=[%d]\t\t', i, j, i*j );
        j += 1;
    i += 1;
    print("\n");
    

