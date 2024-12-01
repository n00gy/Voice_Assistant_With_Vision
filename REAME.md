Screenshot and Voice Assistant
Features

- **Voice Interaction**: Speak to the assistant to ask questions or give commands.
- **Screenshot Capture**: Press `F9` to capture a screenshot, which can be included in conversations for analysis.
- **Text-to-Speech**: The assistant reads responses aloud using a Text-to-Speech engine.

Installation

### Prerequisites
- Python 3.8 or later installed on your system.
- An OpenAI API key. Sign up and get your API key from OpenAI.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/n00gy/Voice_Assistant_With_Vision.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Voice_Assistant_With_Vision
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"  # On Windows: set OPENAI_API_KEY=your_openai_api_key
   ```

Usage

Run the script:
```bash
python main.py
```

### Interacting with the Assistant
1. Speak into the microphone when prompted.
2. Press `F9` to capture a screenshot. The assistant will analyze the screenshot and include it in the conversation.
3. Say "exit" or "quit" to stop the program.

Dependencies

The project relies on the following Python libraries:
- `openai` – For AI-generated responses.
- `pyttsx3` – For Text-to-Speech conversion.
- `SpeechRecognition` – For capturing and processing voice input.
- `keyboard` – For detecting keypresses (e.g., `F9`).
- `Pillow` – For capturing and handling screenshots.

Contributing

Contributions are welcome! Feel free to submit issues or pull requests for improvements.

License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute it as per the license terms.

Acknowledgments

- [OpenAI](https://openai.com/) for the powerful API.
- The Python community for the fantastic libraries used in this project.
