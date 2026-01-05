## Executing the examples:
'''
 pytest --lg-env env.yaml test_serial.py
'''

### Pytest verbose
'''
 pytest --lg-env=env.yaml test_serial.py -vvv

'''

### Pytest : view print statements
'''
 pytest -s -o log_cli=true --lg-env=env.yaml test_serial.py -vvv

'''