from os import listdir
from os.path import isfile, join, abspath
import json

DATA_DIR = abspath("../data")
PROJECT_NAME_FILE = "projects"
REPO_SERVER = "https://github.com"
AUTHOR = "edgarmejiav"

LANG_TEMPLATE_VARIABLE = "@LANGUAGES"

def replace_lang(raw: str, langs: list) -> str:
    langs = [ f"<a href=\"{REPO_SERVER}/{AUTHOR}/{AUTHOR}/blob/main/README_{l}.md\">{l}</a>" for l in langs if len(l) > 0]
    return raw.replace(LANG_TEMPLATE_VARIABLE, "&nbsp;|&nbsp;".join(langs))

def get_projects_data(name: str = PROJECT_NAME_FILE, lang: str = "") -> list:
    if len(lang) > 0:
        lang = f".{lang}"
    json_file = open(join(DATA_DIR, f"{name}{lang}.json"))
    return json.load(json_file)

def get_all_by_lang() -> dict:
    data = {}
    files = get_all_files()
    for (name, lang) in files:
        data_json = get_projects_data(name, lang)
        if len(lang) == 0:
            data[name] = data_json
        else:
            if not name in data:
                data[name] = {}
            data[name][lang] = data_json
    return data

# get all json data files in data directory
def get_all_files() -> list:
    files = []
    for f in listdir(DATA_DIR):
        if isfile(join(DATA_DIR, f)) and f.endswith(".json"):
            f_split = f.split(".")
            name, lang = f_split[0], ""
            if len(f_split) == 3:
                lang = f_split[1]
            files.append((name, lang))
    return files