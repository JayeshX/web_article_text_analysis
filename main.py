import pandas as pd
import nltk
import Analysis

d = Analysis.Analysis()
# Example usage
print("average sentence lengths")

dataframe1 = pd.read_excel('C:/Users/User/Desktop/interndrive/input.xlsx')
negative_words_file_path = 'C:/Users/User/Desktop/internship docs/negative-words.txt'
stopwords_file_path = 'C:/Users/User/Desktop/internship docs/stopwords.txt'
positive_words_file_path = 'C:/Users/User/Desktop/internship docs/positive-words.txt'
ids = []
for index, row in dataframe1.iterrows():
    url = row['URL_ID']
    ids.append(url)
data = []
al = []
avc = []
cwc = []
ns = []
cpp = []
pols = []
ps = []
nwps = []
ss = []
swc = []
wc = []
for i in ids:
    text_file_path = "C:/Users/User/Desktop/git trial/" + str(i) + ".txt"
    average_length = d.get_average_sentence_length(text_file_path)
    al.append(average_length)
    averge_words = d.average_word_count(text_file_path)
    avc.append(averge_words)
    complex_words = d.get_complex_word_count(text_file_path)
    cwc.append(complex_words)
    negative_score = d.get_negative_score(text_file_path, negative_words_file_path, stopwords_file_path)
    ns.append(negative_score)
    count_personal_pronoun = d.count_personal_pronouns(text_file_path)
    cpp.append(count_personal_pronoun)
    polarity_score = d.get_polarity_score(text_file_path)
    pols.append(polarity_score)
    positive_score = d.get_positive_score(text_file_path, positive_words_file_path, stopwords_file_path)
    ps.append(positive_score)
    words_per_sentence = d.no_words_per_sentence(text_file_path)
    nwps.append(words_per_sentence)
    sub_score = d.get_subjectivity_score(text_file_path)
    ss.append(sub_score)
    syl_count = d.get_syllable_word_count(text_file_path)
    swc.append(syl_count)
    word_count = d.word_count(text_file_path)
    wc.append(word_count)

cmpx_percentage = []
fog_index = []
j = 0
for i in ids:
    complex_percentage = (cwc[j] / wc[j]) * 100
    cmpx_percentage.append(complex_percentage)
    fg = 0.4*(nwps[j]+ complex_percentage)
    fog_index.append(fg)
    j += 1

data = {'IDS': ids,
        'Average Length': al,
        'Average Word Count': avc,
        "Complex Word Count": cwc,
        'Negative Score': ns,
        'Personal Pronouns Count': cpp,
        'Polarity Score': pols,
        'Positivity Score': ps,
        'Number Of Word Per Sentence': nwps,
        'Subjectivity Score': ss,
        'Syallable Word Count': swc,
        'Word count': wc,
        'Complex Words %': cmpx_percentage,
        'Fog Index' : fog_index
        }
df = pd.DataFrame(data)
print(df)
df.to_excel('C:/Users/User/Desktop/git trial/output.xlsx')
