# editor: 百年
# time: 2024/1/26 11:39

# 定义一个函数，实现菜单界面
def menu():
    print("===============++=SIMS=++=================")
    print("==============学生信息管理系统==================\n")
    print("|-----------功能菜单---------------|")
    print("1.\t\t\t\t\t\t录入学生信息\n2.\t\t\t\t\t\t查找学生信息\n3.\t\t\t\t\t\t删除学生信息\n"
          "4.\t\t\t\t\t\t修改学生信息\n5.\t\t\t\t\t\t对学生成绩进行排序\n6.\t\t\t\t\t\t统计学生人数\n7.\t\t\t\t\t\t显示所有的学生信息\n")


# 定义主函数
def main():
# 实现菜单滞留和功能选择
# 利用while循环来实现，如果结束当前循环即为break时结束服务
    while True:

        # 调用menu()函数实现功能选择菜单滞留
        menu()
#       #实现功能选择交互
        choice=int(input('请输入对应功能的数字'))
        if choice in [i for i in range(0,8)]:
            if choice==0:
#                 退出系统
                ansewer=print("是否退出(y/n)?")
                if ansewer=='y' or 'Y':
                    print('感谢使用')
                    break #结束循环，退出系统
                elif ansewer=='n' or 'N':
                    continue #继续循环
            # 如果选择1，调用insert()函数，插入学生信息
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
        else:
            print('请重新输入正确的数字')

# 分别定义要实现的函数
# 1
def insert():
    pass
# 2
def search():
    pass
# 3
def delete():
    pass
# 4
def modify():
    pass
# 5
def sort():
    pass
# 6
def total():
    pass
# 7
def show():
    pass


# 以主程序方式运行
if __name__ == '__main__':
    main()

