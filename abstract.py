
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

def add_abstract(dd):
    doi = dd["DOI"]
    abstract = get_abstract(doi)
    dd["abstract"] = abstract
    # api_url = "https://api.semanticscholar.org/graph/v1/paper/" + doi + "?fields=abstract"
    # r = requests.get(api_url)
    # time.sleep(3)
    # if r.ok:
    #     abstract = r.json()["abstract"]
    #     dd["abstract"] = abstract
    # else:
    #     print(f"{doi} not found on semantic scholar.")

    return dd
 
# url = "https://scrapeme.live/shop/" 
 


def get_abstract(doi):

    url = f"https://www.doi.org/{doi}"
# driver = webdriver.PhantomJS()
    # driver.get("https://www.doi.org/10.1016/j.trb.2023.02.001")
    driver.get(url)
    # time.sleep(3)
    # innerHTML = driver.execute_script("return document.body.innerHTML")
    if "trb" in doi:
        xpath = "//div[@id='abstracts']/div[2]/div/p"
    elif ("opre" in doi) or ("trsc" in doi):
        xpath = "//div[@class='hlFld-Abstract']/div/p[1]"
    elif "tits" in doi:
        xpath = "//div[@class='u-mb-1']/div"
    else:
        return None
        # raise Exception("unknown doi.")

    # wait for the web to render the page
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element = driver.find_element(By.XPATH, xpath)
    abstract = element.text

    return abstract

# element = driver.find_element(By.ID, "abstracts")
# element = driver.find_element(By.CLASS_NAME, "abstract author")
# print(innerHTML)
# doi = "10.1016/j.trb.2023.02.001"
if __name__ == "__main__":
    doi = "10.1287/opre.2022.2412"
    doi = "10.1109/tits.2023.3241281"
    doi = "10.1109/tits.2023.3240500"
    doi = "10.1287/trsc.2022.1158"
    abstract = get_abstract(doi)
    print(abstract)
    print("done.")
# with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver: 
# 	driver.get(url)