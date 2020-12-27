import urllib.request

response=urllib.request.urlopen('https://www.haberler.com/')

print('Url:\n',response.geturl())

print("Reading content:\n")

for line in response:
    print(line.strip())