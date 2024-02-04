# editor: 百年
# time: 2024/2/2 17:18
# 导入urllib包的request模块
import urllib.request

# 1可以下载一个网页 ,利用.urlretrieve([url, filename=None, reporthook=None, data=None]) 方法
'''url_page='http://www.baidu.com'
urllib.request.urlretrieve(url_page,filename='./demo.html')
'''
    # 这样就把网页下载下来了

# 2下载图片
'''url_pic='https://img.3dmgame.com/uploads/images/news/20190905/1567677085_876493.jpg'
urllib.request.urlretrieve(url_pic,filename='./ngzk.png')'''
# 3下载视频
url_video='http://vod.v.jstv.com/2024/02/03/JSTV_JSWSNEW_1706933253068_Dx0Hz51_1339.mp4'
urllib.request.urlretrieve(url_video,filename='./demo.mp4')