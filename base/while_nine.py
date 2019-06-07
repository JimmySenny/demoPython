#九九乘法表

i = 1;
j = 1;
while(i < 10):
    j = 1;
    while(j < 10):
        if(i >= j ):
            print('[%d]*[%d]=[%d]'%( i, j, i*j ),end='\t');
        j += 1;
    i += 1;
    print("\n");
    

