from setuptools import setup, find_packages

setup(
    name='lfile',
    version='0.1.0',
    author='lvdstr',
    author_email='nathanfabianosilva.com',
    description='módulo Python com pequenas funções de manipulação de arquivos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seuusuario/meu_modulo',  # Repositório do GitHub
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        "colorama"
    ],
)
