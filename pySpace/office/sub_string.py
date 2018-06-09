sub_list = []
def is_palndrom (val):
    j = len(val) -1
    for i in range(len(val)//2):
        if val[i] != val[j]:
            return False
        else:
            j -=1
    return True

def sub_str (val):
    n = len(val)
    for i in range(n):
        temp =0
        while n-i> temp:
            if is_palndrom(val[temp:temp+i+1]):
                global max_len, start
                sub_list.append(val[temp:temp+i+1])
                if max_len < len(val[temp:temp+i+1]):
                    max_len = len(val[temp:temp+i+1])
                    start = temp
            global sub_list
            sub_list.append(val[temp:temp+i+1])
            temp +=1
            
val = 'forgeeksskeegfor'
start = 0
max_len = 0
sub_str(val)

print(val[start:start +max_len])
print(sub_list)
