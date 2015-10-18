#!/usr/bin/env python

import os
import random, string

server = '"server":"172.31.31.224",'
method = '"method":"aes-256-cfb",'
timeout = '"timeout":60'

count = 1
start_port = 1090

password_file_path = os.getcwd() + '/' + 'password_file.txt'

sh_file_path = os.getcwd() + '/' + 'start.sh'
bin_path = '/usr/local/bin/ss-server'
pid_path = '/var/run/shadowsocks-server'

def make_json():
    p_file = open(password_file_path, 'w')
    p_file.write(method + '\n')
    sh_file = open(sh_file_path, 'w')
    sh_file.write('#/bin/bash\n')
    for i in range(count):
        cur_port = start_port + i
        password = random_str(8)
        json_path = os.getcwd() + '/' + str(cur_port) + '.json'
        f = open(json_path, 'w')
        f.write('{\n')
        f.write('        ' + server + '\n')
        f.write('        ' + '"server_port":' + str(cur_port) + ',\n')
        f.write('        ' + '"password":"' + password + '",\n')
        f.write('        ' + method + '\n')
        f.write('        ' + timeout + '\n')
        f.write('}\n')
        f.close()

        p_file.write('port:' + str(cur_port) + '\n' + 'password:' + password + '\n\n')
        sh_file.write(bin_path + ' -u -c ' + json_path + ' -f ' + pid_path + '/' + str(cur_port) + '.pid\n')
    p_file.close()
    sh_file.close()

def random_str(len):
    a = list(string.ascii_letters)
    random.shuffle(a)
    return ''.join(a[:len])
    

if __name__ == '__main__':
    make_json()
