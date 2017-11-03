import urllib.request
import re

link = "link"
filename = "filename" #must exist in the working directory


url = link.replace('gallery', 'a') + "?grid"
f = urllib.request.urlopen(url)
st = str(f.read())
x = re.findall('{\"hash\".*?:\d\d\"', st)

count = 1
for g in x[:len(x)//2]:
    hash1 = re.findall('\"hash\":\"(.*?)\",', g)
    type1 = re.findall('\"ext\":\"\.(...)', g)
    url2 = "http://i.imgur.com/" + hash1[0] + "." + type1[0]
    urllib.request.urlretrieve(url2, "C:\\users\\Mustafa\\desktop\\" + filename + "\\" + str(count) + ".jpg")
    count += 1
