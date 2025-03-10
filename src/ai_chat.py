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
        # PRAWIDŁOWA INICJALIZACJA KLIENTA OpenAI
        client = openai.OpenAI(api_key=OPENAI_API_KEY)  

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}],
            temperature=0.7
        )
        return response.choices[0].message.content

    except openai.APIConnectionError:
        return "Błąd: Problem z połączeniem do OpenAI. Sprawdź swoje połączenie internetowe."

    except openai.APIStatusError as e:
        return f"Błąd API: {e.status_code} - {e.response.text}"

    except Exception as e:
        return f"Błąd krytyczny: {str(e)}"
