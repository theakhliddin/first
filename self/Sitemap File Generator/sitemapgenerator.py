import urllib.parse
from pip._vendor import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib
import xml.etree.ElementTree as ET

class SitemapGenerator:

    def __init__(self, root, filename):
        self.filename = filename
        self.urls = {}
        self.root = root
        self.hostname = urlparse(root).hostname

    def crawl(self, url, level):
        print("Level " + str(level) + "/ Explore" + url)

        page = requests.get(url)

        if page.status_code == 200:
            url = urllib.parse.urldefrag(url)[0]

            if url not in self.urls:
                self.urls[url] = level

                soup = BeautifulSoup(page.content, "html.parser")

                for link in soup.findAll('a'):
                    try:
                        href = link.get('href')
                        result = urlparse(href)
                        newurl = None

                        if result.hostname == None and href is not None:
                            newurl = self.root + ("/", "")[href.startswith("/")] + href;
                        elif result.hostname == self.hostname:
                            newurl = href;
                        if newurl != None:
                            self.crawl(newurl, level + 1)

                    except TypeError:
                        print("Error for link: " + link.get('href'))
            else:
               if self.urls[url] > level:
                   self.urls[url] = level
        else:
            print(url + "unreachable")

    def generatefile(self):
        urlsbylevel = {}
        maxlevel = 0

        for key, value in self.urls.items():
            if value > maxlevel:
                maxlevel = value

            listurls = None

            if value not in urlsbylevel:
                listurls = []
            else:
                listurls = urlsbylevel[value]
            
            if listurls != None:
                listurls.append(key)
                urlsbylevel[value] = listurls
        step = 1 / (maxlevel * 2)

        rootstr = '<urlset></urlset>'
        root = ET.fromstring(rootstr)
        root.attrib = {'xmlns': 'httpt://www.sidemaps.org/schemas/sidemap/0.9'}

        for key, value in urlsbylevel.items():
            priority = round(1 - step * key, 2)

            if priority < 0:
                print("Step =" + str(step) + "Key=" + str(key))

            for item in value:
                url = ET.SubElement(root, "url")
                ET.SubElement(url, "loc").text = item
                ET.SubElement(url, "priority").text = str(priority)
            
        tree = ET.ElementTree(root)
        ET.indent(tree, ' ')
        tree.write(self.filename, encoding="uft-8", xml_declaration=True)


SitemapGenerator = SitemapGenerator("https://www.toutsurlebitcoin.fr", "sitemap.xml")
SitemapGenerator.crawl("https://www.toutsurlebitcoin.fr", 0)
SitemapGenerator.generatefile()