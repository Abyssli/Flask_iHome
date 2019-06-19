# 静态文件接口
- 提供静态文件的蓝图代码
    ```python
    # coding: utf-8

    from flask import Blueprint, current_app
    
    # 提供静态文件的蓝图
    html = Blueprint("web_html", __name__)
    
    # 127.0.0.1:5000/
    # 127.0.0.1:5000/index.html
    # 127.0.0.1:5000/register.html
    # 127.0.0.1:5000/favicon.ico  # 浏览器认为的网站标识,浏览器会自己请求这个资源
    
    @html.route("/<re(r'.*'):html_file_name>")
    def get_html(html_file_name):
    """提供html文件"""
    # 如果html_file_name为”“， 表示访问的路径是/, 请求的是主页
    if not html_file_name:
        html_file_name = "index.html"

    # 如果资源名不是favicon.ico
    if html_file_name != "favicon.ico":
        html_file_name = "html/" + html_file_name

    # flak提供的返回静态文件的方法
    return current_app.send_static_file(html_file_name)
    ```
- 定义正则万能转换器
    ```python
    # 定义正则转换器
    class ReConverter(BaseConverter):
        """定义正则转换器"""
        def __init__(self, url_map, regex):
            # 调用父类的初始化方法
            super(ReConverter, self).__init__(url_map)
            # 保存正则表达式
            self.regex = regex
    ```
- 在启动文件ihome/\_\_init\_\_.py中为flask添加自定义转换器  
    `# 为flask添加自定义的转换器`  
    `from ihome.utils.commons import ReConverter`  
    `app.url_map.converters["re"] = ReConverter`