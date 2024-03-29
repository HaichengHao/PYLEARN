# editor 百年
# date: 2024/1/18 17:24
'''
以主程序形式运行
在每个模块的定义中都包含一个记录模块名称的变量_name_,程序可以检查该变量，
以确定它们在哪个模块中执行。如果一个模块不是被导入到其它程序中执行，那么它可能在解释器的顶级模块中执行。
顶级模块的_name_变量的值为_main_

if __name__ = '__main__':
pass
'''
import calc
print(calc.add(100,1000))
'''
输出结果: 
30 #我们不想输出模块calc中的语句
1100
'''
# 思考，该如何解决这个问题
# 答：在模块中修改，将print(add(20,30))作为主程序运行

# 修改calc.py后再次运行的结果如下
# 1100  <--发现不再输出print(add(20,30))
