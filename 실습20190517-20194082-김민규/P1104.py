str = "    this is string example....wow!!!    "
print("원본 문자열=[" + str + "]")
print("rstrip()=["+str.rstrip()+"]")
print("lstrip()=["+str.lstrip()+"]")
print("strip()=["+str.strip()+"]")
print()

str = "    this is string example....wow!!!\n\t    "
print("원본 문자열=[" + str + "]")
print("rstrip()=["+str.rstrip()+"]")
print()

str = "88888888this is string example....wow!!!8888888"
print("원본 문자열=[" + str + "]")
print("rstrip('8')=["+str.rstrip('8')+"]")
print("lstrip('8')=["+str.lstrip('8')+"]")
print("strip('8')=["+str.strip('8')+"]")
print()

txt = "banana,,,,,ssaaww....."
print("원본 문자열=[" + txt + "]")
print("rstrip(',.asw')=[" + txt.rstrip(",.asw") + "}")
