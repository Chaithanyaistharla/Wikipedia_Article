import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk

# Function to open a random article
def open_random_article():
    a = "https://en.wikipedia.org/wiki/Special:Random"
    u = requests.get(a)
    soup = BeautifulSoup(u.content, 'html.parser')
    title = soup.find(class_="firstHeading").text

    question_label.config(text=title + "\nDo you want to view it?")

    yes_button.config(state=tk.NORMAL)
    no_button.config(state=tk.NORMAL)

# Function to open the selected article in a web browser
def open_article():
    title = question_label.cget("text").split("\n")[0]
    url = 'https://en.wikipedia.org/wiki/%s' % title
    webbrowser.open(url)

# Function to skip to another random article
def skip_article():
    question_label.config(text="Ok. Trying again!")
    yes_button.config(state=tk.DISABLED)
    no_button.config(state=tk.DISABLED)
    open_random_article()

# Function to quit the application
def quit_app():
    root.destroy()

# Configure styles
BG_COLOR = "#f7f7f7"
BUTTON_YES_COLOR = "#00cc00"
BUTTON_NO_COLOR = "#ff0000"
BUTTON_EXIT_COLOR = "#999999"
FONT = ("Arial", 12)

# Create the main window
root = tk.Tk()
root.title("Random Wikipedia Article")
root.geometry("400x250")
root.configure(bg=BG_COLOR)

# Create and configure the question label
question_label = tk.Label(root, text="", font=FONT, bg=BG_COLOR, fg="black")
question_label.pack(pady=20)

# Create a frame to hold the buttons
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack()

# Create and configure the "Yes" button
yes_button = tk.Button(button_frame, text="Yes", command=open_article, font=FONT, bg=BUTTON_YES_COLOR, fg="black")
yes_button.pack(side=tk.LEFT, padx=5, pady=10)

# Create and configure the "No" button
no_button = tk.Button(button_frame, text="No", command=skip_article, font=FONT, bg=BUTTON_NO_COLOR, fg="black")
no_button.pack(side=tk.LEFT, padx=5, pady=10)

# Create and configure the "Exit" button
exit_button = tk.Button(root, text="Exit", command=quit_app, font=FONT, bg=BUTTON_EXIT_COLOR, fg="black")
exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Open the first random article
open_random_article()

# Run the application
root.protocol("WM_DELETE_WINDOW", quit_app)
root.mainloop()
