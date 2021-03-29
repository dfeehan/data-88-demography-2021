test = {   'name': 'q_alameda_arrivals',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> alameda_arrivals.num_rows == 147\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> alameda_arrivals.where('origin_fips', 6077).column('num_in_migrants').item(0) == 2162\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
