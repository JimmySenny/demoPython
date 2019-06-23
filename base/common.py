#输入两个数，得到最大公约数和最小公倍数

num1 = int(input("input num1:"));
num2 = int(input("input num2:"));
common_divisor = 0;
common_multiple = 0;

if( num1 <= 0 or num2 <= 0 ):
    print("input error num");
    exit;
if( num1 <= num2 ):
    common_divisor = num1;
    while True:        
        if( num1 % common_divisor == 0 and num2 % common_divisor == 0):
            break;
        common_divisor -= 1;
    common_multiple = num2;
    while True:
        if( common_multiple % num1 == 0 and common_multiple %num2 == 0):
            break;
        common_multiple += 1;
else:
    common_divisor = num2;
    while True:        
        if( num1 % common_divisor == 0 and num2 % common_divisor == 0):
            break;
        common_divisor -= 1;
    common_multiple = num1;
    while True:
        if( common_multiple % num1 == 0 and common_multiple %num2 == 0):
            break;
        common_multiple += 1;

print("num1[%d]num2[%d]common divisor[%d] multiple[%d]" %( num1, num2, common_divisor, common_multiple ));
