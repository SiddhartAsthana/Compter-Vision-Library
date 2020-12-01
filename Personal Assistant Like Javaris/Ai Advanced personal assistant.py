#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import JarvisAI
import re
import pprint
import random

obj = JarvisAI.JarvisAssistant()


def text_to_speech(text):
    obj.text2speech(text)


while True:
    res = obj.mic_input()

    if re.search('weather|temperature', res):
        city = res.split(' ')[-1]
        weather_res = obj.weather(city=city)
        print(weather_res)
        text_to_speech(weather_res)

    elif re.search('news', res):
        news_res = obj.news()
        pprint.pprint(news_res)
        text_to_speech(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
        text_to_speech(news_res[0])
        text_to_speech(news_res[1])

    elif re.search('tell me about', res):
        topic = res.split(' ')[-1]
        wiki_res = obj.tell_me(topic)
        print(wiki_res)
        text_to_speech(wiki_res)

    elif re.search('date', res):
        date = obj.tell_me_date()
        print(date)
        print(t2s(date))

    elif re.search('time', res):
        time = obj.tell_me_time()
        print(time)
        text_to_speech(time)

    elif re.search('open', res):
        domain = res.split(' ')[-1]
        open_result = obj.website_opener(domain)
        print(open_result)

    elif re.search('launch', res):
        dict_app = {
            'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
            'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe'
        }

        app = res.split(' ', 1)[1]
        path = dict_app.get(app)
        if path is None:
            text_to_speech('Application path not found')
            print('Application path not found')
        else:
            text_to_speech('Launching: ' + app)
            obj.launch_any_app(path_of_app=path)

    elif re.search('hello', res):
        print('Hi')
        text_to_speech('Hi')

    elif re.search('how are you', res):
        li = ['good', 'fine', 'great']
        response = random.choice(li)
        print(f"I am {response}")
        text_to_speech(f"I am {response}")

    elif re.search('your name|who are you', res):
        print("My name is Jarvis, I am your personal assistant")
        text_to_speech("My name is Jarvis, I am your personal assistant")

    elif re.search('what can you do', res):
        li_commands = {
            "open websites": "Example: 'open youtube.com",
            "time": "Example: 'what time it is?'",
            "date": "Example: 'what date it is?'",
            "launch applications": "Example: 'launch chrome'",
            "tell me": "Example: 'tell me about India'",
            "weather": "Example: 'what weather/temperature in Mumbai?'",
            "news": "Example: 'news for today' ",
        }
        ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
        I can open websites for you, launch application and more. See the list of commands-"""
        print(ans)
        pprint.pprint(li_commands)
        text_to_speech(ans)
        
    else:
        print("assign me some task....")
        text_to_speech("assign me some task....")

