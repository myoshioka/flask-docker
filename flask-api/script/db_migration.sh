#!/bin/bash

orator migrate -c db/db_conf.py -p db/migrations/ -f
orator db:seed -c db/db_conf.py -p db/seeder/ -f

