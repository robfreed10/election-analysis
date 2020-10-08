{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The data we need to retrieve\n",
    "# 1. The total number of votes cast\n",
    "# 2. A complete List of candidates who received votes \n",
    "# 3. The percentage of votes each candidate won \n",
    "# 4. The total number of votes each candidate won \n",
    "# 5. Thr winner of the election based on the popular vote\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The time right now is  2020-10-08 13:28:12.063676\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "now = datetime.datetime.now()\n",
    "print(\"The time right now is \", now)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Dialect',\n",
       " 'DictReader',\n",
       " 'DictWriter',\n",
       " 'Error',\n",
       " 'OrderedDict',\n",
       " 'QUOTE_ALL',\n",
       " 'QUOTE_MINIMAL',\n",
       " 'QUOTE_NONE',\n",
       " 'QUOTE_NONNUMERIC',\n",
       " 'Sniffer',\n",
       " 'StringIO',\n",
       " '_Dialect',\n",
       " '__all__',\n",
       " '__builtins__',\n",
       " '__cached__',\n",
       " '__doc__',\n",
       " '__file__',\n",
       " '__loader__',\n",
       " '__name__',\n",
       " '__package__',\n",
       " '__spec__',\n",
       " '__version__',\n",
       " 'excel',\n",
       " 'excel_tab',\n",
       " 'field_size_limit',\n",
       " 'get_dialect',\n",
       " 'list_dialects',\n",
       " 're',\n",
       " 'reader',\n",
       " 'register_dialect',\n",
       " 'unix_dialect',\n",
       " 'unregister_dialect',\n",
       " 'writer']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import csv\n",
    "dir(csv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__class__',\n",
       " '__contains__',\n",
       " '__delattr__',\n",
       " '__delitem__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__getitem__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__iter__',\n",
       " '__le__',\n",
       " '__len__',\n",
       " '__lt__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__setattr__',\n",
       " '__setitem__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " 'clear',\n",
       " 'copy',\n",
       " 'fromkeys',\n",
       " 'get',\n",
       " 'items',\n",
       " 'keys',\n",
       " 'pop',\n",
       " 'popitem',\n",
       " 'setdefault',\n",
       " 'update',\n",
       " 'values']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir({\"Arapahoe\": 422829, \"Denver\": 463353, \"Jefferson\": 432438})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__add__',\n",
       " '__class__',\n",
       " '__contains__',\n",
       " '__delattr__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__getitem__',\n",
       " '__getnewargs__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__iter__',\n",
       " '__le__',\n",
       " '__len__',\n",
       " '__lt__',\n",
       " '__mod__',\n",
       " '__mul__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__rmod__',\n",
       " '__rmul__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " 'capitalize',\n",
       " 'casefold',\n",
       " 'center',\n",
       " 'count',\n",
       " 'encode',\n",
       " 'endswith',\n",
       " 'expandtabs',\n",
       " 'find',\n",
       " 'format',\n",
       " 'format_map',\n",
       " 'index',\n",
       " 'isalnum',\n",
       " 'isalpha',\n",
       " 'isascii',\n",
       " 'isdecimal',\n",
       " 'isdigit',\n",
       " 'isidentifier',\n",
       " 'islower',\n",
       " 'isnumeric',\n",
       " 'isprintable',\n",
       " 'isspace',\n",
       " 'istitle',\n",
       " 'isupper',\n",
       " 'join',\n",
       " 'ljust',\n",
       " 'lower',\n",
       " 'lstrip',\n",
       " 'maketrans',\n",
       " 'partition',\n",
       " 'replace',\n",
       " 'rfind',\n",
       " 'rindex',\n",
       " 'rjust',\n",
       " 'rpartition',\n",
       " 'rsplit',\n",
       " 'rstrip',\n",
       " 'split',\n",
       " 'splitlines',\n",
       " 'startswith',\n",
       " 'strip',\n",
       " 'swapcase',\n",
       " 'title',\n",
       " 'translate',\n",
       " 'upper',\n",
       " 'zfill']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__abs__',\n",
       " '__add__',\n",
       " '__and__',\n",
       " '__bool__',\n",
       " '__ceil__',\n",
       " '__class__',\n",
       " '__delattr__',\n",
       " '__dir__',\n",
       " '__divmod__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__float__',\n",
       " '__floor__',\n",
       " '__floordiv__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__getnewargs__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__index__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__int__',\n",
       " '__invert__',\n",
       " '__le__',\n",
       " '__lshift__',\n",
       " '__lt__',\n",
       " '__mod__',\n",
       " '__mul__',\n",
       " '__ne__',\n",
       " '__neg__',\n",
       " '__new__',\n",
       " '__or__',\n",
       " '__pos__',\n",
       " '__pow__',\n",
       " '__radd__',\n",
       " '__rand__',\n",
       " '__rdivmod__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__rfloordiv__',\n",
       " '__rlshift__',\n",
       " '__rmod__',\n",
       " '__rmul__',\n",
       " '__ror__',\n",
       " '__round__',\n",
       " '__rpow__',\n",
       " '__rrshift__',\n",
       " '__rshift__',\n",
       " '__rsub__',\n",
       " '__rtruediv__',\n",
       " '__rxor__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__sub__',\n",
       " '__subclasshook__',\n",
       " '__truediv__',\n",
       " '__trunc__',\n",
       " '__xor__',\n",
       " 'bit_length',\n",
       " 'conjugate',\n",
       " 'denominator',\n",
       " 'from_bytes',\n",
       " 'imag',\n",
       " 'numerator',\n",
       " 'real',\n",
       " 'to_bytes']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_to_load = (\"/Users/robfreed/Desktop/Resources/election_results.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "election_data = open(file_to_load, 'r')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<_io.TextIOWrapper name='/Users/robfreed/Desktop/Resources/election_results.csv' mode='r' encoding='UTF-8'>"
      ]
     },
     "execution_count": 18,
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
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "election_data.close()"
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
      "<_io.TextIOWrapper name='/Users/robfreed/Desktop/Resources/election_results.csv' mode='r' encoding='UTF-8'>\n"
     ]
    }
   ],
   "source": [
    "with open(file_to_load) as election_data:\n",
    "    print(election_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
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
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "dir(os)"
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
     "execution_count": 22,
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
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_io.TextIOWrapper name='/Users/robfreed/Desktop/Resources/election_results.csv' mode='r' encoding='UTF-8'>\n"
     ]
    }
   ],
   "source": [
    "import csv \n",
    "import os\n",
    "## Assign a variable for the file to load and the path. \n",
    "file_to_load = os.path.join(\"/Users/robfreed/Desktop/Resources\", \"election_results.csv\")\n",
    "\n",
    "#Open the election results and read the file\n",
    "with open(file_to_load) as election_data:\n",
    "    print(election_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<_io.TextIOWrapper name='/Users/robfreed/Desktop/Analysis/election_analysis.txt' mode='w' encoding='UTF-8'>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a filename variable to a direct or indirect path to the file\n",
    "file_to_save = os.path.join(\"/Users/robfreed/Desktop/Analysis\", \"election_analysis.txt\")\n",
    "# Using the open() function with the 'w' mode we will write data to the file\n",
    "open(file_to_save, 'w')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "outfile = open(file_to_save, 'w')\n",
    "##Write some data to the file\n",
    "outfile.write(\"Hello World\")\n",
    "outfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_to_save = os.path.join(\"/Users/robfreed/Desktop/Analysis\", \"election_analysis.txt\")\n",
    "# Using the with statement open the file as a text file\n",
    "with open(file_to_save, 'w') as txt_file:\n",
    "    #write some data to the file\n",
    "    txt_file.write(\"Arapahoe, \")\n",
    "    txt_file.write(\"Denver, \")\n",
    "    txt_file.write(\"Jefferson, \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "run the txt code, then click on the election_analysis.txt file to see the text\n"
     ]
    }
   ],
   "source": [
    "print(\"run the txt code, then click on the election_analysis.txt file to see the text\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_to_save = os.path.join(\"/Users/robfreed/Desktop/Analysis\", \"election_analysis.txt\")\n",
    "with open(file_to_save, 'w') as txt_file:\n",
    "    txt_file.write(\"Counties in the Election\\n-----------------\\nArapahoe\\nDenver\\nJefferson\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
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
    "#Assign a variable to load a file from a path \n",
    "file_to_load = os.path.join(\"/Users/robfreed/Desktop/Resources\", \"election_results.csv\")\n",
    "#Assign a variable to save the file to a path\n",
    "file_to_save = os.path.join(\"/Users/robfreed/Desktop/Analysis\", \"election_analysis.txt\")\n",
    "#Open the election results and read the file\n",
    "with open(file_to_load) as election_data:\n",
    "    file_reader = csv.reader(election_data)\n",
    "    \n",
    "    headers = next(file_reader)\n",
    "    print(headers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "### for above code right under file_reader to print each row ins the CSV File\n",
    "### for row in file_reader:\n",
    "###     print(row)"
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
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World\")"
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
      "Charles Casper Stockham: 23.0% (85,213)\n",
      "\n",
      "Diana DeGette: 73.8% (272,892)\n",
      "\n",
      "Raymon Anthony Doane: 3.1% (11,606)\n",
      "\n",
      "-------------------\n",
      "Winner: Diana DeGette\n",
      "Winning Vote Count: 272,892\n",
      "Winning Percentage: 73.8%\n",
      "-------------------\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import os\n",
    "file_to_load = os.path.join(\"/Users/robfreed/Desktop/Resources\", \"election_results.csv\")\n",
    "file_to_save = os.path.join(\"/Users/robfreed/Desktop/Analysis\", \"election_analysis.txt\")\n",
    "# 1. Inititalize a total vote counter\n",
    "total_votes = 0\n",
    "# Candidate Options\n",
    "candidate_options = []\n",
    "# Declare the empty dictionary\n",
    "candidate_votes = {}\n",
    "#Winning Candidate and Winning Count Tracker\n",
    "winning_candidate = \"\"\n",
    "winning_count = 0\n",
    "winning_percentage = 0\n",
    "#Open the election results and read the file\n",
    "with open(file_to_load) as election_data:\n",
    "    file_reader = csv.reader(election_data)\n",
    "    headers = next(file_reader)\n",
    "    for row in file_reader:\n",
    "        ### same as total_votes = total_votes + 1\n",
    "        total_votes += 1\n",
    "        ### Print the candidate name from each row\n",
    "        candidate_name = row[2]\n",
    "        ### If the candidate does not match any existing candidate....\n",
    "        if candidate_name not in candidate_options:\n",
    "            ### Add it to the list of candidates\n",
    "            candidate_options.append(candidate_name)\n",
    "            \n",
    "            #Begin tracking that candidate's vote count\n",
    "            candidate_votes[candidate_name] = 0\n",
    "            # Add a vote to that candidate's count out of the if statement\n",
    "        candidate_votes[candidate_name] += 1\n",
    "    # 1. Iterate through the candidate list\n",
    "    for candidate_name in candidate_votes:\n",
    "        # 2. Retrieve vote count of a candidate.\n",
    "        votes = candidate_votes[candidate_name]\n",
    "        # 3. Calculate the percentage of votes\n",
    "        vote_percentage = float(votes) / float(total_votes) * 100\n",
    "        \n",
    "        # Print out each candidates name, vote count, and percentage of votes to terminal \n",
    "        print(f\"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\\n\")\n",
    "        \n",
    "  \n",
    "        \n",
    "        if (votes > winning_count) and (vote_percentage > winning_percentage):\n",
    "            # If true then set winning_count = votes and winning_percentage = vote_percentage\n",
    "            winning_count = votes\n",
    "            winning_percentage = vote_percentage\n",
    "            # And, set the winning_candidate equal to the candidate's name\n",
    "            winning_candidate = candidate_name\n",
    "    \n",
    "    winning_candidate_summary = (\n",
    "        f\"-------------------\\n\"\n",
    "        f\"Winner: {winning_candidate}\\n\"\n",
    "        f\"Winning Vote Count: {winning_count:,}\\n\"\n",
    "        f\"Winning Percentage: {winning_percentage:.1f}%\\n\"\n",
    "        f\"-------------------\\n\")\n",
    "    print(winning_candidate_summary)\n",
    "            \n",
    "        # 4. Print the candidate name and the percentage of votes\n",
    "        # print(f\"{candidate_name}: received {vote_percentage}% of the vote. \")\n",
    "            \n",
    "### wont print every name for each time it is found in CSV, just once \n",
    "# print(candidate_votes)\n",
    "    "
   ]
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
