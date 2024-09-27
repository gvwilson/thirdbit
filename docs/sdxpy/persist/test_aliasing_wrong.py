from io import StringIO

import pytest
from aliasing_wrong import LoadAlias, SaveAlias


# [roundtrip]
def roundtrip(fixture):
    writer = StringIO()
    SaveAlias(writer).save(fixture)
    reader = StringIO(writer.getvalue())
    return LoadAlias(reader).load()
# [/roundtrip]

# [no_aliasing]
def test_aliasing_no_aliasing():
    fixture = ["a", {"b": True, 7: {"c": "d"}}]
    assert roundtrip(fixture) == fixture
# [/no_aliasing]

# [shared]
def test_aliasing_shared_child():
    shared = ["content"]
    fixture = [shared, shared]
    result = roundtrip(fixture)
    assert result == fixture
    assert id(result[0]) == id(result[1])
    result[0][0] = "changed"
    assert result[1][0] == "changed"
# [/shared]


@pytest.mark.xfail
def test_aliasing_circular():
    fixture = []
    fixture.append(fixture)
    result = roundtrip(fixture)
    assert len(result) == 1
    assert id(result) == id(result[0])
