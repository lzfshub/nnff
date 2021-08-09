#!/usr/bin/env python
#-*- coding:utf-8 -*-
from parser_args import *
import os
# import cmd_parser as cp

argv = sys.argv[1:]

parser = ArgumentParser(argv=argv)
parser.add_argument('init', help="Init your neutral network file framwork.")
parser.add_argument('-h', '--help', help="Show help.")
parser.add_argument('-v', '--version', help="Show version and exit.")
parser.add_argument('--save-dir <dir>', help="The path where you want to save.")
parser.add_argument('--url <url>', help="Url of neutral network file framwork you want to download.")
total_args, args = parser.parse_args()

# cp.cmd(args)
# help
if __name__ == '__main__':
    if '-h' in args or '--help' in args or total_args == 0:
        help_str = parser.get_help()
        print(help_str)
        sys.exit()
    # version
    if '-v' in args or '--version' in args or total_args == 0:
        print('nnff 0.1')
        sys.exit()
    if 'init' in args:
        if '--url' in args:
            url = args['--url']
        else:
            url = 'https://github.com/lzfshub/nnfileframe.git'
        if '--save-dir' in args:
            dst = args['--save-dir']
        else:
            dst = './'
        os.system(f"git clone {url} {dst}")



'''
pack *.py to *.exe
1. pip install pyinstaller
2. pyinstaller -F nnff.py  -i myico.ico
pack to pypi
python setup.py sdist bdist_wheel
'''