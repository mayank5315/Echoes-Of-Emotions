import streamlit as st
from nlp import CustomerFeedbackAnalyzer

def main():
    st.title("Echoes of Emotion - Sentiment Analysis")
    st.write("Enter customer feedback below to analyze sentiment and generate a summary of likes and dislikes.")

    analyzer = CustomerFeedbackAnalyzer()

    feedback = st.text_area("Customer Feedback", height=200)

    if st.button("Analyze"):
        if not feedback.strip():
            st.warning("Please enter some feedback text to analyze.")
        else:
            with st.spinner("Analyzing feedback..."):
                result = analyzer.analyze_feedback(feedback)
                sentiment = result['sentiment_analysis']['sentiment']
                score = result['sentiment_analysis']['score']
                details = result['sentiment_analysis']['details']
                summary = result['summary']

                st.subheader("Sentiment Analysis Result")

                sentiment_emoji = {
                    'positive': '😊',
                    'negative': '😞',
                    'neutral': '😐'
                }.get(sentiment.lower(), '')

                sentiment_color = {
                    'positive': 'green',
                    'negative': 'red',
                    'neutral': 'gray'
                }.get(sentiment.lower(), 'black')

                st.markdown(f"Sentiment: <span style='color:{sentiment_color}; font-weight:bold; font-size:24px'>{sentiment.capitalize()} {sentiment_emoji}</span>", unsafe_allow_html=True)
                st.markdown(f"**Score:** <span style='font-size:18px'>{score:.2f}</span>", unsafe_allow_html=True)

                st.markdown("### Detailed Scores")
                st.markdown(f"- Negative: {details.get('neg', 0):.3f}")
                st.markdown(f"- Neutral: {details.get('neu', 0):.3f}")
                st.markdown(f"- Positive: {details.get('pos', 0):.3f}")
                st.markdown(f"- Compound: {details.get('compound', 0):.3f}")

                st.markdown("### Summary of Customer Feedback")

                liked = summary.get("liked", [])
                disliked = summary.get("disliked", [])

                if liked and liked != ['None']:
                    st.markdown("**👍 Liked:**")
                    for item in liked:
                        st.markdown(f"- {item}")
                else:
                    st.markdown("**👍 Liked:** None")

                if disliked and disliked != ['None']:
                    st.markdown("**👎 Disliked:**")
                    for item in disliked:
                        st.markdown(f"- {item}")
                else:
                    st.markdown("**👎 Disliked:** None")

if __name__ == "__main__":
    main()
