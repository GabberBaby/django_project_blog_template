#!/bin/bash

./manage.py syncdb --all
./manage.py migrate --fake