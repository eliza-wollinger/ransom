#!/usr/bin/python3.9

# -*- coding: utf-8 -*-

import os

def discover(initial_path):

    extensions = [
        #'exe', 'dll', 'so', 'rpm', 'deb', 'vnlinuz', 'img',                    # System files
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',                # Image files
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape'  # Audio files
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # Video files
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',                            # Microsoft Office files
        'odt', 'otp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',          # Text files
        'yml', 'yaml', 'json', 'xml', 'csv',                                    # Structured data
        'db', 'sql', 'dbf', 'mdb', 'iso',                                       # Data base
        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',       # Web files
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',                                   # C and C++ files
        'java', 'class', 'jar',                                                 # Java files
        'ps', 'bat', 'vb',                                                      # Windows scripts
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',                               # Unix system scripts
        'go', 'py', 'pyc', 'bf', 'coffee',                                      # Other kind of source codes
        'zip', 'tar', 'tgz', '7z', 'rar', 'bak',                                # Compacted files and backups
    ]

    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path


if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)