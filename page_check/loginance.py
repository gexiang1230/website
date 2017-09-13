# coding:utf8
from selenium import webdriver

# 导入浏览器驱动路径
executable_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"


# 指定是chrome 的驱动
# 执行到这里的时候Selenium会去到指定的路径将chrome driver 程序运行起来

driver = webdriver.Chrome(executable_path)

# get 方法 打开指定网址
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')


ele = driver.find_element_by_id("forecastID")

citysWeather = ele.text.split(u'℃\n')

lowest = 28
# lowestCitys = []  # 温度最低城市列表
for one in citysWeather:
    one = one.replace(u'℃','')
    print one
    curcity = one.split('\n')[0]
    lowweather = one.split('\n')[1].split('/')[0]
    lowweather = int(lowweather)
    # 发现气温更低的城市
    if lowweather<lowest:
        lowest = lowweather
        lowestCity = [curcity]
    #  温度和当前最低相同，加入列表
    elif lowweather ==lowest:
        lowestCity.append(curcity)


print u'温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestCity))

driver.quit()