学习笔记
新的做题技巧：
Q70.爬楼梯，用了dp的思路 也第一次尝试了resursion 加缓存的效果 说白了就是在外面见一个全局字典 把中途遇到的处理过的数据存储起来 避免以后重复计算
Q22.括号生成可以使用backtracking 不过不改变path的话 把path的变化作为input的话 可以不用backtarcking
Q104：resursion的思路可以是top-down （initialize 一个值 然后值随着递归往下更新）。 或者bottom-up， 在最底层赋值然后这数值随着递归函数的弹出往上赋值。

其他知识收获：
1.排序根据前两个元素
a=[[1,2],[4,5],[6,6],[6,2],[5,3],[9,7]]
b = sorted(a, key= lambda x:(x[0],x[1]))

2.heap 根据第二元素信息返回：
import heapq
heapq.heapify(a)
heapq.nlargest(3,iterable=a,key=lambda x:x[1])

3.heap 根据hashmap value的信息进行排位
hash={
    "1":1,
    "2":2,
    "3":3
}
 heapq.nlargest(3,hash,key=lambda x:hash[x])

4.把2d list 变成set：
obstacles = [[2,4],[1,4],[3,4]]
obstacles = set(map(tuple, obstacles))




