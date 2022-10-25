import json
import requests
class NotionCommunicator():
    database_id:str
    api_key:str
    database_root: str = "https://api.notion.com/v1/databases/"
    child_page:str = "https://api.notion.com/v1/pages/"
    notion_version: str = "2022-06-28"  
    header:dict = {}
    def __init__(self,database_id:str,api_key:str):
        self.database_id = database_id
        self.api_key = api_key
        self.header = self._get_header()

    def _get_header(self) -> dict:
        # https://developers.notion.com/reference/changes-by-version
        # TODO : need to change dynamic
        return {
            "Authorization":self.api_key,
            "Notion-Version":self.notion_version,
            "Content-Type": "application/json"
            }

    def get_connection(self):
        return


    def get_database(self)->None:
        database_api = f"{self.database_root}/{self.database_id}"
        response_database = requests.get(database_api,headers = self.header)
        if response_database.status_code == 200:
            db = response_database.json()
        else:
            db = None
        self.databese = db

    def get_database_keys(self):
        if self.database is None:
            self.get_database()
        return self.databse["property"].keys()

    @staticmethod
    def convert_dict_bib_to_properties(dict_bib:dict):
        properties= {}
        for k,v in dict_bib.items():
            if k =="title":
                properties.update({k:{"title": [{"text":{"content": str(v)}}]}})
            elif k == "year":
                properties.update({k:{"type": "number","number":int(v)}})
            else:
                properties.update({k:{
                    'type': 'rich_text', 
                    'rich_text': [str(v)]
                }})     
        return properties

    def post_dict_bib_as_page(self,dict_bib)->None:
        properties = self.convert_dict_bib_to_properties(dict_bib)
        post_data = {
            "parent": {
                "database_id": self.database_id
            },
            "properties": properties
        }
        insert_response = requests.post(
                                self.child_page, 
                                headers=self.header,
                                data=json.dumps(post_data))
        if insert_response.status_code == 200:
            _ = insert_response.json()
            # TODO : log insert
            print("Insert bib file to database.")
        else:
            # TODO : log error of insert new page
            print("Fail to insert page", insert_response.status_code)
