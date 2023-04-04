from src.utils.parsing import slash_split

def test_slash_split():

    period = {'period': '2021-01-38/2020-02-26'}
    expect = {
        'period': {
              'min': '2020-02-26'
            , 'max': '2021-01-38'
        }
    }

    assert slash_split(period) == expect