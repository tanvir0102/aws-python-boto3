#!/usr/bin/env python

#uderstanding the fabric module functionality
def hello():
 print("Hello, You are welcome to automation")

#executing the command on the local machine
from fabric.api import local
def uptime():
 local('uptime')

#executing the command on the remote machine
from fabric.api import env, run
env.hosts = ['192.168.0.28','192.168.0.29']

def echo():
 run("echo -n 'Hello, you are tuned for automation'")

def deploy_lamp():
 run("yum install httpd mariadb-server php php-mysql -y")

def uptime_remote():
 run('uptime')

def disk_space():
 run('df -kh')

def kernel_version():
 run('uname -a')
