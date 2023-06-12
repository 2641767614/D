import requests
from io import BytesIO
from PIL import Image

# 图片URL
image_url = "https://example.com/images/example.jpg"

# 通过requests库获取图片二进制数据
response = requests.get(image_url)

# 将二进制数据转换为Image对象并显示
img = Image.open(BytesIO(response.content))
img.show()