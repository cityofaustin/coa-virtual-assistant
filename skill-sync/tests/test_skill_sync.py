from skill_sync import __version__


def test_version():
    assert __version__ == '0.1.0'

"""
stuff to test
given an api key, we get a valid response
test using requeests library
test json output is valid
test output is saved to file (probs need some sort of naming convention)

TEST if response is 200 (ex i got rate limit exceeded)
"""
