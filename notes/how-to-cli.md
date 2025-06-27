## Creating Virtual Environments with venv
You will find authentic documentation at the official web site:
https://docs.python.org/3/library/venv.html


The first step is to create the initial environment:

```bash
$ pwd
/Users/dprasad/teaching/tapmi25/ads5703/virt-env

$ python3 -m venv .

```

Check the contents of the directory:

```bash
$ pwd
/Users/dprasad/teaching/tapmi25/ads5703/virt-env

$ ls -l
total 8
drwxr-xr-x  12 dprasad  staff  384 16 Jun 12:36 bin
drwxr-xr-x   3 dprasad  staff   96 16 Jun 12:36 include
drwxr-xr-x   3 dprasad  staff   96 16 Jun 12:36 lib
-rw-r--r--   1 dprasad  staff  308 16 Jun 12:36 pyvenv.cfg
```

```bash
$  ls -l ./bin/
total 72
-rw-r--r--  1 dprasad  staff  2214 16 Jun 12:36 activate
-rw-r--r--  1 dprasad  staff   945 16 Jun 12:36 activate.csh
-rw-r--r--  1 dprasad  staff  2216 16 Jun 12:36 activate.fish
-rw-r--r--  1 dprasad  staff  9031  8 Apr 19:24 Activate.ps1
-rwxr-xr-x  1 dprasad  staff   268 16 Jun 12:36 pip
-rwxr-xr-x  1 dprasad  staff   268 16 Jun 12:36 pip3
-rwxr-xr-x  1 dprasad  staff   268 16 Jun 12:36 pip3.13
lrwxr-xr-x  1 dprasad  staff    10 16 Jun 12:36 python -> python3.13
lrwxr-xr-x  1 dprasad  staff    10 16 Jun 12:36 python3 -> python3.13
lrwxr-xr-x  1 dprasad  staff    41 16 Jun 12:36 python3.13 -> /usr/local/opt/python@3.13/bin/python3.13
```

Our programs read data files stored in the `data` directory. Therefore, copy `data` here.

```bash
$ cp -rf ../data .
```

We are now all set to install new packages in the new virtual environment.
Activate the environment and install required packages:

```bash
$ pwd
/Users/dprasad/teaching/tapmi25/ads5703/virt-env

$ source ./bin/activate
(virt-env) $

(virt-env) $ pip install --upgrade pip
(virt-env) $ pip3 install pandas openpyxl
(virt-env) $
```



We can execute our programs.

```bash
$ python3 ../src/rbi_bank_tx_stat.py
2025-06-16 13:00:03,883 INFO - Started importing data...
2025-06-16 13:00:03,883 INFO - reading ./data/RTGSNEFTMISMARCH20251A8E4422C463474EBC88BF6BFC026A0B.XLSX
2025-06-16 13:00:26,148 INFO - reading ./data/RTGSNEFTJAN25CD5E02D1321249779606FFE4BADF8439.XLSX
2025-06-16 13:00:26,256 INFO - reading ./data/RTGSNEFTAPRIL2025C5C14916CD804966A715D63CC56A1D24.XLSX
2025-06-16 13:00:26,360 INFO - reading ./data/NEFT122020A5CD3A009E1B45ADAFAA5EF5038476F9.XLSX
2025-06-16 13:00:26,403 WARNING - internet_banking_data: data sheet not foind in './data/NEFT122020A5CD3A009E1B45ADAFAA5EF5038476F9.XLSX'
2025-06-16 13:00:26,445 INFO - Finished!
```
