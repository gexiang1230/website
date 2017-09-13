# coding=utf-8#
#导入webdriver模块
from selenium  import  webdriver
from time import sleep

execute_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
equal_string='2016 © 南京老人佳智能科技有限公司'
driver=webdriver.Chrome(execute_path)

driver.get('http://itest.chinacloudapp.cn:8280/')


login_url=driver.current_url
driver.find_element_by_id('userName').send_keys('ly')
driver.find_element_by_id('password').send_keys('ly123!@#')

#driver.find_element_by_css_selector('button[onclick*="doLogin"]').click()
driver.find_element_by_tag_name('button').click()

sleep(2)


homepage_url=driver.current_url

if homepage_url==login_url:
    print '登陆失败'
else:
    print '登陆成功'

# 检查版本信息

try:
   ele=driver.find_element_by_class_name("copyright").text
   print ele
 # 使用文字对比的时候，需要考虑编码
   if ele == equal_string.decode('utf-8'):
       print '版本信息正确'
   else:
       print '版本信息错误'
except:
       print '版本信息错误'
driver.close()



