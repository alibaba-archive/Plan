#!/bin/bash

# Client dependencies
echo 'Install bower modules...'
cd media
bower install
cd ..

echo 'All Set Up. Start Server with `python manage.py runserver`'
