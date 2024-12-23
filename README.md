# Simple Generative Pre-trained Transformer using API

This project demonstrates the creation of a simple Generative Pre-trained Transformer (GPT) application using Cohere's foundation models, Streamlit for an interactive web interface, and Python. The application accepts user input, processes it via Cohere's API, and generates relevant text outputs.

## Features
- Leverages Cohere's powerful language models for text generation.
- User-friendly interface built with Streamlit.
- Environment variables securely managed using `dotenv`.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- `pip` (Python package installer)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/shivampb/ChatGPT
   cd ChatGPT
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install streamlit cohere dotenv
   ```

4. Get your API key from the [Cohere website](https://cohere.ai/):
   - Sign up or log in.
   - Navigate to the API section to obtain your API key.

5. Create a `.env` file in the project directory to securely store your API key:
   ```
   COHERE_API_KEY=your_api_key_here
   ```

## Usage
1. Run the application using Streamlit:
   ```bash
   streamlit run frontend.py
   ```

2. Open the provided local URL in your browser (usually `http://localhost:8501`).

3. Input your text prompt into the application, and the GPT model will generate relevant outputs.

## Example Workflow
1. User enters a text prompt into the Streamlit interface.
2. The application sends the prompt to Cohere's API using their foundation models.
3. The API processes the input and returns generated text.
4. The generated text is displayed in the Streamlit app.

## File Structure
```
.
├── frontend.py     # Frontend application file
├── backend.py      # Backend logic file
├── requirements.txt # Dependency list
├── .env            # Environment variables file (not included in version control)
└── README.md       # Project documentation
```

## Future Enhancements
- Add additional text processing features like summarization or sentiment analysis.
- Deploy the application to the cloud using platforms like Heroku or AWS.
- Support multiple foundation models.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

---

**Happy Coding!** 🎉
