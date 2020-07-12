import unittest
import getpass
from pprint import pprint
from libwebcq.CQ import CQ
from libwebcq.error import SessionError
from libwebcq.record import CustomerRecord, ModuleRecord, OwnerInfo, RecordType
cq = CQ('http://avclearquest.qlogic.org/cqweb/')
# Open a session befoer any network query.
cq.open_session()
try:
    # Need login before query protected resources.
    user = input('Enter your name: ')
    password = getpass.getpass(prompt="Enter CQ Password for " + user +": ")  
    print(password)
    print("Login into Clearquest...");
    res = cq.login(user, password, 'CQNew')
    res_id1 = cq.find_record('Cont00080744')
    record1 = cq.get_cq_record_details(res_id1, RecordType.CRP)
    #record1 = cq.get_cq_record_details(res_id1, RecordType.CUSTOMER)
    #record1 = cq.get_cq_record_details(res_id1, RecordType.USER)
    #record1 = cq.get_cq_record_details(res_id1, RecordType.MODULE)
    # Don't forget logout. 
    pprint(vars(record1))  
    #print(record1.state)
    cq.logout()
finally:
    # Close session when all work done.
    cq.close_session()

