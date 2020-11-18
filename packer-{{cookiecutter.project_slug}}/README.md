# {{ cookiecutter.project_name }}
{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

{% if is_open_source %}
[![GitHub Super-Linter](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Super-Linter/badge.svg)](https://github.com/marketplace/actions/super-linter)

{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: <https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io>.
{% endif %}

## Features

* TODO

## Credits

This package was created with Cookiecutter and the [Red-Keep/cookiecutter-packer] project template.

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Red-Keep/cookiecutter-packer]: https://github.com/jasimmonsv/cookiecutter-packer
