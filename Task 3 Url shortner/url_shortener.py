import tkinter as tk
import requests
from tkinter import messagebox

api_key = "146a316efdmshe042b07c6392d43p1a84b8jsnd7aee4adc615"
api_host = "url-shortener23.p.rapidapi.com"
url = "https://url-shortener23.p.rapidapi.com/shorten"

def shorten_url():
    root.clipboard_clear()
    url_input = entry_url.get()
    
    
    data = {"url": url_input}
    headers = {"X-RapidAPI-Key": api_key, "X-RapidAPI-Host": api_host}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        short_url = response.json()["short_url"]
        label_result.config(text=f"Shortened URL: {short_url}")
        root.clipboard_append(short_url)
        messagebox.showinfo(message="Copied to Clipboard")
    except Exception as e:
        label_result.config(text=f"An error occurred: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("URL Shortener")

label_url = tk.Label(root, text="Enter URL:")
label_url.pack(pady=10)

entry_url = tk.Entry(root, width=40)
entry_url.pack(pady=10)

btn_shorten = tk.Button(root, text="Shorten URL", command=shorten_url)
btn_shorten.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
