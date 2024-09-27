from render import render
from rendered import RenderedBlock as Block
from rendered import RenderedCol as Col
from rendered import RenderedRow as Row

def test_renders_a_single_unit_block():
    fixture = Block(1, 1)
    fixture.place(0, 0)
    assert render(fixture) == "a"

def test_renders_a_large_block():
    fixture = Block(3, 4)
    fixture.place(0, 0)
    assert render(fixture) == "\n".join(["aaa", "aaa", "aaa", "aaa"])

def test_renders_a_row_of_two_blocks():
    fixture = Row(Block(1, 1), Block(2, 4))
    fixture.place(0, 0)
    assert render(fixture) == "\n".join(["acc", "acc", "acc", "bcc"])

# [col2]
def test_renders_a_column_of_two_blocks():
    fixture = Col(Block(1, 1), Block(2, 4))
    fixture.place(0, 0)
    expected = "\n".join(["ba", "cc", "cc", "cc", "cc"])
    assert render(fixture) == expected
# [/col2]

def test_renders_a_grid_of_rows_of_columns():
    fixture = Col(
        Row(Block(1, 2), Block(3, 4)), Row(Block(1, 2), Col(Block(3, 4), Block(2, 3)))
    )
    fixture.place(0, 0)
    assert render(fixture) == "\n".join(
        [
            "bddd",
            "bddd",
            "cddd",
            "cddd",
            "ehhh",
            "ehhh",
            "ehhh",
            "ehhh",
            "eiig",
            "fiig",
            "fiig",
        ]
    )
