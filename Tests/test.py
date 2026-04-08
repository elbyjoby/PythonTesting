from os.path import split

import pytest

from Utils import jsonutility, generic_utils
from Utils.excelutility import Excel
from Utils.generic_utils import GenericUtils
from Utils.jsonutility import Json

def test_TC001(request):
    testName = request.node.name
    testcaseID=GenericUtils.get_tcID(testName)
    print("££££££££ ",testcaseID)
    jsondata = Json.get_test_case_by_id(testcaseID)
    exceldata = Excel.get_data(testcaseID)
    assert jsondata == exceldata

def test_TC002(request):
    testName = request.node.name
    testcaseID = testName.split("_")[1]
    jsondata = Json.get_test_case_by_id(testcaseID)
    exceldata = Excel.get_data(testcaseID)
    assert jsondata == exceldata

def test_TC003(request):
    testName = request.node.name
    testcaseID = testName.split("_")[1]
    jsondata = Json.get_test_case_by_id(testcaseID)
    exceldata = Excel.get_data(testcaseID)
    assert jsondata == exceldata