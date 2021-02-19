import pytest

def capitalize_case(text:str):
    if not isinstance(text, str):
        raise TypeError("Please provide a string")
    
    return text.capitalize()

def test_capitalize_case():
    assert capitalize_case("some text") == "Some text"

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capitalize_case(3)
        # capitalize_case({"elt": 34})

# def main():
#     test_capitalize_case()

# if __name__ == "__main__":
#     main()
