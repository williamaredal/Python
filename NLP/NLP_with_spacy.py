import spacy

from spacy.tokenizer import Tokenizer
from spacy.lemmatizer import Lemmatizer
from spacy.lookups import Lookups

from spacy.pipeline import TextCategorizer


exampleText = "When learning data science, you shouldn't get discouraged! Challenges and setbacks aren't failures, they're just part of the journey. You've got this! This sentence is about being able to abolish things."
exampleText2 = """Anthony Fauci warned us last week that Covid-19 is likely to be hanging over our lives well into 2021. He’s right, of course. We need to accept this reality and take steps to meet it rather than deny his message.

Many Americans are resistant to this possibility. They’re hoping to restart postponed sports seasons, attend schools more easily, enjoy rescheduled vacations and participate in delayed parties and gatherings.

It is completely understandable that many are tiring of restrictions due to Covid-19. Unfortunately, their resolve is weakening right when we need it to harden. This could cost us dearly.

The unrealistic optimism stems in part from the fact that people have started pinning their hopes on a medical breakthrough. There have been promising developments. Remdesivir holds potential for those who are hospitalized. Convalescent plasma might do the same. Antibody treatments might improve outcomes for some or prevent infections in those at highest risk.

But most cases don’t benefit from these treatments. Further, none of these therapies can prevent infections or hospitalizations on a broad scale. The concern over an unflattened curve isn’t just about death, although that’s certainly a concern. It’s also about an overwhelmed health care system where so many beds are filled that we can’t get care for the many other conditions people experience. Untreated or undertreated heart attacks, strokes, cancer and more will also cause a spike in morbidity and mortality.

Americans are also overestimating what a vaccine might do. Many are focusing on whether approval is being rushed as a campaign ploy, but that’s almost beside the point. It seems likely that a vaccine will be approved this fall and that it will be “effective.” But it’s very unlikely that this vaccine will be a game changer.
"""


# Function that checks how vague a texts is
def HowFuzzy(language, text):
    languageList = { "english" : "en_core_web_sm", "norwegian" : "nb_core_news_sm"}
    selectedLanguage = languageList[language.lower()]

    nlp = spacy.load(selectedLanguage)
    tokenizer = Tokenizer(nlp.vocab)

    fillerWords = [w.text for w in tokenizer(text) if w.is_stop]
    contentWords = [w.text for w in tokenizer(text) if not w.is_stop]
    ratio = len(fillerWords) / len(contentWords)
    
    return ratio



# Function that counts the number of sentences in a text
def SentenceNumber(language, text):
    languageList = { "english" : "en_core_web_sm", "norwegian" : "nb_core_news_sm"}
    selectedLanguage = languageList[language.lower()]

    nlp = spacy.load(selectedLanguage)
    doc = nlp(text)
    sentences = [sent.string.strip() for sent in doc.sents]

    return len(sentences)



# Makes list of positive sentiment words from positiveWords
def SentimentLists():
    try:
        from Sentiment_list import positiveList, negativeList
        from Positive_words import positiveWords
        from Negative_words import negativeWords

        if positiveList is None or negativeList is None:
            listPositive = [word for word in positiveWords.split()]
            listNegative = [word for word in negativeWords.split()]

            listFile = open('Sentiment_list.py', 'w')
            listFile.write('positiveList = ' + str(listPositive) + '\n' + '\n')
            listFile.write('negativeList = ' + str(listNegative) + '\n' + '\n')
            listFile.close()

        else:
            listPositive = 'These already exists'

    except ImportError:
        from Positive_words import positiveWords
        from Negative_words import negativeWords

        listPositive = [word for word in positiveWords.split()]
        listNegative = [word for word in negativeWords.split()]

        listFile = open('Sentiment_list.py', 'w')
        listFile.write('positiveList = ' + str(listPositive) + '\n' + '\n')
        listFile.write('negativeList = ' + str(listNegative) + '\n' + '\n')

        listFile.close()



# Function that finds overall sentiment of text using BOW
def Sentiment(language, text):
    try:
        from Sentiment_list import positiveList
        from Sentiment_list import negativeList
        
        languageList = { "english" : "en_core_web_sm"}
        selectedLanguage = languageList[language.lower()]
        
        positive = 0
        negative = 0
        
        nlp = spacy.load(selectedLanguage)
        doc = nlp(text)

        for token in doc:
            print(token.text, token.pos_)

        for w in text.split():

            if w.lower() in positiveList:
                positive += 1

            if w.lower() in negativeList:
                negative += 1

        if positive != 0 and negative != 0:
            ratio = (positive / negative) 
            print(ratio)

            if ratio < 0.2 and ratio > 0:
                print("this text is overwhelmingly negative")

            elif ratio < 0.4 and ratio >= 0.2:
                print("this text is really negative")        

            elif ratio < 0.6 and ratio >= 0.4:
                print("this text is mostly negative")
            
            elif ratio < 0.8 and ratio >= 0.6:
                print("this text is somewhat negative")
            
            elif ratio < 1 and ratio >= 0.8:
                print("this text is slightly negative")  


            elif ratio == 1:
                print("this text is neutral")


            elif ratio > 1 and ratio <= 1.2:
                print("this text is slightly positive")
            
            elif ratio > 1.2 and ratio <= 1.4:
                print("this text is favourably positive")
            
            elif ratio > 1.4 and ratio <= 1.6:
                print("this text is mostly positive")
            
            elif ratio > 1.6 and ratio <= 1.8:
                print("this text is hugely positive")
            
            elif ratio > 1.8:
                print("this text is overwhelmingly positive")

    except ImportError:
        print('Could not import sentiment lists required')

    return (positive, negative)



# Function that finds number of instances the word-base is in the text
def WordCount(language, text, word):
    languageList = { "english" : "en_core_web_sm", "norwegian" : "nb_core_news_sm"}
    selectedLanguage = languageList[language.lower()]

    nlp = spacy.load(selectedLanguage)
    doc = nlp(text)
    w = nlp(word)

    lemmas = [token.lemma_ for token in doc]
    i = lemmas.count(w[0].lemma_)

    return i


# Function call for positive and negative word list creation
#SentimentLists()

# Function calls:
#print(HowFuzzy("English", exampleText))
#print(SentenceNumber("English", exampleText))
#print(Sentiment("English", exampleText2))
#print(WordCount("English", exampleText2, "they"))