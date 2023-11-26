import requests

def main():
    url = "https://www.baidu.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("成功访问百度网站！")
    else:
        print("访问百度网站失败！")

if __name__ == "__main__":
    main()