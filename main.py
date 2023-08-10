import requests


def open_file_and_write_content_into_list(file_name):
    try:
        with open(f'{file_name}', 'r')as file_to_read:
            pass
    except FileNotFoundError:
        return 'File not found!'
    else:
        return file_to_read.read().split(',')


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


