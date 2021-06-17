import requests

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

url = "https://gnatsstg/web/default/one-click"
fin = open('C:/Users/mbasha/Desktop/foo.txt', 'rb')
files = {'file': fin}
try:
    r = requests.post(url, files=files)
    print r.text
finally:
    fin.close()
