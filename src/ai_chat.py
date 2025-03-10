import openai
import os
from dotenv import load_dotenv

# Załaduj klucz API z pliku .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_response(query):
    """Generuje odpowiedź AI na podstawie zadanego pytania."""
    if not OPENAI_API_KEY:
        return "Błąd: Brak klucza API. Upewnij się, że zmienna środowiskowa OPENAI_API_KEY jest ustawiona."

    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)  # NOWA INICJALIZACJA KLIENTA
        
        response = client.chat.completions.create(  # NOWA METODA WYWOLANIA
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        return response.choices[0].message.content  # POPRAWNE ODCZYTANIE WYNIKU

    except Exception as e:
        return f"Błąd OpenAI: {str(e)}"
