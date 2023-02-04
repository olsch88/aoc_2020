import pytest
from ..d1 import solve_part1, solve_part2


@pytest.fixture
def sample_data():
    return [1721, 979, 366, 299, 675, 1456]


def test_part_1(sample_data):
    assert solve_part1(sample_data) == 514579


def test_part_2(sample_data):
    assert solve_part2(sample_data) == 241861950
