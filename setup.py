import platform
if platform.system() == 'Windows':
    from distutils.core import setup
    import py2exe

    data_files = []
    setup(
        name='School',
        console=['main.py'],
        options={
            'py2exe': {
                'packages': ["sprites"],
                'dist_dir': 'dist_win',
                'compressed': True,
                'includes': [],
            }
        },

        data_files=data_files

    )
else:
    from setuptools import setup
    setup(
        app=["main.py"],
        setup_requires=["py2app"],
    )