import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    
    audio=r.listen(source)
text=r.recognize_google(audio)

if text.lower() == "hello":
    print("Hello! Nice to meet you.")

elif text.lower() == "bye":
    print("Goodbye!")

else:
    print("I don't understand.")

try:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("You said: " + text)
except sr.UnknownValueError:
    print("I could not understand the audio.")
except sr.RequestError:
    print("Could not request results from Google Speech Recognition service.")