# editor 百年
# date: 2023/12/30 15:41
# 会员卡折扣
'''
会员：>=200 8折
     >=100 9折
     <100 不打折

非会员 >=200 9.5折
      <200 不打折
'''

answer=input('请问您有会员卡吗?(y/n)')
money=float(input('您的付款金额为:'))
if answer =='y':
    if money>=200:
        money=money*0.8
        print('您的付款金额为:',money)
    elif 100<=money<200:
        money=money*0.9
        print('您的付款金额为:',money)
elif answer == 'n':
    if money>=200:
        money*=0.95
        print('您的付款金额为:',money)
    else:
        print('您的付款金额为:',money)

