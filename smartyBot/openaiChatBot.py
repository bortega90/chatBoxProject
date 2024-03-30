import os
import tkinter as tk
from tkinter import scrolledtext
import openai

# Get the OpenAI API key from environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')

class SmartyBotApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SmartyBot")
        self.root.configure(background='pink')

        self.chat_box = scrolledtext.ScrolledText(self.root, width=40, height=20)
        self.chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.entry = tk.Entry(self.root, width=30, fg="grey")
        self.entry.grid(row=1, column=0, padx=10, pady=(0, 10), columnspan=2)
        self.entry.insert(0, "write message here")
        self.entry.bind("<FocusIn>", self.clear_entry)
        self.entry.bind("<Return>", self.send_message)

    def run(self):
        self.root.mainloop()

    def chat_with_gpt(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()

    def send_message(self, event=None):
        user_input = self.entry.get()
        if user_input.lower() in ["quit", "exit", "bye", "adios"]:
            self.root.destroy()
            return
        response = self.chat_with_gpt(user_input)
        self.chat_box.insert(tk.END, f"You: {user_input}\n")
        self.chat_box.insert(tk.END, f"SmartyBot: {response}\n\n")
        self.entry.delete(0, tk.END)
        if user_input == "write message here":
            self.entry.config(fg="grey")

    def clear_entry(self, event=None):
        if self.entry.get() == "write message here":
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

if __name__ == "__main__":
    app = SmartyBotApp()
    app.run()