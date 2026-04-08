import configparser
import json
import os
import openpyxl

class GenericUtils:

    @staticmethod
    def get_config(config_type,key):
        config = configparser.ConfigParser()
        # Build the path to the main folder
        config_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configuration.ini')

        # Read the config
        config.read(config_file)
        value = config[config_type].get(key)
        return value


    @staticmethod
    def get_test_case_by_id(testCaseId):
        """
        Reads 'test_data.json' from the main folder,
        finds the test case with the given ID,
        and returns it as a dictionary.
        """
        # Build path relative to this script
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '/Users/elbyjoby/PycharmProjects/Pythontesting/test_data.json')

        # Open and load JSON
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Loop through all test cases and find the one with matching testCaseId

            for testCase in data.get("testCases", []):
                if testCase.get("testCaseId") == testCaseId:
                    return testCase  # Return the dictionary




# Read excel data


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
            }
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
                print(testcase.get("firstName"))
                return testcase

    @staticmethod
    def get_tcID(testName):
        testcaseID = testName.split("_")[1]
        return testcaseID
