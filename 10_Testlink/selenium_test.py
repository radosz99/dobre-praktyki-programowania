from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import testlink
from testlink.testlinkerrors import TLResponseError

status = {'1':'f', '2':'f', '3':'f'} 
URL = 'http://192.168.1.110/lib/api/xmlrpc/v1/xmlrpc.php'
DevKey = '2b9357e4ae95e8cd3ca14a2d2819822b'
testcase_id = 61
testplan_id = 2

tl = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
tl.__init__(URL, DevKey)

try:
    driver = webdriver.Firefox(executable_path=r'E:/Unknown/geckodriver.exe')
    driver.get("http://localhost:5000/game/view")
    status['1'] = 'p'
    mr = driver.find_element_by_id("add_user_btn")
    mr.click()
    status['2'] = 'p'
    tx = driver.find_element_by_name("move")
    tx.send_keys('4:5:i;4:6:s')
    tx.submit()
    status['3'] = 'p'
    try:
        tl.reportTCResult(testcaseid=testcase_id, testplanid=testplan_id, buildname='Build_v1.0', notes='Succeeded', status='p',user='radek1',steps=[
            {'step_number':1,'result':status['1'],'notes':'Go to website'},
            {'step_number':2,'result':status['2'],'notes':'User add'},
            {'step_number':3,'result':status['3'],'notes':'Make move'},
        ])
    except TLResponseError:
        print(f'Nie ma takiego case')
except NoSuchElementException:
    print("Element nieznaleziony")
    try:
        tl.reportTCResult(testcaseid=testcase_id, testplanid=testplan_id, buildname='Build_v1.0', notes='Failed', status='f',user='radek1',steps=[
            {'step_number':1,'result':status['1'],'notes':'Go to website'},
            {'step_number':2,'result':status['2'],'notes':'User add'},
            {'step_number':3,'result':status['3'],'notes':'Make move'},
        ])
    except TLResponseError:
        print(f'Nie ma takiego case')

