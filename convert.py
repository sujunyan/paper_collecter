"""
convert the metadata to the readable markdown
"""

import config
import json
import pathlib
import datetime

class Paper:
    def __init__(self, raw_data) -> None:
        self.raw_data = raw_data
        self.title = raw_data["title"][0]
        self.abstract = raw_data["abstract"]
        if self.abstract is not None:
            self.abstract = self.abstract.replace("<jats:p> ", "")
            self.abstract = self.abstract.replace(" </jats:p>", "")
            pass
        self.doi = raw_data["DOI"]
        self.journal = raw_data["short-container-title"][0]
        date_parts = raw_data["published"]["date-parts"][0]
        if len(date_parts) == 2:
            date_parts.append(1)
        if len(date_parts) == 1:
            date_parts = [date_parts[0], 1, 1]
            
        self.date = datetime.datetime(*date_parts)

    def __lt__(self, other):
        return self.date < other.date
    
    def to_md_str(self):
        """
        convert it to a markdown str for output.
        """
        out_str =  f"**Title: {self.title}**\n\n"
        out_str += f"**Date:** {self.date.strftime('%Y-%m-%d')}\n\n"
        link = f"doi.org/{self.doi}"
        out_str += f"**Link:** [{link}](https://www.{link})\n\n" 
        out_str += f"**Journal:** {self.journal}\n\n"
        out_str += f"**Abstract:** {self.abstract}\n\n"
        return out_str
        
data_dir = config.root_dir.joinpath("meta")

file_list = data_dir.glob("*.json")
paper_list = []
for fl_str in file_list:
    with open(fl_str) as fd:
        data = json.load(fd)
        print(data["title"][0])
        paper = Paper(data)
        paper_list.append(paper)
    # print(fl_str)
paper = paper_list[0]
# print(paper.to_md_str())
paper_list.sort(reverse=True)

# with open("/home/sujy/dev/paper_collecter/meta/opre.2022.2429.json") as f:
#     d = json.load(f)
nsample = 20
with open(config.root_dir.joinpath("papers.md"), "w") as fd:
    for p in paper_list[1:nsample]:
        fd.write(p.to_md_str())
        fd.write("\n---\n")
        # print(p.date)

print("done.")