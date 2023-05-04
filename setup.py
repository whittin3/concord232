from setuptools import setup

setup(name='concord232',
      version='0.15',
      description='GE Concord 4 RS232 Serial Interface Library and Server',
      author='Jason Carter',
      author_email='jason@jason-carter.net',
      url='https://github.com/whittin3/concord232',
      packages=['concord232'],
      install_requires=['requests', 'stevedore', 'prettytable', 'pyserial', 'flask'],
      scripts=['concord232_server', 'concord232_client']
  )
