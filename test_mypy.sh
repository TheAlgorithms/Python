#!/bin/bash

python --version

mypy_test() {

    serverIp=""
    serverPassword=""

    pip install mypy
    python3 typecheck.py

    # Upload cache
    sudo apt-get update
    sudo apt-get install -y sshpass
    ssh-keyscan $serverIp >> ~/.ssh/known_hosts
    #TODO: The location of cache subject to change (with python version)
    sshpass -p $serverPassword scp ./.mypy_cache/3.7/cache.db root@$serverIp:~/mypy_cache_db

}

mypy_test
