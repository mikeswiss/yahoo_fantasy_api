#!/bin/python

from yahoo_fantasy_api import game, league
import mock_yhandler


def test_ids(sc):
    gm = game.Game(sc, 'mlb')
    gm.inject_yhandler(mock_yhandler.YHandler())
    ids = gm.league_ids()
    for i in ids:
        print(i)
    assert(len(ids) == 12)
    print(ids)
    assert(ids[5] == '268.l.46645')


def test_ids_for_year(sc):
    gm = game.Game(sc, 'mlb')
    gm.inject_yhandler(mock_yhandler.YHandler())
    ids = gm.league_ids(year=2017)
    assert(len(ids) == 1)
    print(ids)
    assert(ids[0] == '370.l.56877')


def test_to_league(sc):
    gm = game.Game(sc, 'mlb')
    gm.inject_yhandler(mock_yhandler.YHandler())
    lg = gm.to_league('370.l.56877')
    assert(type(lg) is league.League)
