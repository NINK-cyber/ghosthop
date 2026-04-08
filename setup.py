from setuptools import setup

setup(
    name='ghosthop', # Nome do pacote
    version='1.0.0',
    py_modules=['proxy'], # O nome do seu arquivo .py atual
    install_requires=[
        'flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'ghosthop=proxy:main', # Aqui! O comando será 'ghosthop'
        ],
    },
)