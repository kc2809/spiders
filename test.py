import json

x = '{"name": "John", "age": 30, "city": "New York"}'

t = ''
try:
    y = json.loads(t)
    print(y['name'])
    pass
except ValueError:
    print('EXCEPTION')
    pass


html = ""
if not html:
    print('khong co string')
else:
    print('co tri')

urlFormat = "http://www.pic-th.com/ajax/load.php?action=load_all&page=$pageId"
urlArr = []
for i in range(1, 100):
    urlArr.append(urlFormat.replace("$pageId", str(i)))

print(urlArr)

