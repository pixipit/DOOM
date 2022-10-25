import platform
if platform.system() == 'Windows':
    from distutils.core import setup
    import py2exe
    setup(console=['hello.py'])
else:
    from setuptools import setup
    setup(
        app=["main.py"],
        setup_requires=["py2app"],
    )