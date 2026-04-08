import os

import openpyxl

from Utils.generic_utils import GenericUtils


class Excel:

    @staticmethod
    def get_test_cases(file_name, sheet_name):
        # Build file path relative to this script
        file_path = os.path.join(os.path.dirname(__file__), file_name)

        # Load workbook and sheet
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]

        test_cases = []

        # Loop through rows (skip header row 1)
        for row in sheet.iter_rows(min_row=2, values_only=True):

            test_case = {
                "testCaseId": row[0],
                "username": row[1],
                "password": row[2],
                "firstName": row[3],
                "lastName": row[4],
                "age": row[5],

            }
            test_cases.append(test_case)

        return test_cases


    @staticmethod
    def get_data(testID):
        testData = GenericUtils.get_test_cases('/Users/elbyjoby/PycharmProjects/Pythontesting/excel_data.xlsx',
                                               'Sheet1')
        for testcase in testData:
            if testcase.get("testCaseId") == testID:
                return testcase

