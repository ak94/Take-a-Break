import webbrowser
import time

#your fav song url
my_fav_url = "https://google.co.in"

#no of times you want to take a break
no_of_breaks = 3

#after how much time you want to take a break
seconds_for_break = 2 #2 hrs


def take_a_break(no_break,break_time,my_fav_url):
    i=0
    while i< no_break:
        time.sleep(break_time)
        webbrowser.open(my_fav_url)
        i=i+1

take_a_break(no_of_breaks,seconds_for_break,my_fav_url)
    
