import pyttsx3
import PyPDF2
from tkinter.filedialog import *

# Opening the pdf file-book
book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    voice = pyttsx3.init()
    voice.say(text)
    voice.runAndWait()