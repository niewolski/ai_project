import openai
import os
from dotenv import load_dotenv

# Załaduj klucz API z pliku .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Upewnij się, że klucz API jest poprawnie wczytany
if not OPENAI_API_KEY:
    raise ValueError("Błąd: Brak klucza API! Sprawdź plik .env lub zmienne środowiskowe.")

# Nowa inicjalizacja klienta OpenAI dla wersji 1.65.5
client = openai.Client(api_key=OPENAI_API_KEY)

def generate_response(query):
    """Generuje odpowiedź AI na podstawie zadanego pytania."""

    if not query or len(query.strip()) == 0:
        return "Błąd: Pytanie nie może być puste."

    try:
        response = client.chat.completions.create(  # NOWY FORMAT
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}],
            temperature=0.7
        )
        return response.choices[0].message.content  # ZWRÓĆ TEKSTOWĄ ODPOWIEDŹ

    except openai.APIConnectionError:
        return "Błąd: Nie można połączyć się z OpenAI. Sprawdź swoje połączenie internetowe."
    
    except openai.AuthenticationError:
        return "Błąd: Nieprawidłowy klucz API OpenAI. Sprawdź plik `.env`."

    except openai.APIError as e:
        return f"Błąd OpenAI API: {e}"

    except Exception as e:
        return f"Błąd krytyczny: {str(e)}"
