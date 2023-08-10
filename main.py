import requests


with open('sites_to_sort.txt', 'r')as f:
    content = f.read()
    sitesListed = content.split(',')

dictOfResponses = {}
for site in sitesListed:
    dictOfResponses[site] = requests.get(site).status_code

for key, value in dictOfResponses.items():
    try:
        with open(f'{value}.txt', 'a') as f:
            f.write(key + '\n')
    except FileNotFoundError:
        with open(f'{value}.txt', 'w')as f:
            f.write(key + '\n')


