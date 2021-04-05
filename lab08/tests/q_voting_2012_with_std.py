test = {   'name': 'q_voting_2012_with_std',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> voting_2012_with_std.where('state', 'DISTRICT OF COLUMBIA').where('age', '25 to 34').column('pct_citizen_registered')[0]\n85.3",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.isclose(voting_2012_with_std.where('state', 'DISTRICT OF COLUMBIA').where('age', '25 to 34').column('us_std_prop')[0], 0.1708671221933117, "
                                               'atol=.001)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
