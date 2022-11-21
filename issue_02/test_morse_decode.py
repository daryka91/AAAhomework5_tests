from morse import decode
import pytest

@pytest.mark.parametrize(
    "source_string, result",
    [
        (".... . .-.. .-.. --- -....- --. ..- -.--", "HELLO-GUY"),
        ("... --- ...", "SOS"),
        (".... . .-.. .-.. ---   --. ..- -.--", "HELLO GUY"),
        (".... . .-.. .-.. --- --..--  --. ..- -.--", "HELLO, GUY")
    ]
)
def test_morse_decode(source_string, result):
    assert decode(source_string) == result
