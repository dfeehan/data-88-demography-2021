test = {   'name': 'q_out_migrants',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> out_migrants.num_rows == 2671\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> out_migrants.where('fips', 17031).column('num_out_migrants').item(0) == 114872\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
