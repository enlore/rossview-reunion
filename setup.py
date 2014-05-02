from setuptools import setup

setup(
       name="rossview.reunion.site",
       version="1.0.0",
       description="Simple form processing site",
       author="enlore",
       author_email="n.e.lorenson@gmail.com",
       url="",
       packages=["app"],
       zip_safe=False,
       include_package_data=True,
       install_requires=[
            "Fabric==1.8.3",
            "Flask==0.10.1",
            "Flask-Assets==0.9",
            "Flask-Script==0.6.7",
            "Flask-WTF==0.9.5",
            "Jinja2==2.7.2",
            "MarkupSafe==0.21",
            "WTForms==1.0.5",
            "Werkzeug==0.9.4",
            "argparse==1.2.1",
            "ecdsa==0.11",
            "gunicorn==18.0",
            "ipython==2.0.0",
            "itsdangerous==0.24",
            "paramiko==1.12.3",
            "py==1.4.20",
            "pycrypto==2.6.1",
            "pyjade==2.2.0",
            "pytest==2.5.2",
            "requests==2.2.1",
            "six==1.6.1",
            "webassets==0.9",
            "wsgiref==0.1.2"
           ]
        )
