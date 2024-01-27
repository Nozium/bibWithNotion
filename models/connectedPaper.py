from dataclasses import dataclass

@dataclass
class ConnectedPaper ():
    title:str
    yaer:int
    url:str
    abstract:str
    author:str
    doi:str
    pmid:int=None
    notion_page_id:int = None
    parents_id:int = None
    def get_bib_scheme():
        return {

        }