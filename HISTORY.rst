History
=======

0.3.4 Sun Jan 18 16:01:06 2026 -0800
------------------------------------

0.3.3 Sun Jan 18 15:56:47 2026 -0800
------------------------------------

fixed issue #20

:Problem: Some cleanup needed on moving to uv
:Solution: cleanup done .. see below

::

    modified:   pyproject.toml
    deleted:    requirements.txt
    deleted:    requirements_dev.txt
    deleted:    setup.cfg
    deleted:    setup.py
    modified:   uv.lock

fixed issue #18

:Problem: Need pytests when pushing to master/develop branch
:Solution: Used github actions to trigger pytests

fixed issue #17

:Problem: Document steps for a release
:Solution: steps are documented in runningnotes.rst 2026-01-18



0.3.2 Sun Jan 18 08:58:56 2026 -0800
------------------------------------

fixed issue #11

:Problem: Documentation shows use of python2
:Solution: updated documentation to use python3

fixed issue #10

:Problem: Need notes on how to use uv
:Solution: added uv to notes.txt

fixed issue #9

:Problem: dependency on six not needed - not using python2
:Solution: remove dependency on six in pyproject.toml

fixed issue #8

:Problem: pyproject.toml says python3.13 - downgrade this
:Solution: downgraded to python3.9


0.3.0 (2018-05-04)
------------------

* Fairly complete Release

0.1.0 (2018-03-23)
------------------

* First release on PyPI.

Initial Coding (2013)
---------------------

* All coding was complete in 2013, but not yet packaged for release.
