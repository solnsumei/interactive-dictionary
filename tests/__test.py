from app import format_definitions, translate

"""
    Test format definitions function
"""


def test_invalid_list_entered():
    assert format_definitions('sol', 'Hello') == "Error: function requires only lists"


def test_valid_list_entered():
    assert format_definitions('rain', ['A downpour']) == "rain: A downpour\n"


def test_valid_list_with_more_than_one_item():
    assert format_definitions('rain', ['A downpour', 'Liquid water']) == "rain: A downpour\nLiquid water\n"


"""
    Test translate function
"""


def test_word_not_found():
    assert translate('hhhhhhh') == "The word doesn't exist. Please double check it."


def test_word_found():
    result = "rain: Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.\n"
    result += "To fall from the clouds in drops of water.\n"
    assert translate('rain') == result


def test_acronym_found():
    result = "NATO: An international organization created in 1949 by the"
    result += " North Atlantic Treaty for purposes of collective security.\n"
    assert translate('nato') == result


def test_proper_noun_found():
    result = "Delhi: The largest metropolis by area and the second-largest metropolis by population in India.\n"
    assert translate('Delhi') == result