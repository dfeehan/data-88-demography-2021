test = {   'name': 'q_create_tfr_dataset',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> unpd_tfr_2015.where('area', are.equal_to('Malawi'))['period'][0] == 2015\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> unpd_tfr_2015.where('area', are.equal_to('Mayotte'))['tfr'][0] == 4.1\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
