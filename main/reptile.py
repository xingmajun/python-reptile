# coding=utf-8

from bs4 import BeautifulSoup
from selenium import webdriver
import xlwt

# sample 访问途牛旅游网得到查询数据结果集


def get_infos_from_internet(url):

    driver = webdriver.PhantomJS()

    driver.get(url)

    beautiful_content = BeautifulSoup(driver.page_source, 'html.parser')

    li_items_tags = beautiful_content.find(liwithhan=u"category_列表页详情区域").find_all("li")

    trip_file = xlwt.Workbook()

    trip_sheet = trip_file.add_sheet(u"旅游", cell_overwrite_ok=True)

    trip_sheet.write(0, 0, u"名称")
    trip_sheet.write(0, 1, u"链接")
    trip_sheet.write(0, 2, u"价格")

    for index in range(0, len(li_items_tags)):
        li_item = li_items_tags[index]

        li_item_title = li_item.find("p", class_="title").get_text()
        trip_sheet.write(index+1, 0, li_item_title)
        li_item_a_href = dict(li_item.find("a", class_="clearfix").attrs)['href']
        link = 'HYPERLINK("%s")' % li_item_a_href
        trip_sheet.write(index+1, 1, xlwt.Formula(link))
        li_item_price = li_item.find("div", class_="tnPrice").get_text()
        trip_sheet.write(index+1, 2, li_item_price)

    trip_file.save("C:\\work\\test\\test.xls")

get_infos_from_internet("http://www.tuniu.com/zhoubian/erriyou/whole-nj-2/list-a20170430_20170501-h0-j0_0/")
