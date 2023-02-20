import pathlib

root_dir = pathlib.Path(__file__).absolute().parent

issn_dict = {
    "ts" : "0041-1655",
    "tits" : "1558-0016",
    "trb" : "0191-2615",
    "or" : "1526-5463",
}
n_sample_per_journal = 10
journal_list = list(issn_dict.keys())

def get_file_path_doi(doi):
    doi_suffix = doi.split("/")[1]
    file_path = root_dir.joinpath("meta").joinpath(doi_suffix+".json") 
    return file_path