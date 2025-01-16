# genai-streamlit-app

<img src="https://drive.google.com/uc?export=view&id=1O_nwXF1buw8YkaE24QlBiPBCciYb8nmW" alt="Image 1" width="500px" height="500px" style="display:inline-block;">



A Streamlit app integrating LangChain with Google Generative AI and LangSmith. This app uses `ChatGoogleGenerativeAI` to provide AI-generated responses based on user queries and LangSmith for tracking application interactions.

## 🛠️ Technologies Used

- **LangChain**: Manages AI prompt workflows and connects to Google Generative AI.
- **Google Generative AI (Gemini Pro)**: Powers the AI responses.
- **LangSmith**: Used for tracing and monitoring AI workflows.
- **Streamlit**: Provides the web interface.
- **dotenv**: Manages environment variables.

## ⚙️ How It Works

1. Users enter a query into the Streamlit app.
2. The app generates a response using **Google Generative AI**.
3. The app traces the workflow using **LangSmith** to ensure effective monitoring and debugging.
4. The result is displayed on the app's interface in real-time.

## Features

- **AI-Powered Responses**: Leverages Google Generative AI through LangChain to generate responses based on user input.
- **Tracking**: Uses LangSmith for monitoring and tracking application interactions.
- **Secure Configuration**: Configured for secure API access with environment variables.

## Requirements

- Python 3.8 or higher
- Streamlit
- LangChain
- LangSmith
- `python-dotenv`

## Installation

1. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    ```
2. **Activate the virtual environment**:
      - On Windows:
        ```bash
        .venv\Scripts\activate
        ```
      - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your API keys:
    ```
    GOOGLE_API_KEY=your_google_api_key
    LANGCHAIN_API_KEY=your_langchain_api_key
    ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
