# trellminder
This is a simple cron job intended to run daily which sends an email alert to a [Trello](https://trello.com) user who wishes to know about overdue or nearly due cards.

## How to use
The files in this repo are intended to run in an [OpenShift](https://www.openshift.com) application but it could run anywhere with Python 2.6 and [requests](http://docs.python-requests.org/en/latest/) installed.  To run on OpenShift:

1. create python-2.6 app with cron cartridge
`rhc app create trellminder python-2.6`
`rhc cartridge add cron-1.4 -a trellminder`
2. add requests to your setup.py
`install_requires=['requests']`
3. drop in the above files (minus README.md) into ./openshift/cron/hourly

## Further info
I have a [blog post](http://codegouge.blogspot.com/2013/05/my-weekend-project-trellminder-trello.html) with a little more info.
