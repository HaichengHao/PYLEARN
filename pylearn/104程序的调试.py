# editor 百年
# date: 2024/1/11 20:40
'''
断点：
程序运行到此处，暂时挂起，停止执行，可详细观察程序的运行情况

调试视图触发的3种常见方式：
1单击调试按钮
2在编辑区右键，选择调试
3快捷键 shift + F9

'''
# 经典99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'={0}'.format(i*j),end='\t')
    print()
