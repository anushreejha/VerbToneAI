# VerbTone AI 

VerbTone is an interactive AI assistant designed to perform various tasks such as voice-based interaction, providing real-time weather and news updates, managing time and dates, writing emails, and now enhanced with features like emotion detection and advanced NLP capabilities.

## **Features**

### Core Functionalities:
- **Wake-Word Detection**: Activates only when triggered by phrases like "Hey VerbTone," "Hello," or similar greetings.
- **Weather Updates**: Provides real-time weather information powered by the OpenWeatherMap API.
- **News Headlines**: Fetches the latest top news headlines using the NewsAPI.
- **Intent Classification**: Advanced NLP using Hugging Face’s GPT-2 for understanding and processing user commands accurately.
- **Speech-to-Text & Text-to-Speech**:
  - Converts speech to text for user commands.
  - Responds with voice output.
- **Basic Utility Commands**:
  - Tell the time, date and day.
  - Provide greetings.
  - Perform Google searches.
  - Write and send emails.
  - Provide weather predictions.
  - Read out news headlines.

### Advanced Features:
- **Emotion Detection** (New):
  - Detects user emotions through facial expressions or speech tone.
  - Customizes responses based on the detected emotional state (e.g., happy, angry, sad).
- **Session Continuity** (New):
  - Engages in continuous interaction without requiring repeated wake-word usage.
  - Automatically resets to listening for the wake word after 15 seconds of inactivity.
- **Natural Language Processing (NLP)**:
  - Leverages Hugging Face’s GPT-2 for query understanding and intent classification, ensuring accurate and context-aware responses.

---

## **Installation Instructions**

### Prerequisites:
1. Python 3.8 or higher.
2. To see the required libraries, refer to `requirements.txt`.

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/VerbToneAI.git
   cd VerbToneAI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Obtain API key for weather data:
   - Get an API key for [OpenWeatherMap](https://openweathermap.org/api).

4. Run the application:
   ```bash
   python main.py
   ```

---

## **Usage**

1. Start the assistant by saying a greeting like "Hey VerbTone" or "Hello."
2. Interact with the assistant using commands such as:
   - "What's the weather like today?"
   - "Tell me the latest news."
   - "What time is it?"
   - "Can you write an email for me?"

---

## **Future Enhancements**
- Add support for multi-language interactions.
- Enhance emotion detection to include more nuanced emotional states.
- Expand integration with other APIs for advanced productivity tools.
- Introduce conversational memory for better context retention.

