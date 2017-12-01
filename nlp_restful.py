import string
from urllib.request import urlopen as req

import nltk
from bs4 import BeautifulSoup as soup
from flask import Flask, jsonify, request
from nltk.corpus import stopwords
from nltk.probability import FreqDist

punctuation = set(string.punctuation)
stopwords = set(stopwords.words('english'))

vocabulary = ["said", "'s", "''", "``", "also", "told", "says", "say", "tell",
              "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
              "according", "reported"]


def text_normalization(document):
    WNlemma = nltk.WordNetLemmatizer()

    # improving results excluding tags which are not so important
    exclude_tags = ['IN', 'CD', 'MD', 'LS', 'POS', 'PRP$']
    # standardize each token of the text by lowercasing them
    # removes stopwords (words that don't have much meaning in the analysis) such as 'the', 'as', 'that', etc
    # it keeps only words with a lenth greater than 2
    # it removes words in the vocabulary. The vocabulary is a list of common words in news articles that do not have much meaning in the overall result
    # finally, the line removes numbers and other special characters
    cleaned_document = ' '.join([s.lower() for s in document.split()
                                 if s not in stopwords
                                 if len(s) >= 2
                                 if s not in vocabulary
                                 if s.isalpha()])

    # sentence tokenize the text
    normalized_text = nltk.sent_tokenize(cleaned_document)

    # word tokenize the input text
    normalized_text = [nltk.word_tokenize(s) for s in normalized_text]

    # extract the pos_tag from the text
    pos_tag = [nltk.pos_tag(s) for s in normalized_text]

    # it removes pos_tags elements that are not so important for the overall meaning
    # it removes ponctuation from text, as they are frequent in every article, but don't have any specific meaning
    normalized_text = ' '.join([item[0] for item in [item for item in pos_tag][0]
                                if item[1] not in exclude_tags
                                if item[0] not in punctuation])
    normalized_text = " ".join(WNlemma.lemmatize(word) for word in normalized_text.split())
    return normalized_text


def process_url(urls):
    global cleaned_text
    for item in range(len(urls)):
        print("loaded url {} of {} ".format((item + 1), len(urls)))
        client = req(urls[item])
        raw_html = client.read()
        page_soup = soup(raw_html, "html.parser")
        article_body = page_soup.findAll("div", {"class": "article-body"})
        content = article_body[0]
        speakeable = content.findAll("p", {"class": "speakable"})
        speakeable = [item.text for item in speakeable]
        speakeable_text = ' '.join(speakeable)
        paragraphs = content.findAll("p")
        body_text = [item.text for item in paragraphs]
        joined_text = ' '.join(speakeable_text)
        joined_text = ' '.join(body_text)
        cleaned_text = text_normalization(joined_text.strip())
    print("process completed!")
    # return pd.DataFrame(extracted_content)
    return cleaned_text


def text_tokenize(string):
    return nltk.word_tokenize(string)


def frequent_terms(normalized_text):
    # creates an object with the frequency of each word in the text
    freq_dist = FreqDist(text_tokenize(normalized_text))

    # unpacks the terms and the respective frequency
    (terms, frequency) = zip(*[(item[0], item[1])
                               for item in freq_dist.most_common()
                               if item[0].isalpha()
                               if item[0] not in punctuation
                               if item[0] not in stopwords
                               if item[0] not in vocabulary
                               if len(item[0]) > 2
                               if item[1] >= 2][:10])
    return (terms, frequency)


app = Flask(__name__)

## Create RESTful webservice route with POST method
@app.route('/api', methods=['POST'])
## This function receives a website url passed as parameter, scrap it,
## and extracts the keywords which most represent the text,
## then return them to the caller
def extract_keywords():
    ## get the request parameters
    data = request.get_json(force=True)
    ## extract only the desired parameter
    ## (in this case, there is only 1, but if more, you can select all or specify which one to pick)
    request_url = data['url']
    ## call the frequent_terms function passing the scrapped and cleaned news article
    most_frequent_terms = frequent_terms(process_url([request_url]))
    ## it returns the extracted keywords and their respective weights,
    ## which are useful to draw and visualize the importance of each term
    return jsonify(results=most_frequent_terms)


if __name__ == '__main__':
    ## run the API, waiting for requests on port 9000
    app.run(port=9000, debug=True)
