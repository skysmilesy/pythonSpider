from selenium import webdriver
import requests
from io import BytesIO
from PIL import Image

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\gakataka\Student\recv\chromedriver")
driver.get("http://dun.163.com/trial/jigsaw")
# 最大化窗口
driver.maximize_window()
e = driver.find_element_by_css_selector(".is-right .u-mdtitle")
# 执行JavaScripts语句。arguments可以用来获取实际参数。
driver.execute_script("arguments[0].scrollIntoView();", e)
e = driver.find_element_by_css_selector(".is-right img.yidun_bg-img")
# 如果需要获取JavaScripts的返回值，使用JavaScripts中使用return 。
# rtn_value = driver.execute_script("return [arguments[0].width, arguments[0].height]", e)
# print(rtn_value)
response = requests.get(e.get_attribute("src"))
image = Image.open(BytesIO(response.content))
image.show()