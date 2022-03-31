[TOC]



# 一、刷题常用的python语法与技巧

## 1.1 可直接使用的python內部的函数

### 排序
**list.sort()与.sorted()**

均使用timesort，但是.sort()一般用于列表，而.sorted()一般用于对所有可迭代对象进行排序

时间复杂度$O(nlogn)$空间复杂$O(n)$

[.sort()详细实现细节](https://www.cnblogs.com/clement-jiao/p/9243066.html#:~:text=%E5%89%8D%E4%B8%8D%E4%B9%85%E5%9C%A8%E8%BF%99%E7%AF%87%E6%96%87%E7%AB%A0%20sort%E4%B8%8Esorted%E7%9A%84%E5%8C%BA%E5%88%AB%20%E4%B8%AD%E6%94%B6%E5%88%B0%E4%BA%86%E8%BF%99%E6%A0%B7%E7%9A%84%E4%B8%80%E4%B8%AA%E6%8F%90%E9%97%AE%EF%BC%9A%E2%80%9Cpython%E7%9A%84%20sort%20%E5%86%85%E9%83%A8%E5%AE%9E%E7%8E%B0%E6%9C%BA%E5%88%B6%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F%20%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E6%98%AF%E5%A4%9A%E5%B0%91,%E2%80%9D%E3%80%82%20%E5%87%A0%E7%95%AAGoogle%E4%B9%8B%E5%90%8E%E6%9C%89%E4%BA%86%E4%BB%A5%E4%B8%8B%E7%9A%84%E5%9B%9E%E7%AD%94%EF%BC%9A%20%E5%86%85%E9%83%A8%E5%AE%9E%E7%8E%B0%E6%9C%BA%E5%88%B6%E4%B8%BA%EF%BC%9ATimesort%20%E6%9C%80%E5%9D%8F%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E4%B8%BA%EF%BC%9AO%EF%BC%88n%20log%20n%EF%BC%89%20%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E4%B8%BA%EF%BC%9AO%EF%BC%88n%EF%BC%89/)

## 1.2 运算符

|    运算符    |    作用    |
| :- |:- |
|    **    |   幂指数   |
|    //    |   向下取除数|
|    %     |   取余数|



# 二、基本概念

## 2.1 各种数据类型

下图为不同数据结构在内存空间中占用的空间大小，python万物皆对象，每个数据类型所占空间更多。
![数据类型占用存储空间](\assets\imgs\20200804193045440.png)


# 三、解题思路

## 3.1 递归
### 3.1.1 递归的时间复杂度与空间复杂度分析
**时间（空间）复杂度 = 递归次数 * 每次递归的时间（空间）复杂度**
关键在于找到递归的次数，可以使用画二叉树的方式来找。例如求斐波那契数列的如下代码：

```
class solution(object):
    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n-2)
```
该代码的时间复杂度为$O(2^n)$（相当于直接两个节点一路往下画二叉树）。
### 3.1.2 递归方法应用场景





# 四、分类题型汇总

## 4.1 二分法查找
二分法基本用于有序数组的查找、删除等。

### 相关题目
[704二分查找](https://leetcode-cn.com/problems/binary-search/)
注意左右指针移动时为:
```
left = mid + 1
right = mid - 1
```
[35搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)
要考虑从0或者len(nums)处插入的可能

[69x的完全平方根](https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/)
注意拟牛顿解法

[367有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)

[34在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
最好把直接二分查找和找数字的左右边界法分别做一下

**总结**
找target在有序数组nums中的右边界
```
def help(target):
    i, j = 0, len(nums)-1
    while i <= j:
        m = (i + j) // 2
        if nums[m] <= target: i = m+1
        else: j = m-1
    return i
```
找target在有序数组nums中的左边界
```
def help(target):
    i, j = 0, len(nums)-1
    while i <= j:
        m = (i + j) // 2
        if nums[m] >= target: j = m-1
        else: i = m+1
    return j
```





