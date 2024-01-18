from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.wired.com/"
path = "C:\Chrome Driver\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

# while(True):
#     pass


containers = driver.find_elements(by="xpath", value='//div[@class="SummaryItemContent-eiDYMl clSLtF summary-item__content summary-item__content--vertically-align summary-item__content--bottom-dek"]')
titles= []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/h3').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    links.append(link)

my_dict = {'title': titles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv')

driver.quit()
