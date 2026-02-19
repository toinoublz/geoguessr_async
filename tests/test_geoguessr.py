"""
Tests for the geoguessr_async package.
"""

import pytest
import aiohttp

from geoguessr_async import Geoguessr
from geoguessr_async.models import GeoguessrStats
import geoguessr_async.geo_utils as gu


class TestGeoUtils:
    """Test utility functions."""

    def test_flatten_dict_simple(self):
        """Test flatten_dict with simple dictionary."""
        inputDict = {"a": 1, "b": 2}
        result = gu.flatten_dict(inputDict)
        assert result == {"a": 1, "b": 2}

    def test_flatten_dict_nested(self):
        """Test flatten_dict with nested dictionary."""
        inputDict = {"a": {"b": 1, "c": 2}, "d": 3}
        result = gu.flatten_dict(inputDict)
        expected = {"aB": 1, "aC": 2, "d": 3}
        assert result == expected

    def test_flatten_dict_deep_nested(self):
        """Test flatten_dict with deeply nested dictionary."""
        inputDict = {"a": {"b": {"c": {"d": 1}}}, "e": 2}
        result = gu.flatten_dict(inputDict)
        expected = {"aBCD": 1, "e": 2}
        assert result == expected


class TestGeoguessrInit:
    """Test Geoguessr class initialization."""

    @pytest.mark.asyncio
    async def test_geoguessr_init(self):
        """Test Geoguessr class initialization."""
        ncfa = "test_ncfa_token"
        geoguessr = Geoguessr(ncfa)

        assert geoguessr.ncfa == ncfa
        assert geoguessr.headers["Content-Type"] == "application/json"
        assert geoguessr.headers["cookie"] == f"_ncfa={ncfa}"
        assert isinstance(await geoguessr.session, aiohttp.ClientSession)
        assert geoguessr.me is None
        assert geoguessr.meStats is None
        assert geoguessr.friends is None
        assert geoguessr.activities is None
        assert geoguessr.meId is None
        assert geoguessr.meElo is None


class TestGeoguessrStats:
    """Test GeoguessrStats model."""

    def test_geoguessr_stats_init_with_data(self):
        """Test GeoguessrStats initialization with data."""
        testData = {
            "battleRoyaleRank": {
                "rank": 100,
                "rating": 1500,
                "gamesLeftBeforeRanked": 5
            },
            "duels": {
                "numGamesPlayed": 10
            }
        }

        stats = GeoguessrStats(testData)

        assert stats.battleRoyaleRankRank == 100
        assert stats.battleRoyaleRankRating == 1500
        assert stats.battleRoyaleRankGamesleftbeforeranked == 5
        assert stats.duelsNumgamesplayed == 10

    def test_geoguessr_stats_init_empty(self):
        """Test GeoguessrStats initialization with empty data."""
        stats = GeoguessrStats({})

        assert stats.battleRoyaleRankRank is None
        assert stats.battleRoyaleRankRating is None
        assert stats.duelsNumgamesplayed is None


if __name__ == "__main__":
    pytest.main([__file__])
