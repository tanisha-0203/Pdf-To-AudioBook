# import pyttsx3
# import PyPDF2
# book=open('report.pdf','rb')
# pdfReader=PyPDF2.PdfReader(book)
# pages=pdfReader.numPages
# print(pages)
# speaker=pyttsx3.init()
# speaker.say('Look Mama i can talk')
# speaker.runAndWait()

import pyttsx3
from PyPDF2 import PdfReader

# Open PDF
book = open('report.pdf', 'rb')
pdfReader = PdfReader(book)

# Number of pages
pages = len(pdfReader.pages)
print(pages)

# Text-to-speech
speaker = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
# page=pdfReader.pages[8]
# text=page.extract_text()
# speaker.say(text)
# # speaker.say('Look Mama, I can talk!')
# speaker.runAndWait()

