from django.shortcuts import render
import myblog.settings as st
from myblog.settings import homepage_path

# Create your views here.
def home_index( request ):
    # temp_path = "article/index.html"
    temp_path = st.homepage_path_temp
    temp_path = homepage_path
    temp_path = "article/show.html"
    temp_path = "article/404.html"
    html_data = dict()
    # head images
    head_imgs = st.head_images
    # article list1: latest release article
        # 主题
        # 标题
        # 图片
        # 日期
        # 浏览量
        # 评论数
        # 简述
    article_dict1 = {
        "title":"用DTcms做一个独立博客网站hjgz",
        "theme":"MZ-NetBlog主题hjz",
        "img": "images/201610181739277776.jpg",
        "release_day":"2020-10-14",
        "views_number":300,
        "commends_number":100,
        "sketch":"采用DTcms V4.0正式版（MSSQL）。开发环境：SQL2008R2+VS2010。DTcms V4.0正式版功能修复和优化：1、favicon.ico图标后台上传。（解决要换图标时要连FTP或者开服务器的麻烦）"
        }



    # article list2: Latest comments article list 
        # 标题
        # 发表日期
        # 浏览量
        # 图片

    # run day-number

    # article number

    # 推荐文章

    numbers = [ i for i in range(10)]
    img_1 = "images//201610181557196870.jpg"
    html_data["head_imgs"] = head_imgs
    html_data['numbers'] = numbers
    html_data["img1"] = img_1
    html_data[ "articles_list1" ] = [ article_dict1, article_dict1, article_dict1] 
    html_data[ "articles_list2" ] = [  article_dict1, article_dict1] 
    return render( request, temp_path, html_data )


def article_detail( request ):
    print( "detail ")
    temp_path = "article/show.html"
    return render( request, temp_path )
    
def article_list( request):
    print( "list ")
    temp_path = "article/list.html"
    return render( request, temp_path )

def page_notfound( request ):
    temp_path = "article/404.html"
    return render( request, temp_path)
    