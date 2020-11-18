#! /usr/bin/env python3
from datetime import datetime

import requests


def process_license_text(text):
    """ retrieve only license text from repo

    Args:
        text: full text download from repo

    Returns:
        a string of only the license text and not the rest of the yaml
    """
    license_text = text.split("---")[-1]
    license_text = license_text.replace("[year]", str(year))
    license_text = license_text.replace("[fullname]", owner)
    license_text = license_text.strip()
    return license_text


# Using identified license, grab template text from https://github.com/github/choosealicense.com/tree/gh-pages/_licenses
license_type = "{{ cookiecutter.license }}"
project_slug = "{{ cookiecutter.project_slug }}"
company_name = "{{ cookiecutter.company_name }}"
# determine owner of Software
if company_name != " " or company_name != "":
    owner = "{{ cookiecutter.full_name }}"
else:
    owner = company_name

year = datetime.now().year
# Determine type of license
# License repo at https://github.com/github/choosealicense.com/tree/gh-pages/_licenses
# Raw version of file retrieved from url in license_url
license_url = "https://raw.githubusercontent.com/github/choosealicense.com/gh-pages/_licenses/{}.txt".format(
    license_type.lower()
)
if license_type == "Not Sure":
    license_text = (
        "All rights reserved. No License offered.\nCopyright (c) {year} {owner}"
    ).format(year=year, owner=owner)
else:
    license = requests.get(license_url)
    license_text = process_license_text(license.text)

# write license to file
f = open("./LICENSE.md", "x")
f.write(license_text)
f.close()
