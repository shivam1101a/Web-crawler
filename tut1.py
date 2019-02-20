import requests
from bs4 import BeautifulSoup

#import beautifulsoup library

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

#function to remove duplicate elements from list

def ques_spider(max_pages):
    page=1
    count=0
    while page<= max_pages:
        url = 'https://www.geeksforgeeks.org/tag/amazon/page/'+str(page)  #it is done to add pages
        source_code=requests.get(url)
        plain_text=source_code.text #conversion
        soup=BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'rel':'bookmark'}):
            href=link.get('href')
            title=link.string   #title printing
            print(href)
            print(title)
        arr=[]  #inilizing list
        i=0
        for link in soup.findAll('a', {'rel': 'bookmark'}):
            href=link.get('href')
            arr.append(link)    #adding elements in list
            print(arr[i])
            i+=1
            count+=1    #for number of link traversed

        print(Remove(arr))      #removing duplicate elements
        page += 1
    print(count)


ques_spider(10)     #main
