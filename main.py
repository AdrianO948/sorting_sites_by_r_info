import requests


def open_file_and_write_content_into_list(file_name):
    while True:
        try:
            file_to_read = open(f'{file_name}', 'r')
        except FileNotFoundError:
            file_name = input('File not found! Please enter valid file name (without extension): ' + '.txt')
            continue
        else:
            split_lines_list = file_to_read.read().split(',')
            file_to_read.close()
            return split_lines_list


def getting_requests_codes_into_dict(list_of_sites):
    dict_of_responses = {}
    for site in list_of_sites:
        dict_of_responses[site] = requests.get(site).status_code

    return dict_of_responses


def writing_request_codes_to_files(dictionary_of_responses):
    for key, value in dictionary_of_responses.items():
        try:
            with open(f'{value}.txt', 'a')as f:
                f.write(key + '\n')
        except FileNotFoundError:
            with open(f'{value}.txt', 'w')as f:
                f.write(key + '\n')


fileName = 'sites_to_sort.txt'
listedSites = open_file_and_write_content_into_list(fileName)
dictOfResponses = getting_requests_codes_into_dict(listedSites)
writing_request_codes_to_files(dictOfResponses)
