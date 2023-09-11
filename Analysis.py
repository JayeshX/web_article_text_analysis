import string
import pyphen
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob



class Analysis:
    negative_words_file_path = 'C://Users//User//PycharmProjects//text_analysis_on_web_articles//WordLists//NegativeWords.txt'
    stopwords_file_path = 'C://Users//User//PycharmProjects//text_analysis_on_web_articles//WordLists//StopWords.txt'
    def get_average_sentence_length(self, text_file):
        # Read the text file
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Tokenize the text into sentences
        sentences = nltk.sent_tokenize(text)

        # Calculate the total number of words and sentences
        total_words = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences)
        total_sentences = len(sentences)

        # Calculate the average sentence length
        if total_sentences > 0:
            average_length = total_words / total_sentences
        else:
            average_length = 0

        return average_length

    def average_word_count(self, text_file):
        with open(text_file, 'r', encoding='utf-8') as file:
            data = file.read()
            lines = data.split()
            s = 0
            ns = 0
            ns += len(lines)
            for t in lines:
                if t[-1] == ".":
                    s = s + len(t) - 1
                else:
                    s = s + len(t)

            return (s / ns)

    def get_complex_word_count(self, text_file):
        # Read the text file
        nw = 0
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()
        dic = pyphen.Pyphen(lang='en')
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        text = text.lower()
        words = text.split()
        complex_word_count = 0
        for word in words:
            syllables = dic.inserted(word).count('-') + 1
            if syllables >= 3:
                complex_word_count += 1

        return complex_word_count

    def get_negative_score(self,text_file, negative_words_file, stopwords_file):
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        with open(negative_words_file, 'r',encoding='utf-8') as file:
            negative_words = set(word.strip() for word in file)

        with open(stopwords_file, 'r',encoding='utf-8') as file:
            stopwords = set(word.strip() for word in file)

        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        text = text.lower()
        words = text.split()

        negative_score = sum(1 for word in words if word in negative_words and word not in stopwords)

        return negative_score

    def count_personal_pronouns(self,text_file):
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        personal_pronouns = ['i', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours',
                             'you', 'your', 'yours', 'he', 'him', 'his', 'she',
                             'her', 'hers', 'it', 'its', 'they', 'them', 'their', 'theirs']

        words = text.lower().split()

        personal_pronoun_count = sum(word in personal_pronouns for word in words)

        return personal_pronoun_count

    def get_polarity_score(self,text_file):
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        analyzer = SentimentIntensityAnalyzer()

        sentiment_scores = analyzer.polarity_scores(text)
        polarity_score = sentiment_scores['compound']

        return polarity_score

    def get_positive_score(self,text_file, positive_words_file, stopwords_file):

        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()
        with open(positive_words_file, 'r', encoding='utf-8') as file:
            positive_words = set(word.strip() for word in file)

        with open(stopwords_file, 'r', encoding='utf-8') as file:
            stopwords = set(word.strip() for word in file)

        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        text = text.lower()
        words = text.split()

        positive_score = sum(1 for word in words if word in positive_words and word not in stopwords)

        return positive_score

    def no_words_per_sentence(self,text_file):
        with open(text_file, 'r',encoding='utf-8') as file:
            number_of_words = 0
            data = file.read()
            lines = data.split()
            number_of_words += len(lines)
            sentences = data.split(".")
            ns = len(sentences) - 1  # function call
            if ns==0:
                return 0
            else:
                return number_of_words / ns  # printing result

    def get_subjectivity_score(self,text_file):
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        blob = TextBlob(text)

        subjectivity_score = blob.sentiment.subjectivity

        return subjectivity_score

    def get_syllable_word_count(self,text_file):
        nw = 0
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()
            lines = text.split()
            nw += len(lines)

        dic = pyphen.Pyphen(lang='en')

        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        text = text.lower()
        words = text.split()

        syll = 0
        for word in words:
            syllables = dic.inserted(word).count('-') + 1
            syll = syll + syllables

        return syll / nw

    def word_count(self,text_file):
        number_of_words = 0
        with open(text_file, 'r',encoding='utf-8') as file:
            data = file.read()
            lines = data.split()
            number_of_words += len(lines)
        return number_of_words