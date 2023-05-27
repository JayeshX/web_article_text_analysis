# web_article_text_analysis
The project extracts texts from web articles from a defined url's in an excel sheet. once extracted they are stored in text format in the system. These text files are then used for basic text analysis

# Web Extraction 
during this phase WebTextExtraction file extracts text from website, you can change the extraction code for a specific website or a specific content

# data processing
based on the data extracted there were some unnecessary information in the text files, so i used the RemoveFooters to identify the structure of text and remove unwanted data.

# Analysis 
Various basic parameters for text analysis are used and codes written in the file Analysis.py
the parameters are:
* Average Sentence Length
*	Average Word Count
*	Complex Word Count
*	Negative Score
*	Personal Pronouns Count
*	Polarity Score
*	Positive Score
*	Words Per Sentence
*	Subjectivity Score
*	Syllables Per Word
*	Fog Index

# Storing
once all the parameters are calculated they are stored in an excel sheet for further analysis
