@ECHO OFF

@ECHO "Output: 1"
challenge.py 1

@ECHO "Output: bus car truck"
challenge.py car truck bus

@ECHO "Output: -2 1 4 5 6 8 9"
challenge.py 8 4 6 1 -2 9 5

@ECHO "Output: bus car 1 4 truck 6 8"
challenge.py car truck 8 4 bus 6 1
