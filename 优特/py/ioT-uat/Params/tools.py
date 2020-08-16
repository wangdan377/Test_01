import os
import os.path
import yaml

'''
读取所有yaml数据
'''
def parse():
    path_ya=str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))+'/Params/Yaml'
    pages={}
    for root,dirs,files in os.walk(path_ya):
        for name in files:
            watch_file_path=os.path.join(root,name)
            with open(watch_file_path,'r') as f:
                page =yaml.safe_load(f)
                pages.update(page)
        return pages

'''
读取yaml中的parameters
'''
class GetPages:
    @staticmethod
    def get_page_list():
        _page_list={}
        pages=parse()
        for page,value in pages.items():
            parameters=value['parameters']
            data_list=[]

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page]=data_list

        return _page_list


if __name__ == "__main__":
    lists=GetPages.get_page_list()
    # print(lists)
