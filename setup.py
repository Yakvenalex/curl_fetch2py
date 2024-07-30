from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='curl_fetch2py',
    version='0.1',
    packages=find_packages(),
    author='Alexey Yakovenko',
    author_email='mr.mnogo@gmail.com',
    description='CurlFetch2Py - это библиотека на Python, предназначенная для парсинга команд curl и fetch, '
                'преобразуя их в структурированные объекты Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Yakvenalex/curl_fetch2py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
