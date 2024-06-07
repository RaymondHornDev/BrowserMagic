# External imports

# STL imports
import threading

# Custom imports
from SiteMains import IndeedMain, LinkedInMain, ZipRecruiterMain
from Logger import LoggerCalls


# List container for driver threads
thread_list = []
if __name__ == '__main__':

    # Instanciates a LoggerCalls object    
    lc = LoggerCalls()

    # Instanciates an IndeedMain object
    id = IndeedMain(lc)

    # Instanciates a LinkedInMain object
    li = LinkedInMain(lc)

    # Instanciates a ZipRecruiterMain object
    zr = ZipRecruiterMain(lc)

    # Thread targets IndeedMain
    t1 = threading.Thread(target=id.main)

    # Thread targets LinkedInMain
    t2 = threading.Thread(target=li.main)

    # Thread targets ZipRecruiterMain
    t3 = threading.Thread(target=zr.main)

    # Adds the threads to the thread_list
    thread_list.append(t1)
    thread_list.append(t2)
    thread_list.append(t3)

    # Cycles through thread_list and starts each thread
    for item in thread_list:
        item.start()

    # Cycles through thread_list and joins each thread
    for item in thread_list:
        item.join()
        
    lc.info_call('Finished')
'''
    
lc = LoggerCalls()
id = IndeedMain(lc)
id.main()
'''
