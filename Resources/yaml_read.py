'''
DateTime : 15/07/2020 5:53PM
Author   : Positive
File     : GetAPIParam.py
'''

import yaml
import os
import os.path


def parse():
    yml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/Resources/Params'
    pages = {}
    for root, dir, files in os.walk(yml_path):
        for name in files:
            files_path = os.path.join(root, name)
            with open(files_path, 'r') as f:
                page = yaml.safe_load(f)
                pages.update(page)
        return pages


class GetAPIParam:
    @staticmethod
    def get_param():
        _page_list = {}
        pages = parse()

        for page, value in pages.items():
            paramaters = value['parameters']
            data_list = []

            for paramater in paramaters:
                data_list.append(paramater)
            _page_list[page] = data_list

        return _page_list


if __name__ == '__main__':
    lists = GetAPIParam.get_param()
