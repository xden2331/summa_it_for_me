from tkinter import *
from translator import Translator
from summarizer import Summarizer

translator = Translator()
summarizer = Summarizer()

root = Tk()
root.geometry("")
root.title("太长不看")

l = Label(text="请输入全文")
inputtxt = Text(root, bd=2, relief="ridge")
inputtxt.config(font=("STHeiti", 12, "bold"), spacing2=5)

Output = Text(root, bd=2, relief="ridge")
Output.config(font=("Helvetica Neue", 12), spacing1=1)


def Take_input(text_area, slider=None, dest_lang=None):
    input_text = text_area.get("1.0", "end-1c")
    translated_text = translator.translate(input_text)
    ratio = slider.get() / 100.0 if slider is not None else 0.2
    dest = dest_lang.get() if dest_lang is not None else 'zh-cn'
    summarized_text = summarizer.summarize(
        translated_text, ratio=ratio, dest=dest)
    Output.delete("1.0", END)
    Output.insert(END, summarized_text)


# Set up slider
slider_frame = Frame(root)
Label(slider_frame, text="总结占原文长度比例").grid(row=0, column=0)
slider = Scale(slider_frame, from_=0, to=100, orient=HORIZONTAL)
slider.set(20)
slider.grid(row=0, column=1)

Label(slider_frame, text="总结语言").grid(row=0, column=3)
dest_lang = StringVar(slider_frame)
dest_lang.set("zh-cn")
dest_langs = OptionMenu(slider_frame, dest_lang, "zh-cn", "en")
dest_langs.grid(row=0, column=4)

Display = Button(root, height=2, width=10, text="给我总结一下",
                 command=lambda: Take_input(inputtxt, slider=slider, dest_lang=dest_lang))

Exit = Button(root, text="Exit", command=root.destroy)

l.pack()
inputtxt.pack()
slider_frame.pack()
Display.pack()
Output.pack()
Exit.pack()

root.mainloop()
