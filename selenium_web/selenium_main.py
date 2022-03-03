# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://public.tableau.com/views/FAAAnimalAirstrikeDashboard/StrikeDashboard?:language=en-GB&:display_count=n&:origin=viz_share_link")

print(driver)

driver.implicitly_wait(10.0)

driver.quit()