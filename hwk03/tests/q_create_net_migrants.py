test = {   'name': 'q_create_net_migrants',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(net_migrants.where('fips', 1017).column('omr').item(0), 0.02832077249175695, rtol=.005)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(net_migrants.where('fips', 1017).column('imr').item(0), 0.027113754121526144, rtol=.005)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
