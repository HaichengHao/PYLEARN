# editor 百年
# date: 2024/1/18 17:01

# 导入自定义的模块127mymod1
# 如果直接写import 127mymod1会报错
try:
    import mymod127
    print('模块导入成功')
except BaseException as e:
    print(e)
    # No module named 'mymode127' <--捕获异常信息，提示无次模块，那么如何解决问题
    '''
    需要将目录文件标记为源根 Mark Directory as Source Root'''
    # 再次尝试运行
#     模块导入成功

# 开始调用自定义模块中的方法
import mymod127
# 调用mymod127中的divn(除法)
print(mymod127.divn(6,3))

try:
    print(mymod127.divn(2,0))
except BaseException as e:
    print(e)
    # 零不能作为除数

