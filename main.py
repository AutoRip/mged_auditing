from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,random

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36')

with webdriver.Chrome("./chromedriver",options=options) as driver:
    driver.get("http://nmdms.ustb.edu.cn/")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//*[@id='userAccount']").send_keys("")
    driver.find_element_by_xpath("//*[@id='userPassword']").send_keys("")
    driver.find_element_by_xpath("//*[@id='userLogin']").click()
    driver.implicitly_wait(5)
    driver.switch_to.frame("mainFrame")
    driver.find_element_by_xpath("//*[@id='childDivId']/li[6]/a").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    count = 0
    for i in range(754):
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[3]/div/div/div/div/div/table/thead/tr/th[8]/i"))
        search_box = driver.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[3]/div/div/div/div/div/table/thead/tr/th[8]/i")
        search_box.click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/input").send_keys("倪剑樾")

        search_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/button[1]")
        search_button.click()

        # driver.execute_script("var q=document.documentElement.scrollTop=0")
        # WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[3]/div/div/div/div/div/table/thead/tr/th[1]/span/div/span[1]/div/labbel/span/input"))
        # time.sleep(3)
        check_box = driver.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[3]/div/div/div/div/div/table/thead/tr/th[1]/span/div/span[1]/div/label/span/input")
        check_box.click()
        # WebDriverWait(driver, timeout=10).until(lambda d: d.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[3]/div/div/div/div/div/table/thead/tr/th[1]/span/div/span[1]/div/label/span/input").click())
        submit = driver.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[2]/button[1]")
        submit.click()
        time.sleep(1)
        # WebDriverWait(driver, timeout=10).until(lambda d: d.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[2]/button[1]").click())
        # WebDriverWait(driver, timeout=10).until(lambda d: d.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/button[1]"))
        confirm = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/button[1]")
        confirm.click()
        # driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/button[1]")
        # driver.implicitly_wait(10)
        # WebDriverWait(driver, timeout=20).until(lambda d: d.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[3]/div/div/ul/li[9]/a"))
        # time.sleep(7)
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # next_page = driver.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[3]/div/div/ul/li[9]/a")
        # next_page.click()
        time.sleep(random.randint(5,9))
        driver.refresh()

        # driver.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[3]/div/div/div/div/div/table/thead/tr/th[1]/span/div/span[1]/div/label/span/input").click()
        # driver.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[2]/button[1]").click()
        # driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/button[1]").click()
        # next_page_button = driver.find_element_by_xpath("//*[@id='wrap']/section/main/section/main/div/div[3]/div/div/ul/li[9]")
        # # webdriver.ActionChains(driver).move_to_element(next_page_button).perform()
        # next_page_button.click()



