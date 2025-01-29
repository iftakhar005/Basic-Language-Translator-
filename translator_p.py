from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


root = Tk()
root.geometry('850x550')
root.resizable(False, False)
root.title('Language Translator')


root.configure(bg="#1E1E2F")


style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TLabel",
    font="Helvetica 14",
    background="#1E1E2F", 
    foreground="#F0F0F0",  
)
style.configure(
    "TButton",
    font="Helvetica 12 bold",
    padding=10,
    background="#4CAF50", 
    foreground="white",
)
style.map(
    "TButton",
    background=[("active", "#45A049")],
    foreground=[("active", "white")],
)
style.configure(
    "TEntry",
    font="Helvetica 12",
    padding=5,
    relief="flat",
)
style.configure(
    "TCombobox",
    font="Helvetica 12",
    padding=5,
)

title_label = Label(
    root,
    text="Language Translator",
    font="Helvetica 24 bold",
    fg="#4CAF50", 
    bg="#1E1E2F",
)
title_label.pack(pady=20)

input_frame = Frame(root, bg="#292940", bd=2, relief="groove")
input_frame.pack(pady=10, padx=20, fill=X)


input_label = ttk.Label(input_frame, text="Enter Text:")
input_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

input_text = ttk.Entry(input_frame, width=60)
input_text.grid(row=0, column=1, padx=10, pady=10)


lang_label = ttk.Label(input_frame, text="Select Language:")
lang_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

language_list = list(LANGUAGES.values())
dst_lang = ttk.Combobox(input_frame, values=language_list, width=58, state="readonly")
dst_lang.grid(row=1, column=1, padx=10, pady=10)
dst_lang.set("Choose Language")


output_frame = Frame(root, bg="#292940", bd=2, relief="groove")
output_frame.pack(pady=10, padx=20, fill=X)

output_label = ttk.Label(output_frame, text="Translated Text:")
output_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

output_text = Text(
    output_frame,
    font="Helvetica 12",
    height=8,
    width=60,
    wrap=WORD,
    relief="flat",
    bg="#1E1E2F",
    fg="#F0F0F0",
    bd=1,
    highlightbackground="#4CAF50",
    highlightthickness=1,
)
output_text.grid(row=0, column=1, padx=10, pady=10)


def Translate():
    translator = Translator()
    try:
        translated = translator.translate(text=input_text.get(), dest=dst_lang.get())
        output_text.delete(1.0, END)
        output_text.insert(END, translated.text)
    except Exception as e:
        output_text.delete(1.0, END)
        output_text.insert(END, f"Error: {str(e)}")


trans_bttn = ttk.Button(
    root,
    text="Translate",
    command=Translate,
)
trans_bttn.pack(pady=20)


footer_label = Label(
    root,
    text="Powered by Google Translate",
    font="Helvetica 10 italic",
    bg="#1E1E2F",
    fg="#888888",
)
footer_label.pack(side=BOTTOM, pady=10)


root.mainloop()
