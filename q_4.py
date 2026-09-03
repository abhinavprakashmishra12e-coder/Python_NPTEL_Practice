import speech_recognition as sr

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)

    if text.lower() == "hello":
        print("Hello! Nice to meet you.")
    elif text.lower() == "bye":
        print("Goodbye!")
    else:
        print("I don't understand.")

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results; {e}")

    
