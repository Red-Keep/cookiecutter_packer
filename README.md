# Cookiecutter Packer

[![GitHub Super-Linter](https://github.com/Red-Keep/cookiecutter_packer/workflows/Super-Linter/badge.svg)](https://github.com/marketplace/actions/super-linter)

[Cookiecutter] template for a Packer scripts to build automated machine images.

* GitHub repo: <https://github.com/Red-Keep/cookiecutter-packer/>
* Documentation: <https://cookiecutter-packer.readthedocs.io/>
* Free software: MIT license
* Packer website: <https://www.packer.io/>

## Features

* Github Super-Linter setup
* Sphinx docs: Documentation ready for generation with, for example, ReadTheDocs

[Cookiecutter]: <https://github.com/audreyr/cookiecutter>

## Build Status

Linux:

[![Build](https://img.shields.io/travis/audreyr/cookiecutter-pypackage.svg)](https://travis-ci.org/audreyr/cookiecutter-pypackage)

Windows:

[![Build](https://ci.appveyor.com/api/projects/status/github/audreyr/cookiecutter-pypackage?branch=master&svg=true)](https://ci.appveyor.com/project/audreyr/cookiecutter-pypackage/branch/master)

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

`pip install -U cookiecutter`

Install [requests](https://requests.readthedocs.io/) package:

`pip install -U requests`

Generate a Packer script project:

`cookiecutter https://github.com/Red-Keep/cookiecutter-packer.git`

Then:

* Create a repo and put it there.
* Add the repo to your _ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for your project and their versions. For more info see the [pip docs for requirements files].
* Activate your project on `pyup.io`.

[pip docs for requirements files]: https://pip.pypa.io/en/stable/user_guide/#requirements-files

For more details, see the [cookiecutter-pypackage tutorial].

[cookiecutter-pypackage tutorial]: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

## Not Exactly What You Want?

Don't worry, you have options:

### Similar Cookiecutter Templates

* [Nekroze/cookiecutter-pypackage]: A fork of this with a PyTest test runner, strict flake8 checking with Travis/Tox, and some docs and `setup.py` differences.
* `tony/cookiecutter-pypackage-pythonic`_: Fork with py2.7+3.3 optimizations. Flask/Werkzeug-style test runner, `_compat` module and module/doc conventions. See `README.rst` or the [github comparison view] for exhaustive list of additions and modifications.
* `ardydedase/cookiecutter-pypackage`_: A fork with separate requirements files rather than a requirements list in the `setup.py` file.
* `lgiordani/cookiecutter-pypackage`_: A fork of Cookiecutter that uses Punch_ instead of Bumpversion_ and with separate requirements files.
* Also see the [network] and [family tree] for this repo. (If you find anything that should be listed here, please add it and send a pull request!)

### Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork this to create your own version. Or create your own; it doesn't strictly have to be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter Templates list above with a brief description.
* It's up to you whether or not to rename your fork/own version. Do whatever you think sounds good.

### Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if they make my own packaging experience better.


[Nekroze/cookiecutter-pypackage]: https://github.com/Nekroze/cookiecutter-pypackage
[github comparison view]: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
[network]: https://github.com/audreyr/cookiecutter-pypackage/network
[family tree]: https://github.com/audreyr/cookiecutter-pypackage/network/members
