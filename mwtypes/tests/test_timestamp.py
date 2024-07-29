import pickle

from ..timestamp import LONG_MW_TIME_STRING, Timestamp


def test_self():
    t1 = Timestamp(1234567890)

    # Unix timestamp
    assert t1 == Timestamp(int(t1))

    # Short format
    assert t1 == Timestamp(t1.short_format())

    # Long format
    assert t1 == Timestamp(t1.long_format())


def test_comparison():
    t1 = Timestamp(1234567890)
    t2 = Timestamp(1234567891)

    assert t1 < t2, "Less than comparison failed"
    assert t2 > t1, "Greater than comparison failed"
    assert not t2 < t1, "Not less than comparison failed"
    assert not t1 > t2, "Not greater than comparison failed"

    assert t1 <= t2, "Less than or equal to comparison failed"
    assert t1 <= t1, "Less than or equal to comparison failed"
    assert t2 >= t1, "Greater than or equal to comparison failed"
    assert t2 >= t2, "Greater than or equal to comparison failed"
    assert not t2 <= t1, "Not less than or equal to comparison failed"
    assert not t1 >= t2, "Not greater than or equal to comparison failed"



def test_subtraction():
    t1 = Timestamp(1234567890)
    t2 = Timestamp(1234567891)

    assert t2 - t1 == 1
    assert t1 - t2 == -1
    assert t2 - 1 == t1


def test_strptime():
    assert (
        Timestamp("2009-02-13T23:31:30Z") ==
        Timestamp.strptime("2009-02-13T23:31:30Z", LONG_MW_TIME_STRING))

    assert (
        Timestamp.strptime(
            "expires 03:20, 21 November 2013 (UTC)",
            "expires %H:%M, %d %B %Y (UTC)"
        ) ==
        Timestamp("2013-11-21T03:20:00Z"))


def test_strftime():
    assert (
        Timestamp("2009-02-13T23:31:30Z").strftime(LONG_MW_TIME_STRING) ==
        "2009-02-13T23:31:30Z")

    assert (
        Timestamp("2009-02-13T23:31:30Z").strftime("expires %H:%M, %d %B %Y (UTC)") ==
        "expires 23:31, 13 February 2009 (UTC)")


def test_json():
    timestamp = Timestamp(1234567890)
    assert (
        timestamp ==
        Timestamp.from_json(timestamp.to_json()))

def test_pickling():
    timestamp = Timestamp(1234567890)
    assert (
        timestamp ==
        pickle.loads(pickle.dumps(timestamp)))
