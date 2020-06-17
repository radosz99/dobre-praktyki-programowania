import testlink
import unittest
from testlink.testlinkerrors import TLResponseError
from anagram import find_anagrams
from trie import make_trie
from unittest import (TestCase, TestLoader, TextTestResult, TextTestRunner)
import os
 
 
class TestSimple(unittest.TestCase):
    def test_anagram(self):
        tri = make_trie("ENG")
        anagrams = find_anagrams("abc", tri)
        self.assertTrue(12==len(anagrams))
 
 
OK ='ok'
FAIL ='fail'
ERROR ='error'
SKIP ='skip'
 
 
class JsonTestResult(TextTestResult):
    def __init__(self,stream,descriptions,verbosity):
        super_class =super(JsonTestResult,self)
        super_class.__init__(stream,descriptions,verbosity)
        self.successes =[]
 
 
    def addSuccess(self,test):
        super(JsonTestResult,self).addSuccess(test)
        self.successes.append(test)
 
 
    def json_append(self,test,result,out):
        suite =test.__class__.__name__
        if suite not in out:
            out[suite]={OK:[],FAIL:[],ERROR:[],SKIP:[]}
        if result is OK:
            out[suite][OK].append(test._testMethodName)
        elif result is FAIL:
            out[suite][FAIL].append(test._testMethodName)
        elif result is ERROR:
            out[suite][ERROR].append(test._testMethodName)
        elif result is SKIP:
            out[suite][SKIP].append(test._testMethodName)
        return out
       
       
    def jsonify(self):
        json_out =dict()
        for t in self.successes:
            json_out =self.json_append(t,OK,json_out)
        for t,_ in self.failures:
            json_out =self.json_append(t,FAIL,json_out)
        for t,_ in self.errors:
            json_out =self.json_append(t,ERROR,json_out)
        for t,_ in self.skipped:json_out =self.json_append(t,SKIP,json_out)
        return json_out
 
 
if __name__ == '__main__':
    URL = 'http://192.168.1.110/lib/api/xmlrpc/v1/xmlrpc.php'
    DevKey = '2b9357e4ae95e8cd3ca14a2d2819822b'
    testcase_id = 53
    testplan_id = 2
 
    tl_helper = testlink.TestLinkHelper()
    myTestLink = tl_helper.connect(testlink.TestlinkAPIClient)
    myTestLink.__init__(URL, DevKey)
 
    with open(os.devnull,'w') as null_stream:
        runner = TextTestRunner(stream=null_stream)
        runner.resultclass =JsonTestResult
        suite = TestLoader().loadTestsFromTestCase(TestSimple)
        result = runner.run(suite)
        res = result.jsonify()['TestSimple']
 
    if(len(res['ok'])!=0):
        try:
            myTestLink.reportTCResult(testcaseid=testcase_id, testplanid=testplan_id, buildname='Build_v1.0', notes='Succeeded', status='p',user='radek1',steps=[
                {'step_number':1,'result':'p','notes':'Opened'},
                {'step_number':2,'result':'p','notes':'Made'},
                {'step_number':3,'result':'p','notes':'Invoked'},
                {'step_number':4,'result':'p','notes':'Passed!'}
                ])
        except TLResponseError:
            print(f'Nie ma takiego case')
    elif(len(res['fail'])!=0):
        try:
            myTestLink.reportTCResult(testcaseid=testcase_id, testplanid=testplan_id, buildname='Build_v1.0', notes='Failed', status='f',user='radek1',steps=[
                {'step_number':1,'result':'p','notes':'Opened'},
                {'step_number':2,'result':'p','notes':'Made'},
                {'step_number':3,'result':'p','notes':'Invoked'},
                {'step_number':4,'result':'f','notes':'Failed:('}
                ])
        except TLResponseError:
            print(f'Nie ma takiego case')