
## Crerate a Virtual environment:
'''
 python3 -m venv .venv
'''

## Activate Virtual environment
'''
 source .venv/bin/Activate
'''

Install the dependencies:
'''
 pip install --upgrade pip
 pip install openhtf six setuptools labgrid
'''

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

