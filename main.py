from crossref.restful import Works, Journals
import json
import requests
import time
import pathlib

root_dir = pathlib.Path(__file__).absolute().parent

journal_list = ["ts", "or", "tits", "trb"]
issn_dict = {
    "ts" : "0041-1655",
    "tits" : "1558-0016",
    "trb" : "",
}

def save_one_item(dd):
    doi = dd["DOI"]
    doi_suffix = doi.split("/")[1]
    file_path = root_dir.joinpath("meta").joinpath(doi_suffix+".json") 
    if file_path.exists():
        print(f"skip {file_path}.")
        return

    if not "abstract" in dd:
        api_url = "https://api.semanticscholar.org/graph/v1/paper/" + doi + "?fields=abstract"
        r = requests.get(api_url)
        abstract = r.json()["abstract"]
        dd["abstract"] = abstract
        time.sleep(3)
    js_obj = json.dumps(dd, indent=4)
    with open(file_path, "w") as f:
        f.write(js_obj)
        print(f"{file_path} saved.")

works = Works()
journals = Journals()
issn = issn_dict["tits"]
jw = journals.works(issn)
j = journals.journal(issn)
# jw_fil = jw.filter(from_online_pub_date="2021")
# jw_fil = jw.sort("published").filter(has_abstract="true").sample(1)
jw_fil = jw.sort("published").sample(5)
doi = "10.1287/trsc.2022.1196"

# print(jw_fil.count())
# for x in :
# for x in jw.all():
print("requesting crossref...")
for x in jw_fil:
    doi = x["DOI"]
    # print(x["DOI"])
    save_one_item(x)
    print(x["title"][0])
    # print(x["published"]["date-parts"][0])

# w = works.doi("10.1287/trsc.2022.1196")
# print(j)
# ag = works.agency('10.1590/0102-311x00133115')
# print(ag)


print("done.")