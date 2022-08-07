#for the use you must change the url and you must change your user and password and change thev labels of the page 

from requests_html import HTMLSession
from time import sleep
from selenium import webdriver


def coolmod():
    url_coolmod = "https://www.coolmod.com/msi-gf63-thin-10scsr-876xes-i7-10750h-gtx-1650-ti-max-q-16gb-1tb-nvme-pcie-freedos-156-portatil/"
    session = HTMLSession()
    product_page = session.get(url_coolmod)
    found = product_page.html.find("#main-buy")
    if len(found) > 0:
        driver = webdriver.Firefox()
        driver.get(url_coolmod)
        
        driver.find_element_by_class_name("confirm").click()
        driver.find_element_by_class_name("fas fa-clipboard-check").click()
        driver.find_element_by_class_name("button-buy").click()
        sleep(1)
        driver.find_element_by_class_name("confirm").click()
        driver.find_element_by_class_name("button-buy").click()
        is_form_loaded = None
        form = None
        while not is_form_loaded:
            try:
                form =   driver.find_element_by_class_name("login100-form").click()
            except NoSuchElementException:
                print("dont the form")
        
        
        email = form.find_element_by_name("jform[email]")
        password = form.find_element_by_name("jform[password]")

        email.send_keys("user@user.com")
        password.send_keys("password")
    else:
        print("dont stock")
def main():
    coolmod()


if __name__=="__main__":
    main()