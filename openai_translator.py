import tkinter as tk
from tkinter import ttk
import requests
import json
import os


class TextTranslatorApp:
    def __init__(self, root):
        self.root = root
        root.title("OpenAI Text Translator")

        self.create_widgets()

    def create_widgets(self):
        # Label và Entry cho text input
        label1 = tk.Label(self.root, text="Enter text to translate:")
        self.entry = tk.Entry(self.root, width=50)

        # Label và Combobox cho source language
        label2 = tk.Label(self.root, text="Choose source language:")
        self.source_lang = ttk.Combobox(self.root,
                                        values=["en", "es", "fr", "vi", "ja", "zh", "de", "ko", "th", "auto"])
        self.source_lang.set("auto")

        # Label và Combobox cho target language
        label3 = tk.Label(self.root, text="Choose target language:")
        self.target_lang = ttk.Combobox(self.root, values=["en", "es", "fr", "vi", "ja", "zh", "de", "ko", "th"])
        self.target_lang.set("vi")

        # Button để translate
        translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)

        # Label để hiển thị kết quả
        self.result_label = tk.Label(self.root, text="Translated text will appear here.", wraplength=400,
                                     justify="left")

        # Grid layout giống như mẫu
        label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.source_lang.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        label3.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.target_lang.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        translate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def translate_text(self):
        text_to_translate = self.entry.get()

        if not text_to_translate.strip():
            self.result_label.config(text="Please enter text to translate.")
            return

        source_lang_code = self.source_lang.get()
        target_lang_code = self.target_lang.get()

        # Using LibreTranslate free API (no API key needed)
        url = "https://libretranslate.de/translate"

        # Convert language codes
        lang_mapping = {
            "auto": "auto",
            "en": "en",
            "es": "es",
            "fr": "fr",
            "vi": "vi",
            "ja": "ja",
            "zh": "zh",
            "de": "de",
            "ko": "ko",
            "th": "th"
        }

        source = lang_mapping.get(source_lang_code, "auto")
        target = lang_mapping.get(target_lang_code, "vi")

        data = {
            "q": text_to_translate,
            "source": source,
            "target": target,
            "format": "text"
        }

        try:
            self.result_label.config(text="Translating...")
            self.root.update()

            response = requests.post(url, data=data)
            response.raise_for_status()

            result = response.json()
            translated_text = result.get('translatedText', 'Translation failed')

            self.result_label.config(text=f"Translation: {translated_text}")

        except requests.exceptions.RequestException as e:
            mock_translations = {
                "hello": {"vi": "xin chào", "es": "hola", "fr": "bonjour", "de": "hallo"},
                "goodbye": {"vi": "tạm biệt", "es": "adiós", "fr": "au revoir", "de": "auf wiedersehen"},
                "thank you": {"vi": "cảm ơn", "es": "gracias", "fr": "merci", "de": "danke"},
                "yes": {"vi": "có", "es": "sí", "fr": "oui", "de": "ja"},
                "no": {"vi": "không", "es": "no", "fr": "non", "de": "nein"}
            }

            text_lower = text_to_translate.lower()
            if text_lower in mock_translations and target_lang_code in mock_translations[text_lower]:
                translated_text = mock_translations[text_lower][target_lang_code]
                self.result_label.config(text=f"Translation (offline): {translated_text}")
            else:
                self.result_label.config(text=f"Translation service unavailable. Original text: {text_to_translate}")

        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextTranslatorApp(root)
    root.mainloop()
