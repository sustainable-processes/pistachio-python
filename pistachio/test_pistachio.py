import pytest
from .pistachio import Pistachio


def test_pistachio():
    with Pistachio() as p:
        # Test parsing
        r = p.parse("GSK")
        expected_r = {
            "str": "GSK",
            "grouped": True,
            "cacheAllowed": True,
            "tags": [{"end": 3, "tag": "ASSIGNEE", "val": "GlaxoSmithKline"}],
        }
        assert all(r) == all(expected_r)

        # Test suggestions
        r = p.suggest("Suzuk")

        # Search
        r = p.search("suzuki_coupling")

        # g
