from crossref.restful import Works, Journals



journal_list = ["ts", "or", "tits", "trb"]
issn_dict = {
    "ts" : "0041-1655",
    "tits" : "1558-0016",
    "trb" : "",
}

works = Works()
journals = Journals()
issn = issn_dict["tits"]
jw = journals.works(issn)
j = journals.journal(issn)
# jw_fil = jw.filter(from_online_pub_date="2021")
jw_fil = jw.sort("published").sample(100)
# print(jw_fil.count())
# for x in :
# for x in jw.all():
print("requesting...")
for x in jw_fil:
    print(x["title"][0])
    print(x["DOI"])
    print(x["published"]["date-parts"][0])
# w = works.doi("10.1287/trsc.2022.1196")
# print(j)
# ag = works.agency('10.1590/0102-311x00133115')
# print(ag)


print("done.")