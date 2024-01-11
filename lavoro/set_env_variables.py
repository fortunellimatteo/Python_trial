import os

if 'CODING' in os.environ:
    print(os.environ["CODING"])
else:
    print("No USERDOMAIN variable in environment variables")