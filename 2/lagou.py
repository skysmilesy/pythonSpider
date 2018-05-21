import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
response = requests.get("https://www.lagou.com/zhaopin/Python/?labelWords=label", headers=headers)
response.encoding = "utf-8"
print(response.text)
print(response.request.headers)