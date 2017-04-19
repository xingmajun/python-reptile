# coding=utf-8

from bs4 import BeautifulSoup
from selenium import webdriver

# 访问知乎新闻,爬虫爬数据


def get_infos_from_internet(url):

    driver = webdriver.PhantomJS()

    driver.get(url)

    beautiful_content = BeautifulSoup(driver.page_source, 'html.parser')

    box_items_tags = beautiful_content.find_all("div", class_="box")

    for box_item in box_items_tags:

        box_img_src = dict(box_item.select("img")[0].attrs)['src']

        print box_img_src

        # box_content = box_item.span.get_text()
        #
        # print box_content


get_infos_from_internet("http://daily.zhihu.com/")
