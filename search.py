import yaml
from gocheck import tempfile.yaml
from gocheck.list_parser import ListParser


class Search:
"""
Searches for the words in a file against the list stored in database
"""
    def __init__(self, fileName):
        self.fileName = fileName

    def search(self):
        """
        Main Search function
        """
        search_data = ListParser(self.filename)
        with open(tempfile.yaml, 'r') as DBFile:
            db_list = yaml.load_all(DBFile)
        result = search_algo(search_data, db_list)
        return result

    def search_alg(self, search_data, db_list):
        """
        Algorithm employed for search function
        INPUT search_data = input search 
        OUTPUT - List of words found in the code
        """
        result = []
        for word in db_list:
            for key, value in word.items():
                if value in db_list:
                    result.append(dict(key,value))
        

        

    
        