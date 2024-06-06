#Extrenal imports
from selenium.webdriver.common.by import By

#STL imports
import time

#Custom imports
from SiteTools import LinkedInBrowserTools
from StringTools import StringTools


class LinkedInMain(LinkedInBrowserTools):
    def __init__(self, passedLogger):
        super().__init__(passedLogger)
        self.logger.info_call('LinkedInMain object created')
        self.site_urls = StringTools.site_urls
        self.li_search_strings = StringTools.li_search_strings
        
    def __del__(self):
        self.logger.info_call('LinkedInMain object deleted')
        


    def main(self):
        
        self.login_signin()
        
        time.sleep(5)
        
        input('Type anything')

        job_list = self.search_for_job()
        
        self.button_clicker(By.CSS_SELECTOR, '.msg-overlay-bubble-header__details')

        self.store_job_urls(job_list)

        self.sort_jobs_urls()

        self.kill_driver()
        
    def login_signin(self):
        self.driver.get(self.site_urls['linked_in'])

        # Locates username text area and enters username
        self.text_inputter(By.ID, self.li_search_strings['li_user_name_string'], 'xyz@gmail.com')

        # Locates password text area and enters password
        self.text_inputter(By.ID, self.li_search_strings['li_find_password_string'], 'nope')

        # Locates and clicks button to sign in
        self.button_clicker(By.CSS_SELECTOR, self.li_search_strings['li_sign_in_button_string'])
        
    def search_for_job(self):
        job_entry = 'Python Developer'
        
        # Locates job search text area, enters job search string, and enters RETURN
        self.text_inputter(By.CSS_SELECTOR, self.li_search_strings['li_find_job_type_string'],job_entry, True)

        job_list_container = self.wait_and_search(By.CSS_SELECTOR, self.li_search_strings['li_find_job_list_continer_string'], False)

        job_list = self.wait_and_search(By.CSS_SELECTOR, self.li_search_strings['li_find_job_links'], False)

        return job_list
