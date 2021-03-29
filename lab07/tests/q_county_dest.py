test = {   'name': 'q_county_dest',
    'points': 8,
    'suites': [   {   'cases': [   {'code': '>>> cd.num_rows == 6\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> cd.where('dest_fips', 1073).column('num_out_migrants').item(0) == 47\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
