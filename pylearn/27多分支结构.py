# editor 百年
# date: 2023/12/30 15:27
# 题目：成绩评比
grade=int(input('请输入你的成绩'))
if grade>=90 and grade<=100:
    print('你的成绩评比为A')
elif grade>=80 and grade<90:
    print('你的成绩为B')
elif grade>=70 and grade<80:
    print('你的成绩为C级')
elif grade>=60 and grade<70:
    print('你的成绩为D级')
elif grade>=0 and grade<60:
    print('你的成绩为E级')
elif grade>100 or grade<0 :
    print('输入的成绩有明显错误，请重新输入')