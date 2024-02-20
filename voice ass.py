import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import sys
#Text To Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()  

#now convert audio to text

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return text

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir") 
    else:
        speak("good evening sir ")
    speak("I am virtual assistent jarvis tell me how may i help you ")

#for main function                               
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        if "wikipedia" in query:
            speak("searching details....Wait")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
            
        elif 'open github' in query:
            webbrowser.open("https://www.github.com/harishqw")
            speak("opening github")  
              
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 

        elif 'open insta' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")
            
        elif 'music' in query or "play music" in query:
             webbrowser.open("https://www.youtube.com/watch?v=euCqAq6BRa4&list=RDeuCqAq6BRa4&start_radio=1")
             speak("playing music wait for a second")
             
        elif 'good bye' in query or 'bye' in query:
            speak("good bye")
            exit()
            
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')
            
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['I am fine!','I am nice and full of energy','i am nice!']
            ans_q = random.choice(stMsgs)
            speak(ans_q)

        elif 'good' in query or 'nice' in query:
            print("oh thankyou sir")
            speak("oh thankyou sir")
                
        elif 'who make you' in query or 'who created you' in query or 'who develop you' in query:
            ans_m = " For your information Harish Gupta Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
            
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Friday an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
            
        elif "who i am" in query or "about me" in query or "my details" in query:
            about = "You are Harish and you are a student of Nataji Subhash University and your cource is BCA in first semester and you insta id is Harish_Gupta and your youtube chanel is You'r Tech"
            print(about)
            speak(about)
            
        elif "hello" in query or "hello Friday" in query:
            hel = "Hello Sir ! How May i Help you.."
            print(hel)
            speak(hel)
            
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Friday"  
            print(na_me)
            speak(na_me)
            
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")

        elif query == 'none':
            continue

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()

        elif 'search' in query or 'find' in query:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="
            res_g = 'okay sir i search from internet please wait for a second'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)
            
        elif 'show' in query or 'locate' in query or 'direction' in query:
            temp = query.replace(' ','+')
            g_url="https://www.google.co.in/maps/@23.9559168,84.6823205,9.14z?q="
            res_g = 'okay sir i search from internet please wait for a second'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)
        else:    
            res_g = "sorry sir i can't understand"
            print(res_g)
            speak(res_g)