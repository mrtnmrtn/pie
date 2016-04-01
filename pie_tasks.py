from pathlib import Path

from pie import *


@task
def setup():
    createVenv()
    updateTestPackages()


@task
def createVenvs():
    venv(r'venvs\test').create()


@task
def updatePackages():
    with venv(r'venvs\test'):
        # update pip
        pip(r'install -U pip')
        # and update other requirements
        pip(r'install -U -r requirements.test.txt')


@task
def test():
    with venv(r'venvs\test'):
        cmd(r'py.test -s test')
