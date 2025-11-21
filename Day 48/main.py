from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")



try:
    # search_bar = driver.find_element(By.NAME, value = "gLFyf")
    # print(search_bar.tag_name)

    menu = WebDriverWait(driver,1).until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='content']/div/section/div[2]/div[2]/div/ul")))

    items = menu.find_elements(By.TAG_NAME, "li")

    events = {}

    for i, li in enumerate(items, start=1):
        date = li.find_element(By.TAG_NAME, "time").get_attribute("datetime")
        name = li.find_element(By.TAG_NAME, "a").text
        link = li.find_element(By.TAG_NAME, "a").get_attribute("href")

        events[i]={
            "date":date,
            "name":name,
            "link":link
        }

    print(events)

except Exception as e:
    print("No Data Found!", e)

finally:
    driver.quit()