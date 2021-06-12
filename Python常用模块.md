## heapq

> from heapq import #
>
> python heapq 模块中76个函数：

### 1. heapify(heap) 

​		将列表转化为堆，python中默认创建小根堆(min-heap)

```python
from heapq import *
heap = [5, 8, 0, 4, 6, 7]
heapify(heap)
print(heap)
# [0, 4, 5, 8, 6, 7]
```

### 2. heappush(heap,  x)

​		向堆中添加元素x

```python
heappush.push(heap, 1)
print(heap)
# [0, 4, 1, 8, 6, 7, 5]
```

### 3. heappop(heap)

​		弹出堆顶元素

```python
print(heappop(heap))
# 0
```

### 4.heapreplace(heap, x)

​		先弹出堆顶元素，再插入元素x

```python
heapreplace(heap, -1)
print(heap)
# [-1, 4, 5, 8, 6, 7]
```

### 5. heappushpop(heap, x)

​		先插入元素x, 在弹出堆顶元素

```python
heappushpop(heap, -2)
print(heap)
# [-1, 4, 5, 8, 6, 7]
```

### 6. nlargest(n, iter)   nsmallet(n, iter)

​		用来寻找任何可迭代对象iter中的前n个最大的或前n个最小的元素。

```python
from heapq import *
lst = [5, 8, 0, 4, 6, 7]
print(nsmallest(3, lst))
# [0, 4, 5]
print(nlargest(3, lst))
# [8, 7, 6]
```

