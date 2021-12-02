import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

table = PrettyTable([4 * ' ', 30 * ' ', 'MJ   ', 'V   ', 'E   ', 'Î   ', 'GM   ', 'GP   ', 'G   ', 'P   '])

f = open("clasament.txt", "w")
URL = 'https://lpf.ro/liga-1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

rows = soup.find(id='nr_etapa_clasament').text.strip()
f.write("CLASAMENT LIGA 1 - ETAPA " + rows + 2 * '\n')

results_table = soup.find(id='clasament_ajax')
team_rows = results_table.find_all(class_='echipa_row')

for team in team_rows:
    team_cell = team.find('td', class_='echipa')
    team_name = team_cell.find('a').text.strip()
    team_position = team.find('td', class_='poz').text.strip()
    team_points = team.find('td', class_='puncte').text.strip()
    my_list = list(team)[4:12]

    table.add_row([team_position, team_name, my_list[0].text.strip(), my_list[1].text.strip(), my_list[2].text.strip()
                   , my_list[3].text.strip(), my_list[4].text.strip(), my_list[5].text.strip(), my_list[7].text.strip()
                   , team_points])

table.align = 'l'
f.write(table.get_string())
