import pytest
from src.translator import translate_content

# Define the test cases

complete_eval_set_real = [
    {"post": "Hola me llamo Owen", "expected_answer": None},  # This will just print the result
    {"post": "Me gusta papas", "expected_answer": None},  # This will just print the result
    {"post": "Me gusta salchichas", "expected_answer": None}  # This will just print the result
]

@pytest.mark.parametrize("entry", complete_eval_set_real)
def test_translate_content(entry):
    post = entry["post"]
    # Call the function and print the result
    is_english, translation = translate_content(post)
    print(f"Post: {post}, Is English: {is_english}, Translation: {translation}")
