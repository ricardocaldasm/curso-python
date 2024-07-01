import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br/")
except urllib.error.URLError:
    print("Erro ao abrir o site.")
else:
    print("Site está acessível!")
