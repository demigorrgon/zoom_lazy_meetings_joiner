# zoom_lazy_meetings_joiner
Zoom meetings scheduler for people that have to be there but don't want to

Opens up a link in your browser with built-in package: ```webbrowser``` straight to your zoom desktop client

NO PYAUTOGUI! You can use some of it if you want to automate desktop app behaviour

Basic usage:
 - make somename.csv file
 - specify it in ```FILENAME``` varible in ```scheduler.py```
 - specify rows with three columns: ```name,link,date```
 - dates accepted: ```monday 12:10```, ```tuesday 8:30```, etc.
 - ```pip install -r requirements.txt``` or whatever package manager you're using
 - ```python scheduler.py```


 TODO: user friendly file input

 TODO: tests

 TODO: add MS teams opening