# -------------------------------------#
def remove_duplicate(arr):
    arr_dict = {}
    for val in arr:
        if val not in arr_dict:
            print(val)
            arr_dict[val] = 0

names = ['vishal', 'vishal', 'babu', 'chak', 'chak']
#remove_duplicate(names)

# -------------------------------------#

# rev_str by recursion

def rev (rev_str,main_str):
    if main_str is not '':
        return rev(rev_str +main_str[-1] , main_str[:-1])
    else:
        return rev_str

#print(rev("", "vishal"))

# -------------------------------------#
# sort dict by value
#sorted(mydict.iteritems(), key=lambda (k,v): (v,k))

# -------------------------------------#
def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n ==1:
        print('move disk 1 from rod', from_rod , 'to rod', to_rod)
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print('move disk', n, 'from rod ', from_rod, 'to rod', to_rod)
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)


#tower_of_hanoi(3, 'a', 'b', 'c') 
# -------------------------------------#