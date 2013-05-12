# trellminder
This is a simple cron job intended to run daily which sends an email alert to a [Trello](https://trello.com) user who wishes to know about overdue or nearly due cards. I run this daily in order to get an email if a card which is assigned to me is overdue or due within in the next 24 hours.

I have a [blog post](http://codegouge.blogspot.com/2013/05/my-weekend-project-trellminder-trello.html) with a little more info. This script was only intended to scratch an itch but I thought others might get some good out of it.

## Usage
`trellminder.py -c config_file`

See trellminder.cfg for proper syntax.

## How to install 
The files in this repo are intended to run in an [OpenShift](https://www.openshift.com) application but it could run anywhere with Python 2.X and [requests](http://docs.python-requests.org/en/latest/) installed.  To run on OpenShift:

1. Create python-2.6 app with a cron cartridge: `rhc app create trellminder python-2.6`, `rhc cartridge add cron-1.4 -a trellminder`
2. Add requests to your setup.py: `install_requires=['requests']`
3. Configure trellminder.cfg accordingly.
4. Drop the above files (minus README.md) into ./openshift/cron/hourly
