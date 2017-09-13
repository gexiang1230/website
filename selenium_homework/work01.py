# coding:utf-8
from selenium import webdriver
import re


exe_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver=webdriver.Chrome(exe_path)
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
driver.implicitly_wait(10)#添加隐式等待，等待获取网页上面的内容
# forecasts=driver.find_element_by_xpath("//div[@id='forecastID']/dl[1]")# 注意这里是查第1个不是第二个
# forecasts=driver.find_element_by_xpath("//div[@id='forecastID']/dl[last()]")# 查找最后一个元素
forecasts=driver.find_element_by_id('forecastID').text# 查找id=forecastID
forecast=re.split(u'℃\n', forecasts)
print forecast
lowest=100
#lowcitys=[]
for one in forecast:
   one=one.replace(u'℃','')
   lowestweather=one.split('\n')[1].split('/')[1]
   lowestcity = one.split('\n')[0]
   lowestweather=int(lowestweather)
   if lowestweather<=lowest:
       lowest=lowestweather
       lowestCity = [lowestcity]
       #  温度和当前最低相同，加入列表
   elif lowestweather== lowest:
       lowestCity.append(lowestcity)

print u'当前气温最低的城市是{0},最低气温的城市是{1}'.format(lowest,' '.join(lowestCity)) #前面一定要加u，表示为unicode
# print u'当前气温最低的城市是%s,最低气温的城市是%d' %(' '.join(lowestCity,lowest))
# print u'温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestCity))




driver.close()