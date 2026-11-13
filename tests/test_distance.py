import pytest

from vector_store.scoring import distance_to_score


@pytest.mark.parametrize(
    "distance, expected",
    [
        (0.0, 100.0),   
        (1.0, 0.0), 
        (0.5, 50.0),
        (0.15, 85.0),
        (0.12345, 87.66),  
    ],
)
def test_distance_to_score(distance, expected):
    assert distance_to_score(distance) == expected


def test_score_never_exceeds_100():
    assert distance_to_score(-0.2) == 100.0  


def test_score_never_below_0():
    assert distance_to_score(1.7) == 0.0  


def test_better_match_scores_higher():
    assert distance_to_score(0.1) > distance_to_score(0.4)