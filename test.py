
def insert_sort(old_list):
    n = len(old_list)
    for i in range(1,n):
        temp = old_list[i]
        j = i
        while j > 0 and temp < old_list[j-1]:
            old_list[j] = old_list[j-1]
            j = j-1
            old_list[j] = temp
        return old_list
        
old_list = [1,9,5,0,-2,38,20,-9,6]
insert_sort(old_list)

