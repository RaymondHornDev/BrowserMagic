#Extrenal imports
from selenium.webdriver.common.by import By

#STL imports
import time

#Custom imports
from AbstractTool import AbstractSortingTools
from PageTools import PageTools

#LinkedIn specific browser tools
class LinkedInBrowserTools(PageTools, AbstractSortingTools):
    
    def __init__(self, passedLogger):
        super().__init__(passedLogger)
        self.logger.info_call('LinkedIn Browser Tools object created')
        
    def __del__(self):
        self.logger.info_call('LinkedIn Browser Tools object deleted')
    
    def store_job_urls(self, passedList):
        local_iter = 0
        for item in passedList:
            if local_iter >= 4:
                job_link = item.get_attribute('href')
                
                if 'Python' in str(job_link) or 'Developer' in str(job_link):
                    self.job_urls.append(job_link)
                    
            local_iter += 1
            
    def sort_jobs_urls(self):
        try:
            self.driver.refresh()
            time.sleep(.2)
            for url in self.job_urls:
                self.logger.info_call(url)
                self.driver.get(url)
                time.sleep(2)   # Let the page load
                
                is_there = self.test_for_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card')
                    
                if len(is_there) > 0:
                    self.logger.debug_call('Button found')
                    self.pull_company_name()
                    self.apply_menu_root()
                    
                else:
                    self.logger.debug_call('Buttton not found')
                
        except ValueError as ve:
            errorReport = f'Error in cycle through jobs: {ve}'
            self.logger.error_call(errorReport)
            
    def pull_company_name(self):
        name_div = self.test_for_element(By.CSS_SELECTOR, '.app-aware-link')
        if len(name_div) > 0:
            self.logger.info_call('Company Name Found')
            self.pull_company_name_text()
        else:
            self.logger.info_call('Company name anchor not found')
            
    def pull_company_name_text(self):
        page_source = self.driver.page_source
        soup = self.soup_parser(page_source, "html.parser")
            
        wrapper_div = self.soup_search(soup, 'div', 'job-details-jobs-unified-top-card__primary-description-without-tagline')
        if wrapper_div:
            company_name = self.soup_search(wrapper_div, 'a', 'app-aware-link')
            if company_name:
                self.logger.info_call(company_name.text)
                    
            else:
                self.logger.debug_call('Text not found')
                
        else:
            self.logger.debug_call('Compnay name wrapper div not found')
            
        self.find_job_detail(soup)
            
    def find_job_detail(self, passed_source):
        '''Searches for job details div'''
        detail_span =  self.soup_search(passed_source, 'div', 'jobs-box__html-content jobs-description-content__text t-14 t-normal jobs-description-content__text--stretch')
        if detail_span:
            self.find_job_detail_text(detail_span)
        else:
            self.logger.debug_call('Detail span not found')
        
    def find_job_detail_text(self, passed_element):
        '''Prints text on job details'''
        self.logger.info_call(passed_element.text)
            
    def apply_menu_root(self):
        try:
            time.sleep(2)
            # Stores a handle to the current tab
            this_window = self.driver.current_window_handle
            
            # Locates the apply button and clicks it
            button = self.test_for_element(By.CSS_SELECTOR, "div.jobs-apply-button--top-card")
            self.logger.debug_call(type(button))
            if  len(button) > 0:
                time.sleep(.2)
                button[0].click()
                time.sleep(.2)
                
                exit_tree =  self.tab_test(this_window)
                if exit_tree:
                    self.menu_exit()
                   
        except ValueError as ve:
            errorReport = f'Unclickableness: {ve}'
            self.logger.error_call(errorReport)
            
    def menu_exit(self):
        try:
            time.sleep(.2)
            exit_butt = self.test_for_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]')
            if len(exit_butt) > 0:
                time.sleep(.2)
                exit_butt[0].click()
                
                drop_button = self.test_for_element(By.CSS_SELECTOR, 'button[data-control-name="discard_application_confirm_btn"]')
                if len(drop_button) > 0:
                    time.sleep(.2)
                    drop_button[0].click()
                    time.sleep(.2)
            
        except ValueError as ve:
            errorReport = f'Error in menu exit: {ve}'
            self.logger.error_call(errorReport)