import pandas as pd

f1 = open('gpt-neo-lyrics-gen/data.txt', "r")
source = f1.readlines()
source = set(source)
source.remove('<|endoftext|>')
for line in list(source):
    if not line[0].isalpha() or line.split()[0] == 'Verse':
        source.remove(line)

f2 = open('gpt-neo-lyrics-gen/predicts.txt')
gpt = f2.readlines()
gpt = set(gpt)
for line in list(gpt):
    if not line[0].isalpha() or line.split()[0] == 'Verse':
        gpt.remove(line)

gpt_clean = gpt - source

f3 = open('gen_markov.txt')
mrkv = f3.readlines()
mrkv = set(mrkv)
for line in list(mrkv):
    if not line[0].isalpha() or line.split()[0] == 'Verse':
        mrkv.remove(line)

mrkv_clean = mrkv - source

df1 = pd.DataFrame.from_dict({'text' : list(source), 'original' : [0]*len(source), 'generated' : [0]*len(source)})
df1.to_csv('texts_project/source.csv')

df2 = pd.DataFrame.from_dict({'text' : list(gpt_clean), 'original' : [0]*len(gpt_clean), 'generated' : [0]*len(gpt_clean)})
df2.to_csv('texts_project/gpt.csv')

df3 = pd.DataFrame.from_dict({'text' : list(mrkv_clean), 'original' : [0]*len(mrkv_clean), 'generated' : [0]*len(mrkv_clean)})
df3.to_csv('texts_project/markov.csv')
