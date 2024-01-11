# editor 百年
# date: 2024/1/11 10:45
'''
思路不清晰导致的bug,建议注释或调试，打印输出，查看报错信息
'''
lst=[{'rating' :[9.7,2062397],'id':'1292052','type':['犯罪','剧情'],'title':'肖申克的救赎','actors':['蒂姆·罗宾斯','摩根·弗里曼']},
     {'rating':[9.6, 1528760],'id':'1291546','type':['剧情','爱情','同性'],'title':'霸王别姬','actors':['张国荣','张丰毅','巩俐','葛优']},
     {'rating' :[9.5, 1559181],'id' :'1292720','type':['剧情','爱情'],'title':'阿甘正传','actors':['汤姆·汉克斯','罗宾·怀特']}]
name=input('请输入你要查询的演员:')
# 遍历列表
for item in lst:
    # 指定一个对象act_lst接收字典中的演员（key）对应的值(value)
    act_lst=item['actors']
    # print(act_lst)
    '''
    输出演员列表
    ['蒂姆·罗宾斯', '摩根·弗里曼']
    ['张国荣', '张丰毅', '巩俐', '葛优']
    ['汤姆·汉克斯', '罗宾·怀特']

'''
    # for in 遍历演员列表，如果输入的演员在列表内
    for actor in act_lst:
        if name in actor:
            print(name,'出演了',item['title']) #就输出演员名+'出演了'+获取字典中的title(key)对应的值




    '''for movie in item:
        actors=movie['actors']
        if name in actors:
            print(name+'出演了'+movie)'''
