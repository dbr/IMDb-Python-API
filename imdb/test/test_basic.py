import imdb


def test_simple_search():
    sr = imdb.search("ghost busters")
    print sr