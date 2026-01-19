============================
Running Notes for pyclearsky
============================

2026-01-18
==========

Changed __init__.py # version

bumping a version and pushing branch and pushing tags

::

    uv version --bump patch/minor/major

    git commit -m "Bump version to $(uv version --short)"
    git tag "v$(uv version --short)"
    git push origin <branch>
    git push origin tag "v$(uv version --short)"

Now publish::

    uv build
    uv publish --token # token comes here

------

Lists of files changing when uv is used::

files changed::

    .github/workflows/tests.yml # for github actions
    pyclearsky/__init__.py # version is got from pyproject.toml
    docs/requirements.txt # needed for readthedocs
    pyproject.toml # uv likes having everything here

Once uv is set upthese files can be removed::

    requirements.txt
    requirements_dev.txt
    setup.cfg
    setup.py

------

running on uv

bump an update and publish to pypi
