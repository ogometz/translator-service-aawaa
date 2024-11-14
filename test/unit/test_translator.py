from src.translator import translate_content
from unittest.mock import patch

def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_french():
    is_english, translated_content = translate_content("Ceci est un message en français")
    assert is_english == False
    assert translated_content == "This is a French message"

def test_spanish():
    is_english, translated_content = translate_content("Esta es un mensaje en español")
    assert is_english == False
    assert translated_content == "This is a Spanish message"

def test_portuguese():
    is_english, translated_content = translate_content("Esta é uma mensagem em português")
    assert is_english == False
    assert translated_content == "This is a Portuguese message"

def test_japanese():
    is_english, translated_content = translate_content("これは日本語のメッセージです")
    assert is_english == False
    assert translated_content == "This is a Japanese message"

def test_english():
    is_english, translated_content = translate_content("This is an English message")
    assert is_english == True
    assert translated_content == "This is an English message"

def test_llm_unexpected_response():
    with patch("src.translator.translate_content") as mock_translate:
        mock_translate.return_value = (False, "Unexpected response")
        is_english, translated_content = translate_content("Dies ist eine Nachricht auf Deutsch")
        assert is_english == False
        assert translated_content == "This is a German message"

def test_llm_gibberish_response():
    pass
