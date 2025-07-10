import pyttsx3 as py#modules
import datetime as dt 
import speech_recognition as sr 
import wikipedia as wp
import webbrowser as wb      
import os
import random as rn


engin = py.init('sapi5') 
voice = engin.getProperty('voices')
engin.setProperty('voice',voice[0].id)#0 male,1 female voice


ToDoList=[]


def speak(audio):#it is the voice of the system
    
    engin.say(audio)
    engin.runAndWait()
    
def takeInput():#it takes the input form the user via microphone and returns outpit as string
    
    v=sr.Recognizer( )
    with sr.Microphone()as source:
        print("Listening.....")
        v.pause_threshold = 1
        v.energy_threshold=250
        aud= v.listen(source)

    try:
        print("thinking....")
        query = v.recognize_google(aud,language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print(e)
        print("Didn't got you on that one \ncould  you repeat")
        return "None"
    return query



if __name__ =="__main__":#main body
    while True:#cotinously takes input from user
        query = takeInput().lower()
        # if 'jarvis' in query:#checks if jarvis is said to continue the program
        # query=query.replace("jarvis","")
        print(query)

        #logic for code
        if 'wikipedia' in query:#search in wikipedia
            speak('Searching')
            lines=3
            try:
                query = query.replace("wikipedia", "")
                results = wp.summary(query, sentences=lines)
            except:
                speak("sorry i couldn't find anything, you can try any other keyword to search for")
            speak("here are the results")
            speak(results)
            speak ("do you want to listen more")
            query1=takeInput().lower()
            if "yes" in query1:
                    lines+=3
                    results=wp.summary(query,sentences=lines)
                    speak(results)
            elif "no" in query1:
                    speak("OK")
            else:
                    speak ("could you repeat")
            

        elif 'hello'in query:#greetings
            greetings=["Hello there, What can i help you with" , "Hey what's up, wan't some help with something?" , "what can i do for you today"]
            speak (rn.choice(greetings))
            
        elif 'open' in query:#open
            if 'youtube' in query:#youtube
                speak("opening youtube..")
                wb.open('youtube.com')
            if 'aniwatch' in query:#aniwatch
                speak("opening aniwatch..")
                wb.open('aniwatch.to')
                
        elif 'time' in query:#tells time
            time= dt.datetime.now().strftime("%H:%M:%S")
            speak(time)

        elif 'date' in query:
            date=dt.date.today().strftime("%m/%d/%Y")
            speak(date)

        elif 'add to list' in query:
            speak("what do you wan't to add")
            query=takeInput().lower()
            if query in ToDoList:
                ToDoList.append(query)
                speak("{query} has been added" )
            else:
                speak("I did't heard you this time could you start over")

        elif 'what is in list' in query:
            speak(ToDoList)
            print(ToDoList)
        
        elif 'remove from list' in query:
            speak("what you wan't to remove")
            query=takeInput().lower()
            if query in ToDoList:
                ToDoList.remove(query)
                speak("{query} has been removed" )

            else:
                speak("{query} is not in list")

        elif 'spotify' in query:#open spotify
            path="C:\\Users\\ADMIN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
            os.startfile(path)
        elif 'stop' in query:
            engin.stop()
            exit    