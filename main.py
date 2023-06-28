import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk

def open_random_article():
    a = "https://en.wikipedia.org/wiki/Special:Random"
    u = requests.get(a)
    soup = BeautifulSoup(u.content, 'html.parser')
    title = soup.find(class_="firstHeading").text

    question_label.config(text=title + "\nDo you want to view it?")

    yes_button.config(state=tk.NORMAL)
    no_button.config(state=tk.NORMAL)

def open_article():
    title = question_label.cget("text").split("\n")[0]
    url = 'https://en.wikipedia.org/wiki/%s' % title
    webbrowser.open(url)

def skip_article():
    question_label.config(text="Ok. Trying again!")
    yes_button.config(state=tk.DISABLED)
    no_button.config(state=tk.DISABLED)
    open_random_article()

def quit_app():
    root.destroy()

root = tk.Tk()
root.title("Random Wikipedia Article")
root.geometry("400x250")

question_label = tk.Label(root, text="")
question_label.pack(pady=20)

yes_button = tk.Button(root, text="Yes", command=open_article)
yes_button.pack(pady=10)

no_button = tk.Button(root, text="No", command=skip_article)
no_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=quit_app)
exit_button.pack(pady=10)

open_random_article()

root.protocol("WM_DELETE_WINDOW", quit_app)
root.mainloop()
