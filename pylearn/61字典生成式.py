# editor 百年
# date: 2024/1/4 14:18
'''
内置函数zip()
用于将可迭代对象作为参数，将对象中对应的元素打包成一个元组，
然后返回由这些元组组成的列表
'''
# 用法
# 定义键
goods=['香蕉','李子','葡萄']
# 定义值
prices=[10,15,20]

dic1={goods:prices for goods,prices in zip(goods,prices)}
print(dic1)
# {'香蕉': 10, '李子': 15, '葡萄': 20}


# 如果元素个数并不相同怎么办?
nprices=[10,20,30,40]

dic2={goods:nprices for goods,nprices in zip(goods,nprices)}
print(dic2)
# {'香蕉': 10, '李子': 20, '葡萄': 30}
# 发现zip()会按顺序来存储

# 若是少的情况怎么办
sprices=[10,20]
dic3={goods:sprices for goods,sprices in zip(goods,sprices)}
print(dic3)
# {'香蕉': 10, '李子': 20} <--zip()非常的‘聪明’
dic3.clear()
print(dic3)

# 删除香蕉
del dic2['香蕉']
print(dic2)
# 修改葡萄价格,增加沙糖桔
dic2['葡萄']=6
dic2['沙糖桔']=5
print(dic2)
# {}
# {'李子': 20, '葡萄': 30}
# {'李子': 20, '葡萄': 6, '沙糖桔': 5}