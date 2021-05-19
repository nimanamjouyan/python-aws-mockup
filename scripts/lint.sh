#!/usr/bin/env bash

set -e
set -x

autoflake -r . --recursive --in-place --remove-all-unused-imports --exclude=__init__.py
isort -rc .
black . --line-length=120
flake8 .
