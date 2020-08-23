学习笔记

排序算法：

1：Bubble sort 时间复杂度 O(n) 特点是好实现， 写一个double for loop + swap element

2：Quick sort 时间复杂度 O(nlogn) 核心是实现一个pivot function，——> 选择一个数当pivot 然后判断比pivot小的数放左边，大的数放右边，用一个count来记录比pivot小的个数 最后再把pivot放回正确的位置。 完成了pivot function后，quicksort的实现是以pivot的位置为准 不断重复地切割直到list的长度为一。

3：Merge sort 时间复杂度 O(nlogn) 分治的思想 把list 切割成最小单位后 再一次按照从小到大顺序重组。
