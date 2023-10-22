from scripts.data_getters.get_cb_data import *


def test_get_key_rate():
    pass


def test_get_latest_date():
    pass


def test_get_previous_date_ordinal():
    test_input = "2023-10-14"
    expected = "2023-10-13"
    result = get_previous_date(test_input)
    assert result == expected


def test_get_curs_on_date():
    pass


def test_get_necessary_cb_curses():
    pass


def test_get_cb_usd():
    test_input = {
        "Доллар США": {
            "Vcurs": "50.80"
        },
        "Евро": {
            "Vcurs": "90.56"
        },
        "Китайский юань": {
            "Vcurs": "10.08"
        }
    }
    expected = "50.80"
    result = get_cb_usd(test_input)
    assert result == expected


def test_get_cb_eur():
    test_input = {
        "Доллар США": {
            "Vcurs": "50.80"
        },
        "Евро": {
            "Vcurs": "90.56"
        },
        "Китайский юань": {
            "Vcurs": "10.08"
        }
    }
    expected = "90.56"
    result = get_cb_eur(test_input)
    assert result == expected


def test_get_cb_cny():
    test_input = {
        "Доллар США": {
            "Vcurs": "50.80"
        },
        "Евро": {
            "Vcurs": "90.56"
        },
        "Китайский юань": {
            "Vcurs": "10.08"
        }
    }
    expected = "10.08"
    result = get_cb_cny(test_input)
    assert result == expected
