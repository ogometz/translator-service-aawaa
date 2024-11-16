
from src.translator import translate_content


def test_llm_normal_response_chinese():
    """Test for Chinese language translation."""
    is_english, translated_content = translate_content("这是一条中文消息")
    print(f"Post: '这是一条中文消息', Is English: {is_english}, Translation: {translated_content}")
    assert is_english == False
    assert translated_content == "This is a Chinese message"


def test_llm_normal_response_spanish():
    """Test for Spanish language translation."""
    is_english, translated_content = translate_content("Hola, ¿cómo estás?")
    print(f"Post: 'Hola, ¿cómo estás?', Is English: {is_english}, Translation: {translated_content}")
    assert is_english == False
    assert translated_content == "Hello, how are you?"


def test_llm_normal_respons_french():
    """Test for French language translation."""
    is_english, translated_content = translate_content("Bonjour, je m'appelle Jean.")
    print(f"Post: 'Bonjour, je m'appelle Jean.', Is English: {is_english}, Translation: {translated_content}")
    assert is_english == False
    assert translated_content == "Hello, my name is Jean."


def test_llm_normal_respons_german():
    """Test for German language translation."""
    is_english, translated_content = translate_content("Guten Tag, wie geht es Ihnen?")
    print(f"Post: 'Guten Tag, wie geht es Ihnen?', Is English: {is_english}, Translation: {translated_content}")
    assert is_english == False
    assert translated_content == "Good day, how are you?"


def test_llm_normal_respons_japanese():
    """Test for Japanese language translation."""
    is_english, translated_content = translate_content("こんにちは、お元気ですか？")
    print(f"Post: 'こんにちは、お元気ですか？', Is English: {is_english}, Translation: {translated_content}")
    assert is_english == False
    assert translated_content == "Hello, how are you?"


def test_llm_normal_respons_english():
    """Test for a normal response in English."""
    is_english, translated_content = translate_content("The weather is nice today.")
    print(f"Post: 'The weather is nice today.', Is English: {is_english}, Translation: {translated_content}")
    assert is_english == True
    assert translated_content == "The weather is nice today."


def test_llm_gibberish_response():
    """Test for gibberish input."""
    is_english, translated_content = translate_content("asdfghjkl12345")
    print(f"Post: 'asdfghjkl12345', Is English: {is_english}, Translation: {translated_content}")
    assert is_english == False
    assert translated_content == "There was an error translating the text"
