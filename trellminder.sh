#!/bin/bash

source $OPENSHIFT_HOMEDIR/python-2.6/virtenv/bin/activate
python $OPENSHIFT_HOMEDIR/app-root/repo/.openshift/cron/daily/trellminder.py -c $OPENSHIFT_HOMEDIR/app-root/repo/.openshift/cron/daily/trellminder.cfg
