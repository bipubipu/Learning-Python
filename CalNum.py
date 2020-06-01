import sys
import itertools
def comp(v1, op, v2):
    if op == '+':
        return v1+v2
    elif op == '-':
        return v1-v2
    elif op == '*':
        return v1*v2
    else:
        return v1/v2

def cal(va1,va2,va3,va4,va5):
    for op1 in ['+','-','*','/']:
        for op2 in ['+','-','*','/']:
            for op3 in ['+','-','*','/']:
                for op4 in ['+','-','*','/']:
                    result = comp(comp(comp(comp(va1,op1,va2),op2,va3),op3,va4),op4,va5)
                    if abs(result - 42) < 1e-10:
                        return True
    else:
        return False
for line in sys.stdin:
    
    val = list(map(int, line.split()))
    all_val = list(itertools.permutations(val)) 
    
    for va1,va2,va3,va4,va5 in all_val:
        if cal(va1,va2,va3,va4,va5):
            print('YES')
            break
    else:
        print('NO')
