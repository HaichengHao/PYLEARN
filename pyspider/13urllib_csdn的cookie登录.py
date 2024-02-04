# editor: 百年
# time: 2024/2/4 15:57
# 适用的场景:数据采集的时候，需要绕过登录，然后进入到某个页面
# 什么情况下访问不成功？请求头的信息不够，所以访问不成功
import urllib.request
# url='https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F'
# url='https://blog.csdn.net/weixin_45938063?spm=1000.2115.3001.5343'
blog_url='https://blog.csdn.net/weixin_45938063/article/details/135975622?spm=1001.2014.3001.5501'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
# 'cookie':'_T_WM=38203987059; WEIBOCN_FROM=1110006030; SUB=_2A25Iuz4zDeRhGeFN71AX9yzNyD-IHXVruT_7rDV6PUJbktAGLW7QkW1NQDFRlWelB14URQC5hzLOotX7XxpawSlC; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5T6oo4dm4fuT8CvbpMwRZT5JpX5KzhUgL.FoM0ShzcS0zpe0e2dJLoIE5LxKqLBK2L1heLxKBLBonL12zLxKnLBo.L122peoeNe5tt; SSOLoginState=1707036261; ALF=1709628261; MLOGIN=1; XSRF-TOKEN=4cca7a; M_WEIBOCN_PARAMS=oid%3D4997730340700391%26lfid%3D102803%26luicode%3D20000174%26uicode%3D20000174; mweibo_short_token=3ef56f20a8'
'cookie':'uuid_tt_dd=10_37193282020-1639827461736-189161; UN=weixin_45938063; __bid_n=1863902fac9ede313b4207; FPTOKEN=rsh0EoFWnDIgCPvySFJe2MavXUzvsGb4NnALNWJC/qWdm/mgUuEQbE9WOFoTL6+0PYuaM5i3tJS9MtmmSD5CxLnaohOS4oQW9d2Zd0ETYZ3JbnPocxE2mE57YtTOY448QkMsS0ATPdXiwQ/+Jj/N5YZWkDcUl/5Jv2alEZU6O8GWMDjoa6cu46GlUJne6+9TYHijeLyBU7mkUteqSVI7v+utZPGXE1+yWy9lpeG7PHT6MA00rtENCCy2r5afU6efrcr3PyEtg0i13azgObYWjS8pSB6hi5oWavhW0Txmcyu1LeOQHaCHszM2Js6Oa5G1LetM4lLK2m2zdcBJXnMfToZ3Ll+QOUKe5dMoVY0XpNH6AmFBjJdxINHFYsyuy1QTNlSs9GuPzhfJ4WCaUSizsA==|fwdMnSc2sqvYlnzGKpxNsd7dSS8U4rJfzMdbSt54dk0=|10|d3d5e7695af8cf456e2cba16b9129f74; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1680359359; fpv=b8bbda9c38b4e4a8b3b6db825a46c3c4; UserName=weixin_45938063; UserInfo=0ba7b4c7a9ce4a4aa630c5c55e4de349; UserToken=0ba7b4c7a9ce4a4aa630c5c55e4de349; UserNick=%E7%99%BE%E5%B9%B4%E0%A9%AD+%E1%90%95%29%E0%A9%AD*%E2%81%BE%E2%81%BE; AU=A14; BT=1700362732086; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22weixin_45938063%22%2C%22scope%22%3A1%7D%7D; c_adb=1; c_ins_um=-; c_dl_prid=1705458004825_589270; c_dl_rid=1705926039279_289809; c_dl_fref=https://so.csdn.net/so/search; c_dl_fpage=/download/weixin_44604586/12503429; c_dl_um=distribute.pc_search_result.none-task-blog-2%7Eall%7Etop_positive%7Edefault-1-126002741-null-null.142%5Ev99%5Epc_search_result_base3; c_ins_prid=1703900229846_880789; c_ins_rid=1706006242542_318075; c_ins_fref=https://mp.csdn.net/mp_blog/manage/article; c_ins_fpage=/?utm_source=636161750&spm=1011.2415.3001.9242; weixin_45938063comment_new=1706167725371; creative_btn_mp=3; firstDie=1; c_pref=default; c_first_ref=default; c_first_page=https%3A//www.csdn.net/; c_segment=9; https_waf_cookie=3b66c524-1861-46f8af742e602e453b51b177a20f5afadca1; dc_sid=dd8d8cc55efa16cee8f49e717080a148; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1706944220,1706960613,1707035406,1707037646; c_dsid=11_1707037748818.869486; log_Id_click=867; c_ref=https%3A//www.csdn.net/; c_page_id=default; log_Id_pv=845; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1707037752; dc_session_id=10_1706970785719.783399; dc_tos=s8bqrf; log_Id_view=11241; waf_captcha_marker=60f3cdc0093025c62064d4ff82293c80b920a33c4390eee547a3a7997f7d30cc'
}
request=urllib.request.Request(url=blog_url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)

with open('./someone_blog.html','w+',encoding='utf-8') as wfp:
    wfp.write(content)
