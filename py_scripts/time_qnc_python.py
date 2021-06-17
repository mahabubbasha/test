#!/usr/local/bin/python

import subprocess

from datetime import datetime
from datetime import timedelta

hostname = 'gnats'
QUERY_PR = '/usr/local/bin/query-pr -H '+ hostname + ' -P 1529 '
INIT_QEXPR = 'number == "661330"'


#qnc_path = '/homes/spaku/timings/qnc_time.csv'
qnc_path = '/homes/rajesha/qnc_time.csv'

qnc_file = open(qnc_path,'a')

start_time = datetime.now()
PR_NUMS = subprocess.Popen(QUERY_PR + ' -F -e \'' + INIT_QEXPR + '\' | wc -l', \
                           shell=True, stdout=subprocess.PIPE, \
                           stderr=subprocess.STDOUT)

for num in PR_NUMS.stdout.readlines():
    num = num.decode(encoding='utf-8').rstrip('\r\n')

dt = datetime.now() - start_time
ms = (((dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0) / 1000)
qnc_file.write('Q13,'+str(ms)+'\n')

INIT_QEXPR = '-e \'responsible == "phil"\' --summary --state=\'open|verify-resolution|need-info|analyzed\''
start_time = datetime.now()
PR_NUMS = subprocess.Popen(QUERY_PR + ' ' + INIT_QEXPR + ' | wc -l', \
                           shell=True, stdout=subprocess.PIPE, \
                           stderr=subprocess.STDOUT)

for num in PR_NUMS.stdout.readlines():
    num = num.decode(encoding='utf-8').rstrip('\r\n')

dt = datetime.now() - start_time
ms = (((dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0) / 1000)
qnc_file.write('Q14,'+str(ms)+'\n')

INIT_QEXPR = 'state == "open" & (description ~ "gnats" | environment ~ "gnats" | fix ~ "gnats")'
start_time = datetime.now()
PR_NUMS = subprocess.Popen(QUERY_PR + ' -e \'' + INIT_QEXPR + '\' -f number | wc -l', \
                           shell=True, stdout=subprocess.PIPE, \
                           stderr=subprocess.STDOUT)

for num in PR_NUMS.stdout.readlines():
    num = num.decode(encoding='utf-8').rstrip('\r\n')

dt = datetime.now() - start_time
ms = (((dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0) / 1000)
qnc_file.write('Q11,'+str(ms)+'\n')

start_time = datetime.now()
PR_NUMS = subprocess.Popen("/usr/bin/wget --no-check-certificate -O - 'https://gnatstest:gnats@gnats.juniper.net/web/default/255112' | wc -l", \
                           shell=True, stdout=subprocess.PIPE, \
                           stderr=subprocess.STDOUT)

for num in PR_NUMS.stdout.readlines():
    num = num.decode(encoding='utf-8').rstrip('\r\n')

dt = datetime.now() - start_time
ms = (((dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0) / 1000)
qnc_file.write('Q36,'+str(ms)+'\n')

start_time = datetime.now()
PR_NUMS = subprocess.Popen("/usr/bin/wget --no-check-certificate -O - 'https://gnatstest:gnats@gnats.juniper.net/web/default/do-query?adv=1&expr=%28From%3A%3D%3D%22phil%22+|+From%3A%3D%3D%22phil%40juniper.net%22%29+%26++++++++++++%28!+%28state+%3D%3D+%22suspended%22+|+state+%3D%3D+%22closed%22%29%29&queryname=phil%27s+submitted+PRs&columns=synopsis%2Creported-in%2Csubmitter-id%2Cproduct%2Ccategory%2Cproblem-level%2Cblocker%2Cplanned-release%2Cstate%2Cresponsible%2Coriginator%2Carrival-date&colType=noscoped' | wc -l", \
                           shell=True, stdout=subprocess.PIPE, \
                           stderr=subprocess.STDOUT)

for num in PR_NUMS.stdout.readlines():
    num = num.decode(encoding='utf-8').rstrip('\r\n')

dt = datetime.now() - start_time
ms = (((dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0) / 1000)
qnc_file.write('Q16,'+str(ms)+'\n')

start_time = datetime.now()
PR_NUMS = subprocess.Popen("/usr/bin/wget --no-check-certificate -O - 'https://gnatstest:gnats@gnats.juniper.net/web/default/32621' | wc -l", \
                           shell=True, stdout=subprocess.PIPE, \
                           stderr=subprocess.STDOUT)

for num in PR_NUMS.stdout.readlines():
    num = num.decode(encoding='utf-8').rstrip('\r\n')

dt = datetime.now() - start_time
ms = (((dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0) / 1000)
qnc_file.write('Q15,'+str(ms)+'\n')


