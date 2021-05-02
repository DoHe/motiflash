from pytest import mark

from cards.views import profile


@mark.parametrize("points,level", [
    (0, 1),
    (99, 1),
    (100, 2),
    (float("inf"), len(profile.LEVEL_BREAK_POINTS)),
    (-1, 1),
])
def test_level(points, level):
    assert profile.level_for_points(points) == level
