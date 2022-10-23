# bibWithNotion
## What for
- To manage Bib info with tag / status , parse .bib file and post to your Notion database.

## Feature Comming
- Export bib list with tag filtering.

## Setup To Use
### Setup Notion
1. create notion app account
2. get notion api key : see [here](https://developers.notion.com/docs/getting-started)
>**note info**
> You should have owner ship of your workspace
> If you need more custom with discord or any apps. see bellow video. (Notion Public)
> https://www.youtube.com/watch?v=n8WzcnZYOIM
3. set notion key to .env file : ref to .env_template
~~~.env
NOTION_DB_ID = "str : length(13)"
NOTION_API_KEY = "str : Any(XX)" <= HERE!!!
~~~
4. get notion database id from url ( see [docs](https://developers.notion.com/docs/getting-started#step-2-share-a-database-with-your-integration))
~~~
https://www.notion.so/myworkspace/a8aec43384f447ed84390e8e42c2e089?v=...
                                  |--------- Database ID --------|
~~~
copy database id to NOTION_DB_ID
~~~.env
NOTION_DB_ID = "str : length(13)" <= HERE!!!
NOTION_API_KEY = "str : Any(XX)" 
~~~


### Setup Python Env
>**note info**
> python == 3.10.6
> OS == OSX(11.4)
> CPU == Intel Core i9
> Sorry... I did not checked another python version and devices.

~~~sh
mkdir venv
cd venv
python3.10 -m venv bibWithNotion
cd ..
source venv/bibWithNotion/bin/activate
pip3 install -r requirement.txt
~~~

### Store Bib Files
Store .bib files into .bibfiles/
You can change target file directry by cli arguments.
(see Use With CLI section) 

> **note warn**
> Now, you can only use https://www.connectedpapers.com/ type .bib files


### Use With CLI


### Use With Notebook

