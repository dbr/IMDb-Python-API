import imdb


def test_simple_search():
    sr = imdb.search("ghost busters")
    first = sr['data']['results'][0]['list'][0]
    print first
    assert first['title'] == 'Ghost Busters'
    assert first['tconst'] == 'tt0087332'
