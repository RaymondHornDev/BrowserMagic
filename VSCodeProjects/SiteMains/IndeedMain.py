from SiteMains.SiteTools.IndeedBrowserTools import IndeedBrowserTools

class IndeedMain(IndeedBrowserTools):
    def __init__(self, passedLogger):
        ''' Indeed Main constructor '''
        super().__init__(passedLogger)
        self.logger.info_call('IndeedMain object created')
        
    def __del__(self):
        self.logger.info_call('IndeedMain object deleted')
        
    def main(self):
        self.sign_in()
        
        self.job_search()
        
        job_clickables = self.get_job_clickable()
        
        self.sort_jobs(job_clickables, len(job_clickables) - 1)
           
        self.kill_driver()
