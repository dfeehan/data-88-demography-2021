test = {   'name': 'q_join_std_popn_voting',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> voting_2016_with_std.where('state', 'FLORIDA').where('age', '65+').column('pct_total_registered')[0]\n71.4", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.isclose(voting_2016_with_std.where('state', 'FLORIDA').where('age', '65+').column('us_std_prop')[0], .20873119, atol=.001)\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
