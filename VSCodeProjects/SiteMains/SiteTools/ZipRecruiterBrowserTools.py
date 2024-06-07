#Extrenal imports
from selenium.webdriver.common.by import By

# STL import
import time

# Custom imports
from StringTools import StringTools
from SiteMains.SiteTools.DriverControlTools.PageTools import PageTools
from ABTools.AbstractTool import AbstractSortingTools

class ZipRecruiterBrowserTools(PageTools, AbstractSortingTools):
    '''A class that inherits from the Page Tools'''
    def __init__(self, passedLogger):
        super().__init__(passedLogger)
        self.logger.info_call('ZipRecruiter object created')
        self.zr_search_strings = StringTools.zr_search_strings
        
    def __del__(self):
        self.logger.info_call('ZipRecruiter object destroyed')            
                                     
    def open_main_page(self):
        url_string = StringTools.site_urls['zip_recruiter']
        self.driver.get(url_string)
        
    def job_links(self):
        time.sleep(.5)
        job_links = self.test_for_element(By.TAG_NAME, "h2")
        if len(job_links) > 0:
            self.store_job_links(job_links)
                   
    def store_job_links(self, passed_list):
        for item in passed_list:
            if item.get_attribute('class') == 'font-bold text-black text-header-sm':
                anchor = item.find_element(By.TAG_NAME, 'a')
                
                if anchor:
                    self.job_urls.append(anchor)
                        
    def sort_jobs_urls(self):
        time.sleep(.2)
        
        for item in self.job_urls:
            time.sleep(.25)
            item.click()
            time.sleep(.25)
            self.apply_button()
            
    def apply_button(self):
        '''Collects all the buttons on the page and '''
        current_tab = self.driver.current_window_handle
        partial_text = 'Apply'
        button = self.test_for_element(By.XPATH, f"//*[contains(text(), '{partial_text}')]")
        button[1].click()
        time.sleep(.1)
        single_tab = self.tab_test(current_tab)
        if single_tab == True:
            self.apply_menu_root()
                
    def apply_menu_root(self):
        '''Searches modal for exit buttons'''
        exit_button = self.wait_and_search(By.XPATH, '//button[@title="Close"]', False)
        if len(exit_button) > 0:
            self.look_for_exit_button(exit_button)
        else:
            self.logger.debug_call('Exit button not found')
            
    def look_for_exit_button(self, passed_list):
        '''Sorts the list of exit buttons and extracts the correct on. Clicks it and the
        following exit button. WebdriverWait is used to allow the modal elements to load
        before attempting to locate them'''
        self.logger.debug_call(len(passed_list), 'items in passed exit button list')
        passed_list[2].click()
        cancel_button = self.wait_and_search(By.XPATH, '//p[contains(., "Cancel Application")]/parent::*')
        if cancel_button:
            cancel_button.click() 