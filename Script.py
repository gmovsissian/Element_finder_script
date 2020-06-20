import validators
from selenium import webdriver

def get_element_count(url):
    driver = webdriver.Chrome("WebDriver\chromedriver.exe")
    driver.get(url)
    form_list = driver.find_elements_by_xpath("//form[@method='get']")
    print("Number of Form elements with method='get' is: " + str(len(form_list)))
    image_list = driver.find_elements_by_xpath("//img")
    print("Number of elements with Image tag is: " + str(len(image_list)))
    driver.quit()

if __name__ == "__main__":
    print("Input Your URL (e.g. http://www.auto.am)")
    input_URL = str(input())

    while not validators.url(input_URL):
        print("Input Correct URL")
        input_URL = str(input())
    get_element_count(input_URL)