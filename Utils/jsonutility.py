import json
import os

class Json:

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

