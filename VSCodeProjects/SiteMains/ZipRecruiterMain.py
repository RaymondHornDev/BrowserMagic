# External imports
from selenium.webdriver.common.by import By

# Custom imports
from SiteTools.ZipRecruiterBrowserTools import ZipRecruiterBrowserTools

class ZipRecruiterMain(ZipRecruiterBrowserTools):
    def __init__(self, passedLogger):
        super().__init__(passedLogger)
        self.logger.info_call('ZipRecruiterMain object created')
        
    def __del__(self):
        self.logger.info_call('ZipRecruiterMain object deleted')
        
    def main(self):
        # Navigate to website
        self.open_main_page()
        
        # Login to website
        self.login()
        
        # Pause for security questions
        input('Enter RETURN')
        
        # Job Search and process loop
        self.job_search()
        
        self.kill_driver()
        
    def login(self):
        # Once for use name
        self.text_inputter(By.ID, self.zr_search_strings['login_input'], 'xyz@gmail.com')
        
        # Once for password
        self.text_inputter(By.ID, self.zr_search_strings['password_input'], 'yup')
        
        self.button_clicker(By.ID, self.zr_search_strings['submit_button'])
        
    def job_search(self):
        # Find job search input and button
        self.text_inputter(By.ID, 'downshift-0-input', 'Python Developer')
        self.button_clicker(By.ID, 'zds-1')
        
        # Job search
        self.job_links()
        
        # Cycle through job links and preform page tasks
        self.sort_jobs_urls()
