import time
from src.singleton.all_links_to_scrape import AllLinksToScrape
from src.operations.driver_setup import driver_setup
from src.operations.pause_until_loaded import pause_until_loaded
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver


class GetAllAddressLinksFromTab:

    def __init__(self, tab_link):
        self.tab_link = tab_link

    def get_all_address_links_from_tab(self):
        driver = driver_setup()
        a = ActionChains(driver)
        # driver.get(
        #     "https://www.domain.com.au/sitemap-listings-sale-2022111004.xml")
        driver.get(self.tab_link)

        # url_list = driver.find_elements(By.CSS_SELECTOR, "urlset > url")
        # print("URL LIST", url_list)
        # url_list_full = []
        # for u in url_list:
        #     url_list_full.append(u.text)

        # print("URL LIST FULL", url_list)
        print("time sleep.")
        time.sleep(500)
        (driver, a) = pause_until_loaded(driver, a)
        print("here", self.tab_link)

        self.try_and_get_dream_homes_and_home_designs_to_inspire_you_links(
            self, driver, a)


        time.sleep(5000)

    def try_and_get_dream_homes_and_home_designs_to_inspire_you_links(self, driver, a):
        base_xpath = "//div[@data-testid='dream-homes-item']"
        try:

            dream_homes_and_home_designs_to_inspire_you_links_list = []
            num_of_apartments_shown = len(driver.find_elements(
                By.XPATH, f"{base_xpath}"))
            for _ in range(num_of_apartments_shown):
                right_click_arrow = driver.find_element(
                    By.XPATH, f"{base_xpath}//button[@class='slick-arrow slick-next']")

            while driver.find_element(By.XPATH, f"{base_xpath}//button[@class='slick-arrow slick-next']"):
                print("arrow is visible!")
                a.move_to_element(right_click_arrow).click().perform()
                # for i in range(num_of_apartments_shown):

            all_links_to_scrape_instance = AllLinksToScrape.get_instance()
            # all_links_to_scrape_instance.add_to_links_list(self=all_links_to_scrape_instance, link)
            
        except NoSuchElementException:
            return

            # each page may have: "Dream Homes" and "The Block" and "Newly Released" and "New Developments"
            # "Dream Homes" and "Home designs to inspire you" xpath: "//div[@data-testid='dream-homes-item']"
            # "The Block" xpath: "//div[@data-testid='the-block-listing-item']"
            # "Newly Released" xpath: "//div[@data-testid='dream-homes-item']"
            # "New Developments" xpath: "//div[@data-testid='featured-projects-card']"
            # all would attach to the front of: "//a[@href]"
            # to get right arrow, append this to the back: "//button[@class='slick-arrow slick-next']"


"""
for Dream Homes: //div[@class='css-fz49w8']
for The Block 2022 Properties: //div[@class='css-1t7a3eq']

Dream Homes right arrow: //div[@data-testid='domain-dream-homes']//button[@class='slick-arrow slick-next']
The Block 2022 Properties right arrow: //div[@data-testid='domain-the-block-wrapper']//button[@class='slick-arrow slick-next']
//div[starts-with(@class, “css-”)]

"""
