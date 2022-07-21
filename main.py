# pip install pdfplumber gtts art
from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'[+] Original file name {Path(file_path).name}')
        print('[+] Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        audio.save(f'{file_name}')

        return f'[+] {file_name}.mp3 saved successfully!\n -- Have a good day! --'
    elif file_path == '':
        return 'You did not enter a path.'
    else:
        return 'File not exists. Check the file path.'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    print("[!] You must enter file language.")
    language = input("Choose language, for example 'en' or 'ru'(by default it's en): ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()


# The language of PDF file MUST be tha same as MP3 file. If PDF file lang en, the lang of mp3 file also must be en.
