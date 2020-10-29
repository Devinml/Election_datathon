import pandas as pd
import json

class DfJson(object):
    def __init__(self,file_path):
        self.file_path = file_path
        self.df = self.convert_to_df()
    
    def convert_to_df(self):
        with open(self.file_path,'r') as json_file:
            json_strings = list(json_file)

        json_list = []
        for tweet in json_strings:
            json_list.append(json.loads(tweet))
        df = pd.DataFrame(json_list)
        return df

if __name__ == '__main__':
    file_path = 'data/concatenated_abridged.jsonl'
    data = DfJson(file_path)
    data.df.to_pickle('data/pkl_df/df.pkl')