import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path=r'C:\Users\55719\Desktop\Programing\chromedriver.exe')
page_number = 1
# Url with a variable in the end to choose the page where the complain links will be saved
# With a for loop the pages will go through the ReclameAqui complain pages appending the links of the complains to the
# Links list

url = "https://www.reclameaqui.com.br/empresa/delboni-auriemo-medicina-diagnostica/lista-reclamacoes/?pagina=" + str(
    page_number)
# List of the links. The Function 'getting_elements' will get each url from the links list
links = []
#Lists Of the information that will be saved on the DataFrame
lst_data_complains = []
lst_id_complains = []
lst_location_complains = []
lst_titles_complain = []
lst_status_complain = []

driver_path = r'C:\Users\55719\Desktop\Programing\chromedriver.exe'
def getting_elements(url, driver_path):
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url)
    try:
        info_complain = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "col-md-10"))
        )
        status_complain = driver.find_element_by_class_name("img-mobile-status").get_attribute('alt')
        lst_status_complain.append(status_complain)
        # Turning the html into normal text in order to split the information and sort them into the lists
        page_info = info_complain.text
        # print(informacao_da_pagina)

        divided_page_info = page_info.split("\n")
        # print(informacao_da_pagina_dividida)

        complain_title = divided_page_info[0]
        lst_titles_complain.append(complain_title)
        # City, ID, Hour/date of the complain
        c_id_h_complain = divided_page_info[2]  # Cidade, id, horário/data

        split1_cidh = c_id_h_complain.split('ID')

        localizacao_da_reclamacao = split1_cidh[0]
        lst_location_complains.append(localizacao_da_reclamacao)

        split2_cidh = c_id_h_complain.split(localizacao_da_reclamacao)

        id_h_da_reclamacao = split2_cidh[1]

        split3_cidh = id_h_da_reclamacao.split(' ')

        id_complain = split3_cidh[1]
        lst_id_complains.append(id_complain)
        global df

        data_complain = split3_cidh[2] + " " + split3_cidh[4]
        lst_data_complains.append(data_complain)

    finally:
        driver.quit()


html_link_complain = driver.find_elements_by_class_name("link-complain-id-complains")

for page_number in range(1, 102):  # For loop going to the next page

    url = "https://www.reclameaqui.com.br/empresa/delboni-auriemo-medicina-diagnostica/lista-reclamacoes/?pagina=" + str(
        page_number)
    driver.get(url)
    sleep(3)
    html_link_complain = driver.find_elements_by_class_name("link-complain-id-complains")
    for every_link_complain in html_link_complain:  # For Loop getting the Complain Links
        link = every_link_complain.get_attribute('href')
        links.append(link)
for every_link in links:  # For Loop going through every link and applying the getting elements function
    getting_elements(every_link)
# Saving the lists with the info in a Dataframe
df = pd.DataFrame({'data_da_reclamacao': lst_data_complains,
                   'titulo_reclamacao': lst_titles_complain,
                   'localizacao_reclamacao': lst_location_complains,
                   'id': lst_id_complains,
                   'status_reclamacao': lst_status_complain})
df.to_csv("Dados_a_Ser_Tratados_Reclame_Aqui.csv", sep=';')

