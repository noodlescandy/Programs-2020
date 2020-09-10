from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import urllib.request, json, time
#from selenium.webdriver import ActionChains

query = input("Enter name of playlist/music you want: ")
query.replace(" ", "+")

options = Options()
options.headless = True
#options.headless = False
driver = webdriver.Firefox(options=options)

#actionChains = ActionChains(driver)
driver.get('https://youtube.com/results?search_query=' + query + '&sp=EgIQAw%253D%253D)')
#print(driver.current_url)

viewFullButton = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-renderer[1]/div/yt-formatted-string[2]/a')
viewFullButton.click()
#print("clicked on first\n")

url = driver.current_url
playlistDefinition = "list="
if not playlistDefinition in url:
    viewFullButton = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-renderer[2]/div/yt-formatted-string[2]/a')
    viewFullButton.click()
    url = driver.current_url

driver.close()

oldurl = url
with urllib.request.urlopen("https://www.youtube.com/oembed?url=" + url + "&format=json") as url:
    data = json.loads(url.read().decode("utf-8"))
    #print(data)
title = data['title']
author_name = data['author_name']
print("\nRetrieved Playlist:")
print(title)
print(author_name)
#print(vidCount)
print(oldurl)

"""
TODO
- ADD MULTIPLE CHOICES FOR WHICH PLAYLIST TO USE
- ADD AUTOMATIC DOWNLOAD OF PLAYLIST AFTER CHOICES
x SHOW NAME OF PLAYLIST AND author_name
- SHOW HOW MANY VIDEOS ARE IN IT
x AUTODETECT AND REMOVE ADS FROM RESULT
"""
