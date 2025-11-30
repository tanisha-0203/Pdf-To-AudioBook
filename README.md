🎧 PDF to Audiobook Converter (Python)

Convert any PDF file into an audiobook using Python!
This project uses PyPDF2 for PDF text extraction and pyttsx3 for offline text-to-speech conversion.

🚀 Features

📄 Reads PDF files page-by-page

🗣 Converts text to speech (fully offline)

🔊 Works with any English text-based PDF

🧠 Simple, clean, beginner-friendly Python code

🖥 No API keys or internet required

🧰 Technologies Used

Python 3.10+

PyPDF2 → for reading PDF files

pyttsx3 → for offline TTS (Text-to-Speech)
📦 Installation

Install dependencies:

pip install PyPDF2
pip install pyttsx3


Place your PDF file in the same folder as your Python script.

▶️ How to Run
python Book.py


Or rename your file as needed.

📌 Code Example
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

🎧 What This Program Does

Extracts text from every page of the PDF

Converts it into speech

Reads the entire PDF aloud like a real audiobook

Perfect for:

Students

Multitaskers

Visually impaired users

Listening to notes instead of reading

🔮 Future Improvements

GUI version (Tkinter)

Add play/pause buttons

Change voice rate / pitch

Export audio as .mp3 or .wav

Read selected pages

🤝 Contributing

Pull requests are welcome!
Feel free to fork the repo and improve the project.

📄 License

This project is open-source and free to use.
