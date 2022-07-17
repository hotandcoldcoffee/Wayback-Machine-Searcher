import requests
import pandas
import re
from urllib import request
from Scripts.objnum import objnum
from bs4 import BeautifulSoup
import os

print("")
print("                                           | WayBack Machine Searcher |                                                   ")
print("")
print("                                            made by u/hotandcoldcoffee                                                  ")
print("")

while True:
   url = input("insert url: ")
   letter = input("insert word: ")
   if url and letter:
      check = "https://web.archive.org/cdx/search/cdx?url=" + url + "&filter=mimetype:text/html&matchType=prefix&output=json&filter=statuscode:200&fl=timestamp,original"
      print("Please Wait... this may take several minutes.")
      reading = pandas.read_json(check)
      if reading is not None:
         index = objnum(reading[0]) - 1
         print("found " + str(index) + " pages to look for.")
         for i in range(index):
            num = i + 1
            timestamp = reading[0][num]
            original = reading[1][num]
            link = "https://web.archive.org/web/" + timestamp + "/" + original
            response = requests.get(link)
            content = response.content
            soup = BeautifulSoup(content , 'html.parser')
            find = soup.find_all(string=re.compile(letter))
            if find:
               print(str(find) + " found in " + link + "(" + str(num) + "/" + str(index) + ")")
               download = open(timestamp + ".html" , "wb")
               download.write(content)
               print(link + " downloaded")
            else:
               print(link + " not found" + "(" + str(num) + "/" + str(index) + ")")




   


            
            
          