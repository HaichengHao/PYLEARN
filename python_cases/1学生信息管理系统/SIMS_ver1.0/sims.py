# editor: 百年
# time: 2024/1/26 11:39
# 定义要保存成的文件
# file_name='stu_info.txt'
file_name='D:/PYWORK/python_cases/1学生信息管理系统/SIMS_ver1.0/stu_info.txt'
# 定义主函数
func_lst = [i for i in range(0,8)]
def main():
    while True:
        menu()
        choice=int(input('请选择功能:'))
        if choice in func_lst:
            if choice==0:
                answer=input('确定退出吗？')
                if answer == 'y' or answer == 'Y':
                    print('感谢使用')
                    break
                elif answer == 'N' or answer == 'n':
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        else:
            print('请输入正确的数字')
            continue




# 定义一个函数，实现菜单界面
def menu():
    print("===============++=SIMS=++=================")
    print("==============学生信息管理系统==================\n")
    print("|-----------功能菜单---------------|")
    print("1.\t\t\t\t\t\t录入学生信息\n2.\t\t\t\t\t\t查找学生信息\n3.\t\t\t\t\t\t删除学生信息\n"
          "4.\t\t\t\t\t\t修改学生信息\n5.\t\t\t\t\t\t对学生成绩进行排序\n6.\t\t\t\t\t\t统计学生人数\n7.\t\t\t\t\t\t显示所有的学生信息\n")


# 定义一个save函数，用于存储信息
def save(lst):
    try:
        fp=open(file_name,'a',encoding='utf-8')
    except:
        # fp=open('D:/PYWORK/python_cases/1学生信息管理系统/SIMS_ver1.0/stu_info.txt','w',encoding='utf-8')
        fp=open(file_name,'w',encoding='utf-8')
    for item in lst:
        fp.write(str(item)+'\n')
        #关闭文件
    fp.close()

# 1实现insert()函数
def insert():
    stu_lst=[]
    while True: #循环输入
        id=input('请输入学生id（如1001）:')
        # 空字符串的布尔值为False,所以if not id 即如果字符串为空则提示重新输入
        if not id:
            print('请重新输入')
            break
        name=input('请输入学生姓名:')
        if not name:
            print('请重新输入')
            break
        try:
            chinese=int(input('语文成绩:'))
            math=int(input('数学成绩:'))
            english=int(input('英语成绩:'))
        except:
            print('请重新输入正确的成绩')
            continue
        stu_info={'id':id,'姓名':name,'语文':chinese,'数学':math,'英语':english}
        stu_lst.append(stu_info)
        answer=input('是否继续添加?')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            print('学生信息录入完毕!')
            break
    # 调用save()函数
    save(stu_lst)



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

