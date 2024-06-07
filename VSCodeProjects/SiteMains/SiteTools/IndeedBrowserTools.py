# External imports
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# STL imports
import time

# Custom imports
from SiteMains.SiteTools.DriverControlTools.PageTools import PageTools
from StringTools import StringTools

class IndeedBrowserTools(PageTools):
    def __init__(self, passedLogger):
        super().__init__(passedLogger)
        self.logger.info_call('IndeedBrowserTools object created')
        self.site_url = StringTools.site_urls['indeed']
        self.stored_jobs = []
        
    def __del__(self):
        self.logger.info_call('IndeedBrowserTools object deleted')
        
    def sign_in(self):
        self.driver.get(self.site_url)
        time.sleep(.25)
        
        self.text_inputter(By.XPATH, '//input[@type="email"]', 'xyz@gmail.com', True)
            
        self.button_clicker(By.LINK_TEXT, 'Sign in with login code instead')
        
        input()
        
        self.text_inputter(By.XPATH, '//input[@name="cityState"]', 'Carbondale, PA')
        
        self.text_inputter(By.XPATH, '//input[@name="postalCode"]', '18407', True)
        
        time.sleep(.35)
         
    def job_search(self):
        money_input = self.wait_and_search(By.XPATH, '//input[@id="payinput-onboarding-minimumpay-minimumPay-minimumPay"]')
        if money_input:
            self.logger.debug_call('Cash input found')
            money_input.send_keys(Keys.CLEAR)
            time.sleep(.35)
            if money_input.get_attribute('value') == '':
                money_input.send_keys('30,000')
            
            self.button_clicker(By.XPATH, '//button[@aria-label="Continue"]')
            time.sleep(.35)
            job_input = self.wait_and_search(By.XPATH, '//input[@name="desiredJob-0"]')
            time.sleep(.35)
            job_input.send_keys(Keys.RETURN)
            self.logger.debug_call('Return pressed')
            time.sleep(3)
            
    def get_job_clickable(self):
        self.logger.info_call('Get clickables called')
        return self.wait_and_search(By.XPATH, "//span[starts-with(@id, 'jobTitle')]/parent::*", False)
            
    def sort_jobs(self, job_boxes, num):
        self.logger.info_call('Sort jobs called')
        #num = len(job_boxes)
        self.recursive_search(job_boxes, num)
        
    def recursive_search(self, job_boxes, num):
        self.logger.info_call('Recursive search called')
        if len(job_boxes) > 0:
            self.logger.info_call('Job boxes lenght test passed')
            job_saved = job_boxes[-1] in self.stored_jobs
            if job_saved:
                self.logger.info_call(len(self.stored_jobs))
                
            else:
                self.logger.debug_call('Anchors found')
                actions = ActionChains(self.driver)
                if num < len(job_boxes) - 1:
                    search_num = num + 1
                else:
                    search_num = num
                self.driver.execute_script("window.scrollTo(0, arguments[0]);", job_boxes[search_num].location['y'])
                actions.move_to_element(job_boxes[num]).perform()
                time.sleep(.5)
                            
                if 'full details of' in job_boxes[num].get_attribute('aria-label'):
                    print(job_boxes[num].text, '\n')
                    job_boxes[num].click()
                    time.sleep(1)
                    self.stored_jobs.append(job_boxes.pop(num))
                    
                if num > 0:
                    self.sort_jobs(job_boxes, num-1)
                    
                else:
                    self.sort_jobs(self.get_job_clickable(), len(self.get_job_clickable()))   
                
    '''        
    def sort_jobs(self):
        more_jobs = True
        while more_jobs:
            job_boxes = self.wait_and_search(By.XPATH, "//span[starts-with(@id, 'jobTitle')]/parent::*", False)
            if job_boxes[-1] in self.stored_jobs:
                more_jobs = False
            else:
                if len(job_boxes) > 0:
                    self.logger.debug_call('Anchors found')
                    self.cycle_through_job_list(job_boxes)
                    time.sleep(.5)
                else:
                    self.logger.debug_call('Spans not found')
                    more_jobs = False
                
    def cycle_through_job_list(self, job_boxes):
        iter = 0
        for item in job_boxes:
            if item not in self.stored_jobs:
                actions = ActionChains(self.driver)
                self.driver.execute_script("window.scrollTo(0, arguments[0]);", item.location['y'])
                actions.move_to_element(item).perform()
                time.sleep(.5)
                            
                if 'full details of' in item.get_attribute('aria-label'):
                    print(item.text, '\n')
                    item.click()
                    time.sleep(1)
                    self.stored_jobs.append(item)
                    
            iter += 1
    ''' 
