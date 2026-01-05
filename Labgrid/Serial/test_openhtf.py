'''
Description: To test Serial Write and Read. 
Arguments: Modify the env.yaml file to add your device serial port and board rate paramaters.

Author: Muzammil Patel
Date :05/01/2025
'''
from time import sleep

def test_command_test(target):
    shell = target.get_driver("SerialDriver")
    # Activate the Shell
    shell.on_activate()
    # Write on the Serial
    sh =shell.write(b"AT\r\n")
    sleep(0.5)

    # Read the Serial Port
    sh = shell.read(timeout=2.0)
    print(f" Serial received message :{sh.decode("utf-8")}")
    
    # Deactivate the Shell
    shell.on_deactivate()
 
