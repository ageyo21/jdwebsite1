#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


"""HTTP Methods
1)GET:-Append the info into the URL after the info in submitted in the form.
       Send the data by using key:value pairs  to the URL.
       e.g.http://www.jdphotography.com/index.html?name1=value1&name2=value2
       Can send upto 1024 characters only.
       Can't send binary data, like images or word documents,to the server.
       Don't use GET Method for sesnsitive info like password etc.
       
2)POST:-Transfers info via HTTP headers.
        No restriction on data size to be sent.
        Can send ASCII as well as binaryb data.
        Sent data goes through HTTP header so security depends on HTTP protocol.
        Using POST Method is secure.  
3)PUT:-Data updation,deletion
4)PATCH:-Data updation     
"""