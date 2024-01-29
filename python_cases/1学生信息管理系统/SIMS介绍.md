#SIMS学生信息管理系统(Students Information Management System)

## 系统开发环境

- 操作系统: Windows11
- 开发工具: Pycharm
- Python解释器版本: Python3.10
- Python内置模块:os,re

## 项目目录结构

![项目目录结构](D:\PYWORK\python_cases\1学生信息管理系统\文件结构.png)

## 需求分析

- 学生信息管理系统应该具备的功能
  - 添加学生及成绩信息
  - 将学生信息保存到文件当中
  - 修改和删除学生信息
  - 查询学生信息
  - 根据学生成绩进行排序
  - 统计学生的分数

## 系统设计

![SIMS结构图](D:\PYWORK\python_cases\1学生信息管理系统\SIMS_structure_chart.png)

## 系统业务流程

![SIMS业务流程](D:\PYWORK\python_cases\1学生信息管理系统\SIMS业务流程.png)

## 主函数设计

![SIMS主函数设计](D:\PYWORK\python_cases\1学生信息管理系统\SIMS主函数设计.png)

> ### 实现主函数


| 编号 | 功能                               |
| ------ | ------------------------------------ |
| 0    | 退出系统                           |
| 1    | 录入学生信息，调用insert()函数     |
| 2    | 查找学生信息，调用search()函数     |
| 3    | 删除学生信息，调用delete()函数     |
| 4    | 修改学生信息，调用modify()函数     |
| 5    | 对学生成绩排序，调用sort()函数     |
| 6    | 统计学生人数，调用total()函数      |
| 7    | 显示所有的学生信息，调用show()函数 |

## 学生信息维护模块设计

1. 实现从控制台录入学生信息，并将信息保存到磁盘文件当中

> ![录入学生信息实现](D:\PYWORK\python_cases\1学生信息管理系统\SIMS录入学生信息实现.png)
> 具体实现
>
>> save()函数，用于将学生信息保存到文件
>> insert()函数，用于记录学生信息
>>
2. 实现查询学生信息功能
> 从控制台录入学生ID或姓名，到磁盘文件中找到对应的学生信息
> ![查询_统计实现](D:\PYWORK\python_cases\1学生信息管理系统\SIMS查询_统计模块设计.png)
>具体实现
>> 编写主函数中调用的查找学生信息的函数search()
>> 定义显示查询结果的函数show_student(query_student)

3.实现从控制台找到学生信息，并将其删除
> ![删除信息实现](D:\PYWORK\python_cases\1学生信息管理系统\SIMS删除模块.png)
>具体实现 
>> 编写主函数中调用的修改学生信息的函数modify()
>> 调用了show()函数显示学生信息

4.实现修改学生信息功能
> 从控制台录入学生ID，到磁盘文件中找到对应的学生信息，将其进行修改
> ![修改学生信息实现](D:\PYWORK\python_cases\1学生信息管理系统\SIMS修改学生信息.png)  


## 项目打包

## 全部代码
