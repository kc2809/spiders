import json
import re

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

str1 = 'topic-456.html'
print(re.findall('\d+', str1)[0])


str2 = "http://www.pic-th.com/topic-611.html"
print(str2.split('/')[-1])

url2Form = "http://www.pic-th.com/$url"
arrx = []
[arrx.append(url2Form.replace("$url", str(i))) for i in range(1, 100)]
print(arrx)
