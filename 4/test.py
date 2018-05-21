from PIL import Image, ImageEnhance, ImageFilter, ImageChops

import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="")
driver.get("")
e = driver.find_element_by_css_selector("")
# e.location  {"x":,   "y":}
# e.size    {"width": , "height":}
# e.rect


# e.location["x"]
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.ID, "tcaptcha_popup")))
wait.until(expected_conditions.visibility_of_element_located((By.ID, "tcaptcha_popup")))
wait.until(expected_conditions.element_to_be_clickable((By.ID, "tcaptcha_popup")))
# 不建议使用了
# driver.switch_to_frame()
# 切换到内部窗体。
driver.switch_to.frame(driver.find_element_by_id("frame_id"))

bg = driver.find_element_by_id("slideBkg")
# 很可能取出的就是一个None，因为src属性是动态生成的。
# src = bg.get_attribute("src")
wait.until(lambda d: bg.get_attribute("src"))
src = bg.get_attribute("src")


# 难以程度：
# 网易 < 腾讯 < 极验

# 腾讯与网易的不同之处：
# 1 腾讯的图片不是原始的大小，需要我们自行处理，进行缩放。
# 2 腾讯的弹窗会产生一个IFrame（内部窗体）。需要我们进行切换到内部窗体中处理。
# 3 腾讯Img对象的src属性是动态生成的，需要我们使用wait 【wait.until(lambda d: bg.get_attribute("src"))】进行等待。
# 4 腾讯的滑块图片没有与背景图像等高（不同于易盾），需要我们自己进行计算剪切位置。
# 5 腾讯的滑块不是处于最左边的位置。我们需要对该偏移量进行处理。

