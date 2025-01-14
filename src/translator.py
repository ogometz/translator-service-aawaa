from openai import AzureOpenAI
import os

# First Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key = os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint="https://apirecitation.openai.azure.com"  # Replace with your Azure endpoint
    )


def get_language(post: str) -> str:
    context = f"I'm trying to translate some text, only return the language it is written in and nothing else. What is the language this text: {post} is written in."

    try:
        # Make request for language detection
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": context
                }
            ]
        )

        # Extract and return detected language
        detected_lang = response.choices[0].message.content.strip()
        # print("this is detected lang:", detected_lang)
        return detected_lang

    except Exception as e:
        print(f"Error: {e}")
        return ""
    

def get_translation(post: str) -> str:
    context = (
        f"I want to translate an input text to English."
        f"First, check the language of the text. If the language is English, return the original input exactly as it is, with no changes at all."
        f"If the text does not belong to any language, even after uncapitalizing the input text, return the statement 'There was an error translating the text'."
        f"If the text can be translated to English, return only the translated text to English with no additional text. Do not add, remove, or alter any punctuation marks; match the punctuation pattern of the original text exactly."
        f"For example, if the input is 'Hola' translate it to 'Hello' without any punctuation. If the input has punctuation, like '¡Hola!', translate it as 'Hello!' preserving the punctuation style."
        f"This is the input text: '{post}'."
    )

    try:
        # Make request for translation
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": context
                }
            ]
        )

        # Extract and return translated text
        translation = response.choices[0].message.content.strip()
        return translation

    except Exception as e:
        print(f"Error translating: {e}")
        return ""


def translate_content(content: str) -> tuple[bool, str]:
    try:
        is_eng = get_language(content)
        if (is_eng is None or
        not isinstance(is_eng, str) or
        is_eng == "N/A" or
        len(is_eng) <= 0 or
        is_eng == "I don't understand your request"):
            return False, "There was an error translating the text"

        if is_eng == "English":
            return True, content
        else:
            translated = get_translation(content)
            if (translated is None or
            not isinstance(translated, str) or
            translated == "N/A" or
            len(translated) <= 0 or
            translated == "I don't understand your request"):
                return False, "There was an error translating the text"

            original_full_stop_exist = content.endswith(".")
            translated_post_full_stop_exist = translated.endswith(".")

            if original_full_stop_exist and not translated_post_full_stop_exist:
                return False, translated + "."

            if not original_full_stop_exist and translated_post_full_stop_exist:
                return False, translated[:-1]

            return False, translated

    except Exception as e:
        return False, "There was an error translating the text"
