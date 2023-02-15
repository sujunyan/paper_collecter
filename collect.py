from crossref.restful import Works, Journals
import json
import requests
import time
import pathlib
from config import *
import config
import datetime


def save_one_item(dd):
    doi = dd["DOI"]
    file_path = config.get_file_path_doi(doi)
    if file_path.exists():
        print(f"skip {file_path}.")
        return

    if not "abstract" in dd:
        api_url = "https://api.semanticscholar.org/graph/v1/paper/" + doi + "?fields=abstract"
        r = requests.get(api_url)
        time.sleep(3)
        if r.ok:
            abstract = r.json()["abstract"]
            dd["abstract"] = abstract
        else:
            print(f"{doi} not found on semantic scholar.")
            return
    js_obj = json.dumps(dd, indent=4)
    with open(file_path, "w") as f:
        f.write(js_obj)
        print(f"{file_path} saved.")


print(f"starting collect paper metadata at {datetime.datetime.now()}")
journals = Journals()
for jour in journal_list:
    print(f"requesting crossref for {jour}")
    issn = issn_dict[jour]
    jw = journals.works(issn)
    jw_fil = jw.sort("published").sample(n_sample_per_journal)
    
    for x in jw_fil:
        doi = x["DOI"]
        save_one_item(x)
        print(x["title"][0])

print("done.")