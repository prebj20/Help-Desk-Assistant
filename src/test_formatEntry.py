import pytest

import Mod


def test_formatted():
    input_before = "        - - --cmd -Kb-- - g      "
    expected = "cmd -kb -g"
    input_after = Mod.suggest(input_before)

    assert input_after == expected

    input_before = "     cmd "
    expected = "cmd"
    input_after = Mod.suggest(input_before)

    assert input_after == expected

    input_before = "cmd -kB--g      -D"
    expected = "cmd -kb -g -d"
    input_after = Mod.suggest(input_before)

    assert input_after == expected

def test_args():
    input_before = "     cmd -KB -g      "
    expected = "[cmd][-kb][-g]"
    input_list = Mod.args(input_before)

    input_after = str()

    for string in input_list:
        input_after += f"[{string}]"

    assert input_after == expected

