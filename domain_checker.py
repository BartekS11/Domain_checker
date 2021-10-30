from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from domain_scraping import Get_json, Remember_old_values, sample_values
import sys
from selenium.common.exceptions import NoSuchElementException

domain_url = "https://pl.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck="
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)


def Create_domain_check_url(domain_name):
    domain_name = domain_name.replace(" ", "")
    return "{}{}".format(domain_url, domain_name)


def Setup_selenium():
    valid_url = Create_domain_check_url(name)
    driver.get(valid_url)


def Roll_name():
    name = Get_json()
    return name


def Is_domain_avaliable(domain_name):
    Setup_selenium()
    try:
        avaliable_text = driver.find_element_by_xpath(
            '//*[@id="exact-match"]/div/div/div/div[1]/div[1]/h4'
        ).text
        print(f"Domain {name}.com is not avaliable")
    except NoSuchElementException:
        print(f"Domain {name}.com is  avaliable")
    driver.close()


while True:
    print(50 * "-")
    name = Roll_name()
    print("Your random domain name is: {}".format(name))
    print(
        " 1.Pick that domain name\n 2.Roll domain name again\n 3.Check that domain name is free\n 4.Exit"
    )
    menu = int(input("Pick your choice "))
    print(50 * "-")

    if menu == 1:
        print(name)
    if menu == 2:
        print("Let's roll again")
    if menu == 3:
        Is_domain_avaliable(name)
    if menu == 4:
        sys.exit()
