test = {   'name': 'q_roni',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(unpd_roni.where('area', 'Malawi').where('period', 2000).column('roni').item(0), 28.261, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.isclose(unpd_roni.where('area', 'Germany').where('period', 1960).column('roni').item(0), 5.069, atol=.01)\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
