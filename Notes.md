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

## 1.3 常见操作

### 1.3.1 简单操作

**创建无限大数字**
```
inf = float('inf')
```

**python中的类**
```
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
```
第二种定义方法的name和score属于私有变量，无法直接通过.name来访问，但可以在类中定义方法来获得，因为在内部是可以访问私有变量的。

### 1.3.2 列表操作

**创建空表**
```
L = []
```
**创建长度为n的列表**
```
L = [0] * n
```
**使用列表模拟矩阵**
```
n = 10
matrix = [[0] * n for _ in range(n)]
```
**列表逆序**
```
list.reverse()
s = 'hello'
reversed_s = s[::-1]
s[0:n] = list(reversed(s[0:n]))
```
**字符串和列表互相转换**
```
s = list(s)
s = ''.join(s)
```

### 1.3.3 字典操作
字典的空间复杂度为$O(n)$，查找的时间复杂度为$O(1)$

**字典的基本操作**
1.字典使用规则
```
dict[key]=value#key可以是字符串也可以是数字但不能重复
```
2.字典基本操作
```
del dict[key]#字典删除键值对
dict.clear()#清空字典
dict.get(key)#通过key获得value
dict.update({key1:value1,key1:value1})#更新，若key存在于原字典，则更新其value值
dict.items(),dict.keys(),dict.values()#获得所有键值对/关键字/值，但若想访问需将返回值用list()方法转换
```
```
删除某一字典键值对，不要直接用
for c in need:
for c in list(need.keys()):
                    a = need[c]
                    if a==0:
                        del need[c]
```
**使用字典格式化字符串**
```
# 字符串模板中使用key
temp = '教程是:%(name)s, 价格是:%(price)010.2f, 出版社是:%(publish)s'
book = {'name':'Python基础教程', 'price': 99, 'publish': 'C语言中文网'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
book = {'name':'C语言小白变怪兽', 'price':159, 'publish': 'C语言中文网'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
```
输出为
```
教程是:Python基础教程, 价格是:0000099.00, 出版社是:C语言中文网
教程是:C语言小白变怪兽, 价格是:0000159.00, 出版社是:C语言中文网
```


**当元素无重复时可直接创建字典来一一对应下标与元素**
```
hashmap = {}
for index, element in enumerate(nums):
    hashmap[element] = index
hashmap.get(element)#可以直接获得元素的下标值，若没有则返回None
若想让它在没有时返回0，可以:
hashmap=collections.defaultdict(int)
```

**可以创建一个字典来保存某列表中元素的个数**
```
need = collections.defaultdict(int)
for c in t:#t为某字符串
    need[c]+=1
```

### 1.3.3 python中的链表定义和操作

**链表定义**
```
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
#定义一个node
```

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

[H 指数 II](https://leetcode-cn.com/problems/h-index-ii/)

[分界思想解决有序数据的问题](https://www.bilibili.com/video/BV1d54y1q7k7/?spm_id_from=333.788.recommend_more_video.0/)
![](assets/imgs/屏幕截图%202022-03-31%20192840.png)
![](assets/imgs/屏幕截图%202022-03-31%20192935.png)

### 总结
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

## 4.2 双指针法
一般用于数组和链表的元素删除、移动

### 相关题目

#### 普通双指针法
[移除数组中的某个元素，要求空间复杂度为$O(1)$](https://leetcode-cn.com/problems/remove-element/)

[删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

[移动零(可以看看快排思想的解法)](https://leetcode-cn.com/problems/move-zeroes/)

[比较含退格的字符串(注意whlie>=0时等于号的取值意义)](https://leetcode-cn.com/problems/backspace-string-compare/)

[有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)

[三数之和](https://leetcode.cn/problems/3sum/)
注意高效去重的操作方法，[四数之和](https://leetcode.cn/problems/4sum/)方法类似(注意当循环为while时可以使用循环量+1来继续，但为for时要使用continue,同时注意利用前四个值之和和后三个值之和进行循环跳出和继续来节约时间)

#### 滑动窗口法
[长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)

[水果成篮](https://leetcode-cn.com/problems/fruit-into-baskets/)

[最小覆盖字串(注意理解)](https://leetcode-cn.com/problems/minimum-window-substring/)



### 总结
双指针法的关键是两个指针的位置如何移动，双指针可能分别在两端也可能都在一端，每个指针的移动操作需要根据具体的情况分析，例如[水果成篮](https://leetcode-cn.com/problems/fruit-into-baskets/)中慢指针的移动操作。

## 4.3 链表的一些技巧
主要包含元素删除、顺序调换、环形链表等

### 相关题目

**添加虚拟头节点**
[移除链表中的指定元素](https://leetcode-cn.com/problems/remove-linked-list-elements/)

**设计链表实现各种功能**
[设计链表](https://leetcode-cn.com/problems/design-linked-list/)
[翻转链表](https://leetcode.cn/problems/reverse-linked-list/)
[删除链表的倒数第n个节点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)
注意添加虚拟头节点以及快慢指针的操作
[链表相交](https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/)
注意遍历方法
[环形链表](https://leetcode.cn/problems/linked-list-cycle-ii/)
注意使用相对速度方法理解为什么环形链表快慢指针为何一定会相遇，为何能找到环入口，为何在慢指针走完一圈前一定会和快指针相遇。[理解](https://www.programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html#_142-%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8ii)

## 4.4 字符串


### 相关题目
[字符串反转](https://leetcode.cn/problems/reverse-string-ii/submissions/)
```
for i in range(0,n,k):
i = 0,k,2k,3k......
s[0:k] = s[0:k][::-1]
s = s[::-1]
```
[替换空格](https://leetcode.cn/problems/ti-huan-kong-ge-lcof/)
注意如果原地插入就每次都需要后移
![](assets/imgs/e6c9d24ely1go6qmevhgpg20du09m4qp.gif)
[翻转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/)
**KMP算法相关题目：**
[实现 strStr()](https://leetcode.cn/problems/implement-strstr/)
[重复的子字符串](https://leetcode.cn/problems/repeated-substring-pattern/)











