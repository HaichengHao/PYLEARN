#### 详细的文档介绍：[List of Chromium Command Line Switches « Peter Beverloo![icon-default.png?t=LA92](https://csdnimg.cn/release/blog_editor_html/release1.9.5/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=LA92)https://peter.sh/experiments/chromium-command-line-switches/](https://peter.sh/experiments/chromium-command-line-switches/ "List of Chromium Command Line Switches « Peter Beverloo") 

#### eg: 

**chrome\_options.add\_argument('--incognito')              # 设置Chrome为隐身模式（无痕模式）**

```python
--allow-outdated-plugins             不停用过期的插件。
--allow-running-insecure-content     默认情况下，https 页面不允许从 http 链接引用 javascript/css/plug-ins。添加这一参数会放行这些内容。
--allow-scripting-gallery            允许拓展脚本在官方应用中心生效。默认情况下，出于安全因素考虑这些脚本都会被阻止。
--disable-accelerated-video          停用 GPU 加速视频。
--disable-dart                       停用 Dart。
--disable-desktop-notifications      禁用桌面通知，在 Windows 中桌面通知默认是启用的。
--disable-extensions                 禁用拓展。
--disable-file-system                停用 FileSystem API。
--disable-preconnect                 停用 TCP/IP 预连接。
--disable-remote-fonts               关闭远程字体支持。SVG 中字体不受此参数影响。
--disable-speech-input               停用语音输入。
--disable-web-security               不遵守同源策略。
--disk-cache-dir                     将缓存设置在给定的路径。
--disk-cache-size                    设置缓存大小上限，以字节为单位。
--dns-prefetch-disable               停用DNS预读。
--enable-print-preview               启用打印预览。
--extensions-update-frequency        设定拓展自动更新频率，以秒为单位。
--incognito                          让浏览器直接以隐身模式启动。
--keep-alive-for-test                最后一个标签关闭后仍保持浏览器进程。（某种意义上可以提高热启动速度，不过你最好得有充足的内存）
--kiosk                              启用kiosk模式。（一种类似于全屏的浏览模式）
--lang                               使用指定的语言。
--no-displaying-insecure-content     默认情况下，https 页面允许从 http 链接引用图片/字体/框架。添加这一参数会阻止这些内容。
--no-first-run                       跳过 Chromium 首次运行检查。
--no-referrers                       不发送 Http-Referer 头。
--no-sandbox                         彻底停用沙箱。
--no-startup-window                  启动时不建立窗口。
--proxy-pac-url                      使用给定 URL 的 pac 代理脚本。（也可以使用本地文件，如 --proxy-pac-url="file:\\\c:\proxy.pac"）
--proxy-server                       使用给定的代理服务器，这个参数只对 http 和 https 有效。（例如 --proxy-server=127.0.0.1:8087 ）
--single-process                     以单进程模式运行 Chromium。（启动时浏览器会给出不安全警告）
--start-maximized                    启动时最大化。
--user-agent                         使用给定的 User-Agent 字符串
 
参数：--user-data-dir=UserDataDir
用途：自订使用者帐户资料夹（如：–user-data-dir="D:\temp\Chrome User Data"）
参数：--process-per-tab
用途：每个分页使用单独进程
参数：--process-per-site
用途：每个站点使用单独进程
参数：--in-process-plugins
用途：插件不启用单独进程
 
参数：--disable-popup-blocking
用途：禁用弹出拦截
参数：--disable-javascript
用途：禁用JavaScript
参数：--disable-java
用途：禁用Java
参数：--disable-plugins
用途：禁用插件
参数：–disable-images
用途：禁用图像
参数：--omnibox-popup-count=”num”
用途：将网址列弹出的提示选单数量改为num个
参数：--enable-vertical-tabs
用途：调整chrome游览器标签存放在左边，非顶部
```

