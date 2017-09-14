# coding:utf-8
from selenium import  webdriver
from time import sleep
exepath=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver=webdriver.Chrome(exepath)
driver.get('http://music.baidu.com/top/new')
# lists=driver.find_elements_by_class_name("song-item")
lists=driver.find_elements_by_id('songListWrapper')

# for one in lists:
#     print one.text
# songs=driver.find_elements_by_xpath('//span[@class="song-title "]')
# authers=driver.find_elements_by_xpath('//span[@class="author_list"]')
driver.implicitly_wait(5)

for li in lists:
  uplists =li.find_elements_by_class_name("up")# 如果有up的

  if uplists:
    song =li.find_element_by_xpath('.//span[@class="song-title "]').text
    auther = li.find_element_by_xpath('.//span[@class="author_list"]').text
    # 在上面的求解auther的时候，没有加点就查到的是第一个，参考https://github.com/seleniumhq/selenium/issues/3203获得解决方案
    # //虽然官方是说的是相对路径下找，不管位置，但是上面的语句没有加点就是找不到，因为他是找的根目录的节点
    print  u'{:10s}:{}'.format(song,auther)

driver.quit()




