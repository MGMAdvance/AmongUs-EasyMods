from distutils.core import setup
import py2exe

setup(options={
        'py2exe': {'bundle_files': 1, 'compressed': True}
    },
    name="easymods",
    console=['easymods.py'],
    zipfile=None
    )