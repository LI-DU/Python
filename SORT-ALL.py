#堆排序

def HeapAdjustDown(lst,start,end):
    #temp保存当前节点
    temp = lst[start]
    #2*start+1是序号为start的节点左子节点的编号
    child = 2*start + 1

    while child <= end:
        #找到堆中的叶子节点左右节点中最大的那个
        if child+1 <= end and lst[child+1] > lst[child]:
            child += 1
        #当前的节点符合最大堆的定义，则不用调整，跳出循环
        if lst[child] <= temp:
            break
        lst[start],lst[child] = lst[child],lst[start]
        start = child

def HeapSort(lst):
    #将数组建成最大的堆
    #第一个非叶子节点的位置lem(lst)//2-1
    for child in range(len(lst)//2-1,-1,-1):
        HeapAdjustDown(lst,child,len(lst)-1)

    for child in range(len(lst)-1,0,-1):
        lst[0],lst[child] = lst[child],lst[0]
        #将lst[0,,,i-1]重新调整为最大值
        HeapAdjustDown(lst,0,child-1)

if __name__ == '__main__':
    lst1 = [5,9,20,38,4,6,80,57,25,10,16,8]
    print(lst1)
    HeapSort(lst1)
    print(lst1)

