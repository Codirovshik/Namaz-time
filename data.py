import requests
from bs4 import BeautifulSoup

times = [range(6)]
fajr = " "
sunrise = " "
dhuhr = " "
asr = " "
maghrib = " "
isha = " "

url = 'https://govzalla.com/%D0%BB%D0%B0%D0%BC%D0%B0%D0%B7%D0%B0%D0%BD-%D1%85%D0%B5%D0%BD%D0%B0%D1%88-%D0%B2%D1%80%D0%B5%D0%BC%D1%8F-%D0%BC%D0%BE%D0%BB%D0%B8%D1%82%D0%B2/'
try:
    info = requests.get(url)
    soup = BeautifulSoup(info.text, 'html.parser')
    fajr = soup.find('h4').text
    sunrise = soup.find('h4').findNext('h4').text
    dhuhr = soup.find('h4').findNext('h4').findNext('h4').text
    asr = soup.find('h4').findNext('h4').findNext('h4').findNext('h4').text
    maghrib = soup.find('h4').findNext('h4').findNext('h4').findNext('h4').findNext('h4').text
    isha = soup.find('h4').findNext('h4').findNext('h4').findNext('h4').findNext('h4').findNext('h4').text
    times = [fajr, sunrise, dhuhr, asr, maghrib, isha]

    wfile = open("times.txt", "w")
    wfile.writelines("%s\n" % i for i in times)
    wfile.close()
except requests.ConnectionError:
    wfile = open("times.txt", "r")
    times = wfile.readlines()
    wfile.close()




