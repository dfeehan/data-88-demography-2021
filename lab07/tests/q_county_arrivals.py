test = {   'name': 'q_county_arrivals',
    'points': 8,
    'suites': [   {   'cases': [   {'code': '>>> ca.num_rows == 7\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> ca.where('origin_fips', 1117).column('num_in_migrants').item(0) == 50\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
