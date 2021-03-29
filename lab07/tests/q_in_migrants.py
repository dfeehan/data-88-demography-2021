test = {   'name': 'q_in_migrants',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> in_migrants.num_rows == 2695\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> in_migrants.where('fips', 17031).column('num_in_migrants').item(0) == 84079\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
