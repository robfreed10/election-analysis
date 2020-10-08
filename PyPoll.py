{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/robfreed/Downloads'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(r'/Users/robfreed/Downloads/election_results.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ballot ID</th>\n",
       "      <th>County</th>\n",
       "      <th>Candidate</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1323913</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1005842</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1880345</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1600337</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1835994</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Ballot ID     County                Candidate\n",
       "0    1323913  Jefferson  Charles Casper Stockham\n",
       "1    1005842  Jefferson  Charles Casper Stockham\n",
       "2    1880345  Jefferson  Charles Casper Stockham\n",
       "3    1600337  Jefferson  Charles Casper Stockham\n",
       "4    1835994  Jefferson  Charles Casper Stockham"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The Data we need to retrieve\n",
    "# Total number of votes cast \n",
    "# A complete list of candidates who received votes\n",
    "# the percentage of votes each candidate won \n",
    "# the total number of votes each candidate won \n",
    "# the winner of the election based on the popular vote\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The time right now is  2020-10-07 16:04:27.920598\n"
     ]
    }
   ],
   "source": [
    "#Import the datetime class from the datetime module\n",
    "import datetime\n",
    "now = datetime.datetime.now()\n",
    "print(\"The time right now is \", now)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The time right now is  2020-10-07 16:07:18.945311\n"
     ]
    }
   ],
   "source": [
    "import datetime as dt\n",
    "now = dt.datetime.now()\n",
    "print(\"The time right now is \", now)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "election_data = open(\"/Users/robfreed/Downloads/election_results.csv\", 'r')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<_io.TextIOWrapper name='/Users/robfreed/Downloads/election_results.csv' mode='r' encoding='UTF-8'>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "election_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "election_data.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_io.TextIOWrapper name='/Users/robfreed/Downloads/election_results.csv' mode='r' encoding='UTF-8'>\n"
     ]
    }
   ],
   "source": [
    "with open(r\"/Users/robfreed/Downloads/election_results.csv\") as election_data:\n",
    "    print(election_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['CLD_CONTINUED',\n",
       " 'CLD_DUMPED',\n",
       " 'CLD_EXITED',\n",
       " 'CLD_TRAPPED',\n",
       " 'DirEntry',\n",
       " 'EX_CANTCREAT',\n",
       " 'EX_CONFIG',\n",
       " 'EX_DATAERR',\n",
       " 'EX_IOERR',\n",
       " 'EX_NOHOST',\n",
       " 'EX_NOINPUT',\n",
       " 'EX_NOPERM',\n",
       " 'EX_NOUSER',\n",
       " 'EX_OK',\n",
       " 'EX_OSERR',\n",
       " 'EX_OSFILE',\n",
       " 'EX_PROTOCOL',\n",
       " 'EX_SOFTWARE',\n",
       " 'EX_TEMPFAIL',\n",
       " 'EX_UNAVAILABLE',\n",
       " 'EX_USAGE',\n",
       " 'F_LOCK',\n",
       " 'F_OK',\n",
       " 'F_TEST',\n",
       " 'F_TLOCK',\n",
       " 'F_ULOCK',\n",
       " 'MutableMapping',\n",
       " 'NGROUPS_MAX',\n",
       " 'O_ACCMODE',\n",
       " 'O_APPEND',\n",
       " 'O_ASYNC',\n",
       " 'O_CLOEXEC',\n",
       " 'O_CREAT',\n",
       " 'O_DIRECTORY',\n",
       " 'O_DSYNC',\n",
       " 'O_EXCL',\n",
       " 'O_EXLOCK',\n",
       " 'O_NDELAY',\n",
       " 'O_NOCTTY',\n",
       " 'O_NOFOLLOW',\n",
       " 'O_NONBLOCK',\n",
       " 'O_RDONLY',\n",
       " 'O_RDWR',\n",
       " 'O_SHLOCK',\n",
       " 'O_SYNC',\n",
       " 'O_TRUNC',\n",
       " 'O_WRONLY',\n",
       " 'PRIO_PGRP',\n",
       " 'PRIO_PROCESS',\n",
       " 'PRIO_USER',\n",
       " 'P_ALL',\n",
       " 'P_NOWAIT',\n",
       " 'P_NOWAITO',\n",
       " 'P_PGID',\n",
       " 'P_PID',\n",
       " 'P_WAIT',\n",
       " 'PathLike',\n",
       " 'RTLD_GLOBAL',\n",
       " 'RTLD_LAZY',\n",
       " 'RTLD_LOCAL',\n",
       " 'RTLD_NODELETE',\n",
       " 'RTLD_NOLOAD',\n",
       " 'RTLD_NOW',\n",
       " 'R_OK',\n",
       " 'SCHED_FIFO',\n",
       " 'SCHED_OTHER',\n",
       " 'SCHED_RR',\n",
       " 'SEEK_CUR',\n",
       " 'SEEK_END',\n",
       " 'SEEK_SET',\n",
       " 'ST_NOSUID',\n",
       " 'ST_RDONLY',\n",
       " 'TMP_MAX',\n",
       " 'WCONTINUED',\n",
       " 'WCOREDUMP',\n",
       " 'WEXITED',\n",
       " 'WEXITSTATUS',\n",
       " 'WIFCONTINUED',\n",
       " 'WIFEXITED',\n",
       " 'WIFSIGNALED',\n",
       " 'WIFSTOPPED',\n",
       " 'WNOHANG',\n",
       " 'WNOWAIT',\n",
       " 'WSTOPPED',\n",
       " 'WSTOPSIG',\n",
       " 'WTERMSIG',\n",
       " 'WUNTRACED',\n",
       " 'W_OK',\n",
       " 'X_OK',\n",
       " '_Environ',\n",
       " '__all__',\n",
       " '__builtins__',\n",
       " '__cached__',\n",
       " '__doc__',\n",
       " '__file__',\n",
       " '__loader__',\n",
       " '__name__',\n",
       " '__package__',\n",
       " '__spec__',\n",
       " '_execvpe',\n",
       " '_exists',\n",
       " '_exit',\n",
       " '_fspath',\n",
       " '_fwalk',\n",
       " '_get_exports_list',\n",
       " '_putenv',\n",
       " '_spawnvef',\n",
       " '_unsetenv',\n",
       " '_wrap_close',\n",
       " 'abc',\n",
       " 'abort',\n",
       " 'access',\n",
       " 'altsep',\n",
       " 'chdir',\n",
       " 'chflags',\n",
       " 'chmod',\n",
       " 'chown',\n",
       " 'chroot',\n",
       " 'close',\n",
       " 'closerange',\n",
       " 'confstr',\n",
       " 'confstr_names',\n",
       " 'cpu_count',\n",
       " 'ctermid',\n",
       " 'curdir',\n",
       " 'defpath',\n",
       " 'device_encoding',\n",
       " 'devnull',\n",
       " 'dup',\n",
       " 'dup2',\n",
       " 'environ',\n",
       " 'environb',\n",
       " 'error',\n",
       " 'execl',\n",
       " 'execle',\n",
       " 'execlp',\n",
       " 'execlpe',\n",
       " 'execv',\n",
       " 'execve',\n",
       " 'execvp',\n",
       " 'execvpe',\n",
       " 'extsep',\n",
       " 'fchdir',\n",
       " 'fchmod',\n",
       " 'fchown',\n",
       " 'fdopen',\n",
       " 'fork',\n",
       " 'forkpty',\n",
       " 'fpathconf',\n",
       " 'fsdecode',\n",
       " 'fsencode',\n",
       " 'fspath',\n",
       " 'fstat',\n",
       " 'fstatvfs',\n",
       " 'fsync',\n",
       " 'ftruncate',\n",
       " 'fwalk',\n",
       " 'get_blocking',\n",
       " 'get_exec_path',\n",
       " 'get_inheritable',\n",
       " 'get_terminal_size',\n",
       " 'getcwd',\n",
       " 'getcwdb',\n",
       " 'getegid',\n",
       " 'getenv',\n",
       " 'getenvb',\n",
       " 'geteuid',\n",
       " 'getgid',\n",
       " 'getgrouplist',\n",
       " 'getgroups',\n",
       " 'getloadavg',\n",
       " 'getlogin',\n",
       " 'getpgid',\n",
       " 'getpgrp',\n",
       " 'getpid',\n",
       " 'getppid',\n",
       " 'getpriority',\n",
       " 'getsid',\n",
       " 'getuid',\n",
       " 'initgroups',\n",
       " 'isatty',\n",
       " 'kill',\n",
       " 'killpg',\n",
       " 'lchflags',\n",
       " 'lchmod',\n",
       " 'lchown',\n",
       " 'linesep',\n",
       " 'link',\n",
       " 'listdir',\n",
       " 'lockf',\n",
       " 'lseek',\n",
       " 'lstat',\n",
       " 'major',\n",
       " 'makedev',\n",
       " 'makedirs',\n",
       " 'minor',\n",
       " 'mkdir',\n",
       " 'mkfifo',\n",
       " 'mknod',\n",
       " 'name',\n",
       " 'nice',\n",
       " 'open',\n",
       " 'openpty',\n",
       " 'pardir',\n",
       " 'path',\n",
       " 'pathconf',\n",
       " 'pathconf_names',\n",
       " 'pathsep',\n",
       " 'pipe',\n",
       " 'popen',\n",
       " 'pread',\n",
       " 'putenv',\n",
       " 'pwrite',\n",
       " 'read',\n",
       " 'readlink',\n",
       " 'readv',\n",
       " 'register_at_fork',\n",
       " 'remove',\n",
       " 'removedirs',\n",
       " 'rename',\n",
       " 'renames',\n",
       " 'replace',\n",
       " 'rmdir',\n",
       " 'scandir',\n",
       " 'sched_get_priority_max',\n",
       " 'sched_get_priority_min',\n",
       " 'sched_yield',\n",
       " 'sendfile',\n",
       " 'sep',\n",
       " 'set_blocking',\n",
       " 'set_inheritable',\n",
       " 'setegid',\n",
       " 'seteuid',\n",
       " 'setgid',\n",
       " 'setgroups',\n",
       " 'setpgid',\n",
       " 'setpgrp',\n",
       " 'setpriority',\n",
       " 'setregid',\n",
       " 'setreuid',\n",
       " 'setsid',\n",
       " 'setuid',\n",
       " 'spawnl',\n",
       " 'spawnle',\n",
       " 'spawnlp',\n",
       " 'spawnlpe',\n",
       " 'spawnv',\n",
       " 'spawnve',\n",
       " 'spawnvp',\n",
       " 'spawnvpe',\n",
       " 'st',\n",
       " 'stat',\n",
       " 'stat_result',\n",
       " 'statvfs',\n",
       " 'statvfs_result',\n",
       " 'strerror',\n",
       " 'supports_bytes_environ',\n",
       " 'supports_dir_fd',\n",
       " 'supports_effective_ids',\n",
       " 'supports_fd',\n",
       " 'supports_follow_symlinks',\n",
       " 'symlink',\n",
       " 'sync',\n",
       " 'sys',\n",
       " 'sysconf',\n",
       " 'sysconf_names',\n",
       " 'system',\n",
       " 'tcgetpgrp',\n",
       " 'tcsetpgrp',\n",
       " 'terminal_size',\n",
       " 'times',\n",
       " 'times_result',\n",
       " 'truncate',\n",
       " 'ttyname',\n",
       " 'umask',\n",
       " 'uname',\n",
       " 'uname_result',\n",
       " 'unlink',\n",
       " 'unsetenv',\n",
       " 'urandom',\n",
       " 'utime',\n",
       " 'wait',\n",
       " 'wait3',\n",
       " 'wait4',\n",
       " 'waitpid',\n",
       " 'walk',\n",
       " 'write',\n",
       " 'writev']"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir(os)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__all__',\n",
       " '__builtins__',\n",
       " '__cached__',\n",
       " '__doc__',\n",
       " '__file__',\n",
       " '__loader__',\n",
       " '__name__',\n",
       " '__package__',\n",
       " '__spec__',\n",
       " '_get_sep',\n",
       " '_joinrealpath',\n",
       " '_varprog',\n",
       " '_varprogb',\n",
       " 'abspath',\n",
       " 'altsep',\n",
       " 'basename',\n",
       " 'commonpath',\n",
       " 'commonprefix',\n",
       " 'curdir',\n",
       " 'defpath',\n",
       " 'devnull',\n",
       " 'dirname',\n",
       " 'exists',\n",
       " 'expanduser',\n",
       " 'expandvars',\n",
       " 'extsep',\n",
       " 'genericpath',\n",
       " 'getatime',\n",
       " 'getctime',\n",
       " 'getmtime',\n",
       " 'getsize',\n",
       " 'isabs',\n",
       " 'isdir',\n",
       " 'isfile',\n",
       " 'islink',\n",
       " 'ismount',\n",
       " 'join',\n",
       " 'lexists',\n",
       " 'normcase',\n",
       " 'normpath',\n",
       " 'os',\n",
       " 'pardir',\n",
       " 'pathsep',\n",
       " 'realpath',\n",
       " 'relpath',\n",
       " 'samefile',\n",
       " 'sameopenfile',\n",
       " 'samestat',\n",
       " 'sep',\n",
       " 'split',\n",
       " 'splitdrive',\n",
       " 'splitext',\n",
       " 'stat',\n",
       " 'supports_unicode_filenames',\n",
       " 'sys']"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir(os.path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_to_load =os.path.join(\"Downloads\", \"election_results.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import os\n",
    "## Assign a variable for the file to load and the path\n",
    "file_to_load = os.path.join(\"Downloads\", \"election_results.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is Robert Freed and I approve this message\n"
     ]
    }
   ],
   "source": [
    "print(\"My name is Robert Freed and I approve this message\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    }
   ],
   "source": [
    "print(\"hello world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Ballot ID     County                Candidate\n",
      "0         1323913  Jefferson  Charles Casper Stockham\n",
      "1         1005842  Jefferson  Charles Casper Stockham\n",
      "2         1880345  Jefferson  Charles Casper Stockham\n",
      "3         1600337  Jefferson  Charles Casper Stockham\n",
      "4         1835994  Jefferson  Charles Casper Stockham\n",
      "...           ...        ...                      ...\n",
      "369706    4714953   Arapahoe     Raymon Anthony Doane\n",
      "369707    4497542   Arapahoe     Raymon Anthony Doane\n",
      "369708    4085849   Arapahoe     Raymon Anthony Doane\n",
      "369709    4592018   Arapahoe     Raymon Anthony Doane\n",
      "369710    4660518   Arapahoe     Raymon Anthony Doane\n",
      "\n",
      "[369711 rows x 3 columns]\n",
      "        Ballot ID     County                Candidate\n",
      "0         1323913  Jefferson  Charles Casper Stockham\n",
      "1         1005842  Jefferson  Charles Casper Stockham\n",
      "2         1880345  Jefferson  Charles Casper Stockham\n",
      "3         1600337  Jefferson  Charles Casper Stockham\n",
      "4         1835994  Jefferson  Charles Casper Stockham\n",
      "...           ...        ...                      ...\n",
      "369706    4714953   Arapahoe     Raymon Anthony Doane\n",
      "369707    4497542   Arapahoe     Raymon Anthony Doane\n",
      "369708    4085849   Arapahoe     Raymon Anthony Doane\n",
      "369709    4592018   Arapahoe     Raymon Anthony Doane\n",
      "369710    4660518   Arapahoe     Raymon Anthony Doane\n",
      "\n",
      "[369711 rows x 3 columns]\n",
      "        Ballot ID     County                Candidate\n",
      "0         1323913  Jefferson  Charles Casper Stockham\n",
      "1         1005842  Jefferson  Charles Casper Stockham\n",
      "2         1880345  Jefferson  Charles Casper Stockham\n",
      "3         1600337  Jefferson  Charles Casper Stockham\n",
      "4         1835994  Jefferson  Charles Casper Stockham\n",
      "...           ...        ...                      ...\n",
      "369706    4714953   Arapahoe     Raymon Anthony Doane\n",
      "369707    4497542   Arapahoe     Raymon Anthony Doane\n",
      "369708    4085849   Arapahoe     Raymon Anthony Doane\n",
      "369709    4592018   Arapahoe     Raymon Anthony Doane\n",
      "369710    4660518   Arapahoe     Raymon Anthony Doane\n",
      "\n",
      "[369711 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "for row in df:\n",
    "    print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_reader = csv.reader(r'/Users/robfreed/Downloads/election_results.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<_csv.reader at 0x10f71ebd0>"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file_reader"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['/']\n",
      "['U']\n",
      "['s']\n",
      "['e']\n",
      "['r']\n",
      "['s']\n",
      "['/']\n",
      "['r']\n",
      "['o']\n",
      "['b']\n",
      "['f']\n",
      "['r']\n",
      "['e']\n",
      "['e']\n",
      "['d']\n",
      "['/']\n",
      "['D']\n",
      "['o']\n",
      "['w']\n",
      "['n']\n",
      "['l']\n",
      "['o']\n",
      "['a']\n",
      "['d']\n",
      "['s']\n",
      "['/']\n",
      "['e']\n",
      "['l']\n",
      "['e']\n",
      "['c']\n",
      "['t']\n",
      "['i']\n",
      "['o']\n",
      "['n']\n",
      "['_']\n",
      "['r']\n",
      "['e']\n",
      "['s']\n",
      "['u']\n",
      "['l']\n",
      "['t']\n",
      "['s']\n",
      "['.']\n",
      "['c']\n",
      "['s']\n",
      "['v']\n"
     ]
    }
   ],
   "source": [
    "for row in file_reader:\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_to_load = os.path.join(\"/Users/robfreed/Downloads\", \"election_results.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_to_save = os.path.join(\"/Users/robfreed/Downloads/analysis\", \"election_analysis.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(file_to_load) as election_data:\n",
    "    file_reader = csv.reader(election_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/robfreed/Downloads/election_results.csv'"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file_to_load"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/robfreed/Downloads/analysis/election_analysis.txt'"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file_to_save"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_io.TextIOWrapper name='/Users/robfreed/Downloads/election_results.csv' mode='r' encoding='UTF-8'>\n"
     ]
    }
   ],
   "source": [
    "with open(r'/Users/robfreed/Downloads/election_results.csv') as election_data:\n",
    "    print(election_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-77-5caed7f0b2f4>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mfile_reader\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "for row in file_reader:\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Ballot ID', 'County', 'Candidate']\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import os\n",
    "# Assign a variable to load a file from a path.\n",
    "file_to_load = os.path.join(\"/Users/robfreed/Downloads\", \"election_results.csv\")\n",
    "# Assign a variable to save the file to a path.\n",
    "file_to_save = os.path.join(\"/Users/robfreed/Downloads/analysis\", \"election_analysis.txt\")\n",
    "\n",
    "# Open the election results and read the file.\n",
    "with open(file_to_load) as election_data:\n",
    "    file_reader = csv.reader(election_data)\n",
    "\n",
    "    # Read and print the header row.\n",
    "    headers = next(file_reader)\n",
    "    print(headers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import os\n",
    "file_to_load = os.path.join(\"/Users/robfreed/Downloads\", \"election_results.csv\")\n",
    "file_to_save = os.path.join(\"/Users/robfreed/Downloads/analysis\", \"election_analysis.txt\")\n",
    "\n",
    "with open(file_to_load) as election_data:\n",
    "    file_reader = csv.reader(election_data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<_csv.reader at 0x10f71e950>"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file_reader"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-87-5caed7f0b2f4>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mfile_reader\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
