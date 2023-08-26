from geopy.geocoders import Nominatim

# 创建Geocoder对象
geolocator = Nominatim(user_agent="my_location_app")

# 查询位置信息
location = geolocator.geocode("北京大学")

# 提取纬度和经度
print((location.latitude, location.longitude))