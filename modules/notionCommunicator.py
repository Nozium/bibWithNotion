class NotionCommunicator():
    database_id:str
    api_key:str
    database_root: str = "https://api.notion.com/v1/databases/"
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
            "Notion-Version":self.notion_version
            }

    def get_connection(self):
        return


    def get_database(self):
        return

    def get_database_keys(self):
        if self.database is None:
            self.get_database()
        return self.databse["property"].keys()
