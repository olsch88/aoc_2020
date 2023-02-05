import pytest
from ..d4 import (
    solve_part1,
    solve_part2,
    is_passport_valid_part2,
    get_passport_data,
    get_data,
)


@pytest.fixture
def sample_data_valid():

    return get_passport_data(get_data("d4_valids.txt"))


@pytest.fixture
def sample_data_invalid():

    return get_passport_data(get_data("d4_invalids.txt"))


def test_valids(sample_data_valid):
    for pp in sample_data_valid:

        assert is_passport_valid_part2(pp) is True


# def test_part_2(sample_data):
#     assert solve_part2(sample_data) == 241861950
