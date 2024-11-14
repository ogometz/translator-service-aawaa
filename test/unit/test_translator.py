import pytest
from src.translator import translate_content

# Define the test cases
complete_eval_set = [
    {"post": "Hier ist dein erstes Beispiel.", "expected_answer": (False, "This is your first example.")},
    {"post": "Hola.", "expected_answer": (False, "Hello.")},
    {"post": "Привет.", "expected_answer": (False, "Hello.")},
    {"post": "こんにちは.", "expected_answer": (False, "Hello.")},
    {"post": "你好", "expected_answer": (False, "Hello")},
    {"post": "안녕하세요", "expected_answer": (False, "Hello")},
    {"post": "مرحبا", "expected_answer": (False, "Hello")},
    {"post": "नमस्ते", "expected_answer": (False, "Hello")},
    {"post": "สวัสดี", "expected_answer": (False, "Hello")},
    {"post": "Por favor", "expected_answer": (False, "Please")},
    {"post": "γειά", "expected_answer": (False, "Hello")},
    {"post": "Makemake au e ai", "expected_answer": (False, "I want to eat")},
    {"post": "Hallo", "expected_answer": (False, "Hello")},
    {"post": "Danke.", "expected_answer": (False, "Thank you.")},
    {"post": "ฉันอยากจะนั่งลง", "expected_answer": (False, "I want to sit down")},
    {"post": "To jest zdanie", "expected_answer": (False, "This is a sentence")},
    {"post": "Hello.", "expected_answer": (True, "Hello.")},
    {"post": "Answer Answer.", "expected_answer": (True, "Answer Answer.")},
    {"post": "Today is a nice day.", "expected_answer": (True, "Today is a nice day.")},
    {"post": "INteresting task.", "expected_answer": (True, "INteresting task.")},
    {"post": "test Symbols!", "expected_answer": (True, "test Symbols!")},
    {"post": "No fullstop", "expected_answer": (True, "No fullstop")},
    {"post": "no caps.", "expected_answer": (True, "no caps.")},
    {"post": "grammar the incorrect", "expected_answer": (True, "grammar the incorrect")},
    {"post": "Database class.", "expected_answer": (True, "Database class.")},
    {"post": "More tests.", "expected_answer": (True, "More tests.")},
    {"post": "hello hello hello.", "expected_answer": (True, "hello hello hello.")},
    {"post": "tis has incorect speling.", "expected_answer": (True, "tis has incorect speling.")},
    {"post": "FINAL ENGLISH.", "expected_answer": (True, "FINAL ENGLISH.")},
    {"post": "biuycia8173sdo8yw", "expected_answer": (False, "There was an error translating the text")},
    {"post": "12345 678900", "expected_answer": (False, "There was an error translating the text")},
    {"post": "adguiwhdoin", "expected_answer": (False, "There was an error translating the text")},
    {"post": "qwertyuiopp", "expected_answer": (False, "There was an error translating the text")}
]

# Parameterize the test to create a separate test for each entry in `complete_eval_set`
@pytest.mark.parametrize("entry", complete_eval_set)
def test_translate_content(entry):
    post = entry["post"]
    expected_is_english, expected_translation = entry["expected_answer"]
    is_english, translation = translate_content(post)
    assert is_english == expected_is_english, f"Failed on: {post}"
    assert translation == expected_translation, f"Failed on: {post}"
