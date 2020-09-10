from selenium import webdriver
import time
#from selenium.webdriver import ActionChains

query = input("Enter name of playlist/music you want: ")
query.replace(" ", "+")
driver = webdriver.Firefox()
#actionChains = ActionChains(driver)
driver.get('https://youtube.com/results?search_query=' + query + '&sp=EgIQAw%253D%253D)')
print(driver.current_url)

"""
# OLD WAY THAT DOESN'T ALWAYS WORK
searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
# use xpath plugin for full xpath on firefox
searchbox.send_keys(query)
print("sent query")

searchbutton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
searchbutton.click()
print("clicked search")

filterButton = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/paper-button')
filterButton.click()
print("clicked filter")
#good up to here

#playlistButton = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[2]/ytd-search-filter-renderer[3]')
playlistButton = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[2]/ytd-search-filter-renderer[3]')
playlistButton.click()
print("clicked playlist")

time.sleep(1)
print("nice rest")
"""

viewFullButton = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-renderer[1]/div/a/h3/span')
viewFullButton.click()
print("clicked on first\n")

url = driver.current_url
playlistDefinition = "&list="
if playlistDefinition in url:
    print(url)
else:
    viewFullButton = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-renderer[2]/div/a/h3/span')
    viewFullButton.click()
    print(driver.current_url)
driver.close()

"""
TODO
- ADD MULTIPLE CHOICES FOR WHICH PLAYLIST TO USE
- ADD AUTOMATIC DOWNLOAD OF PLAYLIST AFTER CHOICES
- SHOW NAME OF PLAYLIST AND HOW MANY VIDEOS ARE IN IT
x AUTODETECT AND REMOVE ADS FROM RESULT
"""
