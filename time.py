import requests

city = input("请输入城市名：")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"{city}的天气状况：{desc}，温度：{temp} K")
else:
    print("请求失败，请重试")