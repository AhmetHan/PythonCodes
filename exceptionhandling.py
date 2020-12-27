import urllib.request
import urllib.error

try:
    url=input("Bir url adresi giriniz:")
    response=urllib.request.urlopen(url)
    for line in response:
        print(line.strip())
except urllib.error.URLError as e:
    print("Url hatasi:",e.reason)
except ValueError:
    print("Gecerli bir url adresi giriniz!")