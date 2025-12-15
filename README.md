# Echoes Of Emotions

## Overview
Echoes Of Emotions is a Python application that uses Natural Language Processing (NLP) to analyze customer feedback. It performs sentiment analysis and extracts key phrases to summarize what customers liked and disliked. The project includes a Streamlit web interface for an interactive and visually appealing user experience.

## Features
- **Sentiment Analysis**: Uses NLTK's VADER to classify feedback as positive, negative, or neutral with detailed sentiment scores.
- **Phrase Extraction**: Identifies and summarizes key noun phrases for liked and disliked aspects using NLTK's chunking and frequency analysis.
- **Streamlit Interface**: Provides a user-friendly web interface (`streamlit_app.py`) with emoji-based sentiment visualization and formatted summaries.

## Requirements
- Python 3.6 or higher
- Virtualenv (recommended for virtual environment setup)
- Required Python packages:
  - `nltk` (`pip install nltk`)
  - `streamlit` (`pip install streamlit`)

## Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd echoes-of-emotions
```

### Step 2: Create a Virtual Environment
1. Create a virtual environment to isolate dependencies:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install nltk streamlit
```

### Step 4: Download NLTK Resources
The application automatically downloads required NLTK resources (`vader_lexicon`, `punkt`, `stopwords`, `averaged_perceptron_tagger`) on first run. Alternatively, you can download them manually:
```python
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
```

## Usage

### Running the Streamlit App
1. Ensure the virtual environment is activated.
2. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Open your web browser and navigate to the URL provided by Streamlit (typically `http://localhost:8501`).
4. Enter customer feedback in the text area, click the "Analyze" button, and view the sentiment analysis (with emoji and color-coded output) and summary of liked/disliked aspects.

### Example
**Input Feedback:**
```
The product quality is excellent, and the customer service was very helpful. However, the delivery was slow and packaging was damaged.
```

**Output in Streamlit Interface:**
- **Sentiment**: Neutral 😐 (Score: 0.12)
- **Detailed Scores**:
  - Negative: 0.123
  - Neutral: 0.456
  - Positive: 0.421
  - Compound: 0.123
- **Summary**:
  - **👍 Liked**: product quality, customer service
  - **👎 Disliked**: delivery, packaging

## Project Structure
- `nlp.py`: Contains the `CustomerFeedbackAnalyzer` class for sentiment analysis and phrase extraction.
- `streamlit_app.py`: Streamlit web interface for user interaction, displaying sentiment results and summaries.
- `venv/`: Virtual environment directory (created after setup).
- `README.md`: This file, providing project documentation.

## Dependencies
- **NLTK**: For sentiment analysis, tokenization, stopword removal, part-of-speech tagging, and chunking.
- **Streamlit**: For building the interactive web interface.

## Limitations
- Requires internet access on first run to download NLTK resources.
- Phrase extraction relies on simple noun phrase chunking, which may miss nuanced or complex feedback.
- VADER sentiment analysis may not fully capture sarcasm or context-specific sentiments.

## Future Improvements
- Enhance phrase extraction with advanced NLP techniques (e.g., dependency parsing).
- Add support for batch processing of multiple feedback entries.
- Improve the Streamlit interface with additional visualizations (e.g., sentiment trend charts).
