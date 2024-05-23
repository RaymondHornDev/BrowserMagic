# External imports

# STL imports
import threading

# Custom imports
from IndeedMain import IndeedMain
from LinkedInMain import LinkedInMain
from ZipRecruiterMain import ZipRecruiterMain
from LoggerCalls import LoggerCalls


thread_list = []
if __name__ == '__main__':
        
    lc = LoggerCalls()
    id = IndeedMain(lc)
    li = LinkedInMain(lc)
    zr = ZipRecruiterMain(lc)
    
    t1 = threading.Thread(target=id.main)
    t2 = threading.Thread(target=li.main)
    t3 = threading.Thread(target=zr.main)
    thread_list.append(t1)
    thread_list.append(t2)
    thread_list.append(t3)
    
    for item in thread_list:
        item.start()
    for item in thread_list:
        item.join()
        
    lc.info_call('Finished')
'''
    
lc = LoggerCalls()
id = IndeedMain(lc)
id.main()
'''