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

running on uv

bump an update and publish to pypi
