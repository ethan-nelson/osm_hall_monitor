from setuptools import setup

setup(name='OpenStreetMap Hall Monitor',
      version='0.2',
      description='Passive changeset monitoring for OpenStreetMap.',
      url='http://github.com/ethan-nelson/osm_hall_monitor',
      author='Ethan Nelson',
      author_email='ethan-nelson@users.noreply.github.com',
      install_requires = ['psycopg2','osmdt'],
      packages=['osmhm'],
      zip_safe=False)
      
