test = {   'name': 'q_voting_2016_tot',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> voting_2016_tot.where('state', 'FLORIDA').column('pct_total_registered')[0]\n59.3", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all(voting_2016_tot['age'] == 'Total')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all(voting_2016_tot['state'] != 'US')\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
