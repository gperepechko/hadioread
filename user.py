from dataclasses import dataclass
import pandas as pd
import random

# @dataclass
# class Dataset:
#     : str
#     df: pd.DataFrame

class User: 
    def __init__(self) -> None:
        self.lines = []
        self.cur_line = 0
        self.n_correct = 0
        self.n_questions = None
    
    def load_dataset(self, n_questions=10):
        self.n_questions = n_questions
        datasets = []
        datasets.append(pd.read_csv('texts_project/source.csv'))
        datasets.append(pd.read_csv('texts_project/gpt.csv'))
        datasets.append(pd.read_csv('texts_project/markov.csv'))

        for _ in range(n_questions):
            i_dataset = random.randint(0, len(datasets) - 1)
            dataset = datasets[i_dataset]
            ind = random.randint(0, len(dataset) - 1)
            dct_line = {'line': dataset['text'].iloc[ind],
                        'i_file': i_dataset,
                        'i_line': ind,
                        'correct': False}
            
            self.lines.append(dct_line)

    
    def get_score(self):
        if self.cur_line == 0:
            return 0
        return round(self.n_correct / self.cur_line * 100, 2)

    def add_answer(self, answer):
        if self.cur_line >= len(self.lines):
            return
        if answer == (self.lines[self.cur_line]['i_file'] == 0):
            self.n_correct += 1
            self.lines[self.cur_line]['correct'] = True
        else:
            self.lines[self.cur_line]['correct'] = False
        self.cur_line += 1

    def get_line(self):
        if self.cur_line >= len(self.lines):
            return  None
        return f'Question: {self.cur_line + 1} / {self.n_questions}:\n' + \
            self.lines[self.cur_line]['line']
