from crossref.restful import Works, Journals
import json
import requests
import time
import pathlib
from config import *
import config
import datetime
from abstract import add_abstract
import abstract
import psutil

def save_one_item(dd):
    doi = dd["DOI"]
    file_path = config.get_file_path_doi(doi)
    if file_path.exists():
        print(f"skip {file_path}.")
        return

    if not "abstract" in dd:
        try:
            add_abstract(dd)
        except: 
            print(f"Failed to add abstract for {file_path}.")
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
    if jour == "tits":
        jw_fil = jw.sort("published").sample(100)
    else:
        jw_fil = jw.sort("published").sample(n_sample_per_journal)
    
    for x in jw_fil:
        doi = x["DOI"]
        save_one_item(x)
        print(x["title"][0])


# A robust way to quit Firefox driver.
# Refer to https://stackoverflow.com/questions/48703734/why-does-the-python-selenium-webdriver-quit-not-quit
driver = abstract.driver
driver_process = psutil.Process(driver.service.process.pid)

if driver_process.is_running():
    print ("driver is running")

    firefox_process = driver_process.children()
    if firefox_process:
        firefox_process = firefox_process[0]

        if firefox_process.is_running():
            print("Firefox is still running, we can quit")
            driver.quit()
        else:
            print("Firefox is dead, can't quit. Let's kill the driver")
            firefox_process.kill()
    else:
        print("driver has died")

print("done.")