import openai
import threading
import keyboard
import io
import base64
from PIL import ImageGrab
import pyttsx3
import speech_recognition as sr
import os


# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Initialize conversation history
conversation_history = []

# Flag to indicate if an image has been captured
image_captured = False
captured_image_base64 = ''

def listen_for_f9():
    global image_captured, captured_image_base64
    while True:
        keyboard.wait('f9')
        print("\nF9 pressed. Capturing screenshot...")
        # Capture the screenshot
        screenshot = ImageGrab.grab()

        # Save the screenshot to a bytes buffer
        img_buffer = io.BytesIO()
        screenshot.save(img_buffer, format='PNG')
        img_buffer.seek(0)

        # Encode the image in base64
        captured_image_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
        image_captured = True
        print("Screenshot captured and will be included in the next message.")

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("\nListening... (Speak now)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Processing your speech...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def main():
    global image_captured, captured_image_base64

    # Start the F9 listener thread
    f9_thread = threading.Thread(target=listen_for_f9, daemon=True)
    f9_thread.start()

    print("You can start speaking to the assistant. Say 'exit' to quit.")
    print("Press F9 at any time to capture a screenshot for the assistant to analyze.")

    while True:
        # Get user voice input
        user_input = recognize_speech()
        if user_input is None:
            continue  # Skip if speech was not recognized

        if user_input.lower() in ['exit', 'quit', 'stop']:
            print("Exiting the chat.")
            break

        # Prepare the message
        message = {"role": "user", "content": user_input}

        # If an image was captured, include it in the message
        if image_captured:
            message["content"] = [
                {"type": "text", "text": user_input},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{captured_image_base64}",
                        "detail": "low"
                    },
                },
            ]
            # Reset the flag and image
            image_captured = False
            captured_image_base64 = ''

        # Add the user's message to the conversation history
        conversation_history.append(message)

        # Send the conversation history to the assistant
        try:
            print("Assistant is typing...")
            response = openai.ChatCompletion.create(
                model="gpt-4o",  # Replace with the correct model name
                messages=conversation_history,
                max_tokens=500,
            )
            # Get the assistant's reply
            assistant_message = response.choices[0].message
            content = assistant_message['content']
            print(f"\nAssistant: {content}")

            # Add assistant's reply to the conversation history
            conversation_history.append(assistant_message)

            # Text-to-Speech Conversion using pyttsx3
            print("Assistant is speaking... (Note: The voice is AI-generated)")
            engine.say(content)
            engine.runAndWait()

        except Exception as ex:
            print(f"An error occurred: {ex}")

if __name__ == "__main__":
    main()
