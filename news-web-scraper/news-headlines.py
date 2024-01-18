from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os 
import sys

app_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y") #convert datetime to string format MMDDYYYY

website = "https://www.wired.com/"
path = "C:\Chrome Driver\chromedriver-win64\chromedriver.exe"

#headless-mode
options = Options()
options.add_argument('--headless=new')

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
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

file_name = f'headline-{month_day_year}.csv'
final_path = os.path.join(app_path,file_name)
df_headlines.to_csv(final_path)

driver.quit()
