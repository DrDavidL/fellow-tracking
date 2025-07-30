# Clinical Informatics Fellow Log & Analyzer

This Streamlit application allows Clinical Informatics Fellows to log their experiences during rotations and receive AI-powered recommendations for next steps to ensure comprehensive coverage of clinical informatics topics.

## Features

*   **Experience Logging**: Easily record daily or weekly clinical informatics experiences.
*   **AI-Powered Analysis**: Utilizes GPT-4o to analyze logged experiences and identify gaps in coverage.
*   **Actionable Recommendations**: Provides tailored suggestions for future experiences or learning opportunities to cover all key clinical informatics domains.
*   **Persistent Storage**: Logs are saved to a `log.csv` file, ensuring data is retained across sessions.

## Setup

Follow these steps to set up and run the application locally.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)
*   A virtual environment (recommended)
*   An OpenAI API Key

### Installation

1.  **Clone the repository (if applicable) or navigate to the project directory:**
    ```bash
    cd fellow-tracking
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On macOS/Linux
    source venv/bin/activate
    # On Windows
    .\venv\Scripts\activate
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r streamlit_app/requirements.txt
    ```

### OpenAI API Key Setup

The application requires an OpenAI API key to analyze the logs using GPT-4o.

1.  **Create a `.env` file** in the root directory of this project (the same directory as `README.md`).
2.  **Add your OpenAI API key** to this `.env` file in the following format:
    ```
    OPENAI_API_KEY="your_openai_api_key_here"
    ```
    Replace `"your_openai_api_key_here"` with your actual OpenAI API key.

## Usage

Once the setup is complete, you can run the Streamlit application:

1.  **Ensure your virtual environment is activated.**
2.  **Navigate to the root directory of the project** (where `README.md` is located).
3.  **Run the Streamlit app:**
    ```bash
    streamlit run streamlit_app/app.py
    ```

    This command will open the application in your default web browser. If it doesn't open automatically, Streamlit will provide a local URL (e.g., `http://localhost:8501`) that you can copy and paste into your browser.

## Project Structure

*   `README.md`: This file.
*   `.env`: Stores your OpenAI API key (not committed to version control).
*   `streamlit_app/`:
    *   `app.py`: The main Streamlit application code.
    *   `requirements.txt`: Lists all Python dependencies required by the application.
    *   `log.csv`: Stores the logged clinical informatics experiences. This file is created and managed by the application.
