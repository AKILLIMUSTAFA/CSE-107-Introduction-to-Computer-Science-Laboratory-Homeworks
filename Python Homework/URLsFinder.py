
import urllib2
import re


def getAllLinksFromWebSite(url):
    #connect to a URL
    website = urllib2.urlopen(url)

    #read html code
    html = website.read()

    #use re.findall to get all the links
    links = re.findall('"((http|ftp)s?://[a-z,A-Z,0-9]+.*?)"', html)

    resultLinkListesi = []
    
    for link, type in links:
        if not (link in resultLinkListesi):
            resultLinkListesi.append(link)
    
    return resultLinkListesi


site = raw_input("Please give a URL begin with 'http://www' :")


linkler = getAllLinksFromWebSite(site)

LinkDosyasi = open("Links.txt", "w")

for i in linkler:

    LinkDosyasi.write(i+"\n")


LinkDosyasi.close()

try:
    satir = int(raw_input("How many links for the process: "))

except ValueError:
    print "Please not give a double or a string. It must be a integer!"
    satir = int(raw_input("How many links for the process: "))

c = 0
b = 0
while b < satir:
    b += 1
    c += 1
    LinkDosyasi = open("Links.txt", "a+")
    a = 0
    while a < c:
        a += 1
        linklers = getAllLinksFromWebSite(LinkDosyasi.readline())
    LinkDosyasi.close()
    LinkDosyasi = open("Links.txt", "a+")
    for i in linklers:
        LinkDosyasi.write(i+"\n")
    LinkDosyasi.close()


