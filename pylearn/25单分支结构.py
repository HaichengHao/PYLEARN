# editor 百年
# date: 2023/12/30 14:49
# 选择结构
mony=10000
q=int(input('请输入取款金额:'))
if q<=mony & q>0:
    mony=mony-q
    # 或者可以写为mony-=q
    print('您的银行卡余额为:'+str(mony)+'元')
else:
    print('请输入正确的存款金额')
