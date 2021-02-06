test = {   'name': 'q_e0_byperiod',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> e0_byperiod.num_rows == 5226\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> e0_byperiod.labels == ('area', 'sex', 'period', 'e')\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.isclose(e0_byperiod.where('sex', are.equal_to('male')).where('area', are.equal_to('Malawi')).where('period', "
                                               "are.equal_to(1955))['e'][0],35.799978)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
