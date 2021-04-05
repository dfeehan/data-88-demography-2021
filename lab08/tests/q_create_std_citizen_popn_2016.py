test = {   'name': 'q_create_std_citizen_popn_2016',
    'points': 4,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(std_citizen_popn_2016.where('age', '35 to 44').column('us_std_prop')[0], .153207, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(std_citizen_popn_2016.where('age', '65+').column('us_std_prop')[0], .209731, atol=.01)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
