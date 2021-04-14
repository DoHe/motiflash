import pytest

from cards.utils import parse_export


@pytest.fixture
def export():
    return """Arroganz	prepotenz
Unvorsichtigkeit	imprudenza
Während er an sie dachte, war Peter glücklich	Mentre pensava a lei, Peter era felice"""


@pytest.fixture
def parsed_export():
    return [
        ["Arroganz", "prepotenz"],
        ["Unvorsichtigkeit", "imprudenza"],
        [
            "Während er an sie dachte, war Peter glücklich",
            "Mentre pensava a lei, Peter era felice"
        ],
    ]


def test_parse_export(export, parsed_export):
    actual = parse_export(export)
    assert actual == parsed_export
