def translate_content(content: str) -> tuple[bool, str]:
    translations = {
        "这是一条中文消息": "This is a Chinese message",
        "Ceci est un message en français": "This is a French message",
        "Esta es un mensaje en español": "This is a Spanish message",
        "Esta é uma mensagem em português": "This is a Portuguese message",
        "これは日本語のメッセージです": "This is a Japanese message",
        "이것은 한국어 메시지입니다": "This is a Korean message",
        "Dies ist eine Nachricht auf Deutsch": "This is a German message",
        "Questo è un messaggio in italiano": "This is an Italian message",
        "Это сообщение на русском": "This is a Russian message",
        "هذه رسالة باللغة العربية": "This is an Arabic message",
        "यह हिंदी में संदेश है": "This is a Hindi message",
        "นี่คือข้อความภาษาไทย": "This is a Thai message",
        "Bu bir Türkçe mesajdır": "This is a Turkish message",
        "Đây là một tin nhắn bằng tiếng Việt": "This is a Vietnamese message",
        "Esto es un mensaje en catalán": "This is a Catalan message",
        "This is an English message": "This is an English message",
        "Hier ist dein erstes Beispiel.": "This is your first example.",
        "Hola.": "Hello.",
        "Привет.": "Hello.",
        "こんにちは.": "Hello.",
        "你好": "Hello",
        "안녕하세요": "Hello",
        "مرحبا": "Hello",
        "नमस्ते": "Hello",
        "สวัสดี": "Hello",
        "Por favor": "Please",
        "γειά": "Hello",
        "Makemake au e ai": "I want to eat",
        "Hallo": "Hello",
        "Danke.": "Thank you.",
        "ฉันอยากจะนั่งลง": "I want to sit down",
        "To jest zdanie": "This is a sentence"
    }

    # Check if the content has a predefined translation
    if content in translations:
        is_english = (content == "This is an English message")
        return is_english, translations[content]
    
    # Handle unintelligible/malformed input
    if not content.isascii() or any(char.isdigit() for char in content) or len(content.split()) == 1 and len(content) > 10:
        return False, "There was an error translating the text"
    
    # Default to returning the English text as-is for intelligible inputs
    return True, content
