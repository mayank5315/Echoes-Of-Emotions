import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

class CustomerFeedbackAnalyzer:
    def __init__(self):
        """Initialize sentiment analyzer"""
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
    
    def analyze_sentiment(self, text):
        """Analyze sentiment using NLTK's VADER"""
        scores = self.sentiment_analyzer.polarity_scores(text)
        compound = scores['compound']
        
        if compound >= 0.05:
            sentiment = 'positive'
        elif compound <= -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
            
        return {
            'sentiment': sentiment,
            'score': compound,
            'details': scores
        }
    
    def generate_summary(self, text):
        """Generate an improved summary of likes and dislikes using NLTK phrase extraction and frequency analysis"""
        from nltk.tokenize import sent_tokenize, word_tokenize
        from nltk.corpus import stopwords
        from nltk import pos_tag, ne_chunk
        from nltk.chunk import RegexpParser
        from collections import Counter
        import string

        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)

        stop_words = set(stopwords.words('english'))
        sentences = sent_tokenize(text)

        liked_phrases = []
        disliked_phrases = []

        # Define a simple grammar for noun phrase chunking
        grammar = r"""
          NP: {<JJ>*<NN.*>+}   # Adjective(s) + Noun(s)
        """
        chunk_parser = RegexpParser(grammar)

        for sentence in sentences:
            scores = self.sentiment_analyzer.polarity_scores(sentence)
            compound = scores['compound']
            if compound >= 0.05:
                # Extract noun phrases from positive sentences
                words = word_tokenize(sentence)
                words = [w for w in words if w.lower() not in stop_words and w not in string.punctuation]
                tagged = pos_tag(words)
                tree = chunk_parser.parse(tagged)
                for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
                    phrase = " ".join(word for word, tag in subtree.leaves())
                    liked_phrases.append(phrase)
            elif compound <= -0.05:
                # Extract noun phrases from negative sentences
                words = word_tokenize(sentence)
                words = [w for w in words if w.lower() not in stop_words and w not in string.punctuation]
                tagged = pos_tag(words)
                tree = chunk_parser.parse(tagged)
                for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
                    phrase = " ".join(word for word, tag in subtree.leaves())
                    disliked_phrases.append(phrase)

        # Count frequency of phrases and get most common ones
        liked_counter = Counter(liked_phrases)
        disliked_counter = Counter(disliked_phrases)

        # Select top 5 phrases or less
        top_liked = [phrase for phrase, count in liked_counter.most_common(5)]
        top_disliked = [phrase for phrase, count in disliked_counter.most_common(5)]

        return {
            'liked': top_liked if top_liked else ['None'],
            'disliked': top_disliked if top_disliked else ['None']
        }
    
    def analyze_feedback(self, text):
        """Complete feedback analysis with sentiment and summary generation"""
        sentiment_result = self.analyze_sentiment(text)
        summary = self.generate_summary(text)
        
        return {
            'sentiment_analysis': sentiment_result,
            'summary': summary
        }

def main():
    analyzer = CustomerFeedbackAnalyzer()
    
    feedback = input("Please enter the customer feedback: ")
    
    result = analyzer.analyze_feedback(feedback)
    
    print(f"\nSentiment: {result['sentiment_analysis']['sentiment']} (Score: {result['sentiment_analysis']['score']:.2f})")
    print("\nSummary of Customer Feedback:")
    print("Liked:", ", ".join(result['summary']['liked']))
    print("Disliked:", ", ".join(result['summary']['disliked']))

if __name__ == "__main__":
    main()
