# 桶排序

def BucketSort(lst):
	#创建并初始化桶
	Bucket = [0]*(max(lst) - min(lst) + 1)
	#把所有的元素放入桶中，把对应的元素加1
	for i in range(len(lst)):
		Bucket[lst[i] - min(lst)] += 1
	temp = []
	#取出桶中元素
	for i in range(len(Bucket)):
		if Bucket[i] != 0:
			temp += [min(lst) + i]*Bucket[i]
	return temp

if __name__ == '__main__':
	lst1 = [7,11,28,70,35,19,20,39,4,57,20,8]
	print(lst1)
	print(BucketSort(lst1))

