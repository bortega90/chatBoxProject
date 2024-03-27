import tkinter as tk
from tkinter import scrolledtext
import openai

# Set the OpenAI API key
openai.api_key = "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"

# encapsulate to make mod, easy to read and maintain
class SmartyBotApp:
    def __init__(self):
        #initalizing tkinter window
        self.root = tk.Tk()
        self.root.title("SmartyBot")
        self.root.configure(background='pink')

        #created scroll bar for chat messages
        self.chat_box = scrolledtext.ScrolledText(self.root, width=40, height=20)
        self.chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        #created entry field for user input
        self.entry = tk.Entry(self.root, width=30, fg="grey")
        self.entry.grid(row=1, column=0, padx=10, pady=(0, 10), columnspan=2)
        self.entry.insert(0, "write message here")
        self.entry.bind("<FocusIn>", self.clear_entry)
        self.entry.bind("<Return>", self.send_message)

    def run(self):
        #start loop to keep window open
        self.root.mainloop()

    def chat_with_gpt(self, prompt):
        #using openai api for response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()

    def send_message(self, event=None):
        #function to handle sending msg
        user_input = self.entry.get()
        #trigger words to quit window
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
        #clears entry field once user types
        if self.entry.get() == "write message here":
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

if __name__ == "__main__":
    #create an object of SmartyBotApp class and run program
    app = SmartyBotApp()
    app.run()