# Use web archive API to generate wayback machine links for reference pages. 

import requests
import yaml

WEBARCHIVE_URL = "http://archive.org/wayback/available?url={url}&timestamp={timestamp}"
YAML_DATA = "_data/talks.yml"


def load_data(fn):
    with open(fn) as f:
        return yaml.safe_load(f)

def get_archive_link(link, event_date): 
    archive_query = WEBARCHIVE_URL.format(url=link, timestamp=event_date.strftime("%Y%m%d"))

    resp = requests.get(archive_query)
    wa_data = resp.json()
    if "archived_snapshots" in wa_data.keys() and wa_data["archived_snapshots"]:
        if "closest" in wa_data["archived_snapshots"].keys():
            archive_link_data = wa_data["archived_snapshots"]["closest"]
            if archive_link_data["status"] == "200": 
                return archive_link_data["url"]
    return None


def list_archive(): 

    data = load_data(YAML_DATA)

    for conf in data:
        event_date = conf["conference"]["date"]


        if "link" in conf["conference"].keys() and "archive_link" not in conf["conference"].keys():
            conf_link = conf["conference"]["link"]
            conf_archive_link = get_archive_link(conf_link, event_date)
            if conf_archive_link: 
                conf["conference"]["archive_link"] = conf_archive_link
            else: 
                print(f"❌ Call: https://web.archive.org/save/{conf_link}")

        for talk in conf["conference"]["talks"]: 
            if "link" in talk.keys() and "archive_link" not in talk.keys(): 
                link = talk["link"]

                if "youtube.com" in link or "youtu.be" in link: 
                    continue
                if "web.archive" in link:
                    continue

                archive_link = get_archive_link(link, event_date)
                
                if archive_link: 
                    talk["archive_link"] = archive_link
                   # print(f"Found link for {archive_link}")
                else:
                    print(f"❌ Call: https://web.archive.org/save/{link}")

    
    with open(YAML_DATA, "w", encoding="utf-8") as file:
        yaml.safe_dump(data, file, sort_keys=False)

if __name__ == "__main__": 
    list_archive()

