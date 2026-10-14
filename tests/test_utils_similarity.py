from backend.utils.similarity import jaccard

def test_jaccard_overlap():
    assert jaccard("hello world", "hello there") > 0.2
