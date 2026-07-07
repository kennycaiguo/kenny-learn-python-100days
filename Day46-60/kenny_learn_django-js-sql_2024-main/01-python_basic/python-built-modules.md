
## python built-in modules


```python
# to see the python built-in modules
help('modules')
```


    Please wait a moment while I gather a list of all available modules...


​    

    D:\programs\python3.6_opencv\Python36X64\lib\site-packages\IPython\kernel\__init__.py:13: ShimWarning: The `IPython.kernel` package has been deprecated since IPython 4.0.You should import from ipykernel or jupyter_client instead.
      "You should import from ipykernel or jupyter_client instead.", ShimWarning)
    D:\programs\python3.6_opencv\Python36X64\lib\site-packages\OpenSSL\_util.py:6: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography. The next release of cryptography will remove support for Python 3.6.
      from cryptography.hazmat.bindings.openssl.binding import Binding
    D:\programs\python3.6_opencv\Python36X64\lib\pkgutil.py:92: MatplotlibDeprecationWarning: 
    The matplotlib.compat module was deprecated in Matplotlib 3.3 and will be removed two minor releases later.
      __import__(info.name)


    pygame 2.1.2 (SDL 2.0.18, Python 3.6.3)
    Hello from the pygame community. https://www.pygame.org/contribute.html


    D:\programs\python3.6_opencv\Python36X64\lib\pkgutil.py:107: VisibleDeprecationWarning: zmq.eventloop.minitornado is deprecated in pyzmq 14.0 and will be removed.
        Install tornado itself to use zmq with the tornado IOLoop.
        
      yield from walk_packages(path, info.name+'.', onerror)


    IPython             colorsys            mistune             storemagic
    OpenSSL             comm                mmap                string
    PIL                 commctrl            mmapfile            stringprep
    __future__          compileall          mmsystem            struct
    _argon2_cffi_bindings concurrent          modulefinder        subprocess
    _ast                configparser        mouse               sunau
    _asyncio            constantly          msilib              symbol
    _bisect             contextlib          msvcrt              sympyprinting
    _blake2             contextvars         multiprocessing     symtable
    _bootlocale         copy                nbclassic           sys
    _bz2                copyreg             nbclient            sysconfig
    _cffi_backend       crypt               nbconvert           tabnanny
    _codecs             cryptography        nbformat            tarfile
    _codecs_cn          cssselect           nest_asyncio        telnetlib
    _codecs_hk          csv                 netbios             tempfile
    _codecs_iso2022     ctypes              netrc               tensorboard
    _codecs_jp          curses              nntplib             tensorboard_data_server
    _codecs_kr          cv2                 notebook            tensorboard_plugin_wit
    _codecs_tw          cycler              nt                  tensorflow
    _collections        cythonmagic         ntpath              tensorflow_estimator
    _collections_abc    dataclasses         ntsecuritycon       termcolor
    _compat_pickle      datetime            nturl2path          terminado
    _compression        dateutil            numbers             test
    _csv                dbi                 numpy               testpath
    _ctypes             dbm                 oauthlib            tests
    _ctypes_test        dde                 odbc                textwrap
    _datetime           decimal             opcode              this
    _decimal            decorator           openpyxl            threading
    _distutils_hack     defusedxml          operator            threadpoolctl
    _dummy_thread       difflib             opt_einsum          tifffile
    _elementtree        dis                 optparse            time
    _findvs             distutils           os                  timeit
    _functools          dns                 packaging           timer
    _hashlib            doctest             pandas              tkinter
    _heapq              dummy_threading     pandocfilters       tldextract
    _imp                email               parsel              token
    _io                 encodings           parser              tokenize
    _json               engineio            parso               tornado
    _locale             ensurepip           pasta               trace
    _lsprof             entrypoints         pathlib             traceback
    _lzma               enum                pdb                 tracemalloc
    _markupbase         errno               perfmon             traitlets
    _md5                et_xmlfile          pickle              tty
    _msi                eventlet            pickleshare         turtle
    _multibytecodec     fake_useragent      pickletools         turtledemo
    _multiprocessing    faulthandler        pip                 twisted
    _opcode             filecmp             pipes               types
    _operator           fileinput           pkg_resources       typing
    _osx_support        filelock            pkgutil             typing_extensions
    _overlapped         flask               platform            unicodedata
    _pickle             flask_socketio      plistlib            unittest
    _pydecimal          flatbuffers         poplib              urllib
    _pyio               fnmatch             posixpath           urllib3
    _pyrsistent_version formatter           pprint              uu
    _random             fractions           profile             uuid
    _sha1               ftplib              prometheus_client   venv
    _sha256             functools           prompt_toolkit      w3lib
    _sha3               gast                protego             warnings
    _sha512             gc                  pstats              wave
    _signal             genericpath         pty                 wcwidth
    _sitebuiltins       getopt              pvectorc            weakref
    _socket             getpass             py_compile          webbrowser
    _sqlite3            gettext             pyasn1              webencodings
    _sre                glob                pyasn1_modules      websocket
    _ssl                google_auth_oauthlib pyclbr              werkzeug
    _stat               greenlet            pycparser           wheel
    _string             gridfs              pydispatch          widgetsnbextension
    _strptime           grpc                pydoc               win2kras
    _struct             gzip                pydoc_data          win32api
    _symtable           h11                 pyexpat             win32clipboard
    _testbuffer         h5py                pygame              win32com
    _testcapi           hashlib             pygments            win32con
    _testconsole        heapq               pylab               win32console
    _testimportmultiple hmac                pymongo             win32cred
    _testmultiphase     html                pymysql             win32crypt
    _thread             http                pynput              win32cryptcon
    _threading_local    hyperlink           pyparsing           win32event
    _tkinter            idlelib             pyquery             win32evtlog
    _tracemalloc        idna                pyrsistent          win32evtlogutil
    _warnings           imageio             pythoncom           win32file
    _weakref            imaplib             pytz                win32gui
    _weakrefset         imghdr              pywin               win32gui_struct
    _win32sysloader     immutables          pywin32_bootstrap   win32help
    _winapi             imp                 pywin32_testutil    win32inet
    _winxptheme         importlib           pywintypes          win32inetcon
    abc                 importlib_metadata  qtpy                win32job
    absl                importlib_resources queue               win32lz
    adodbapi            incremental         queuelib            win32net
    afxres              inspect             quopri              win32netcon
    aifc                install             random              win32pdh
    antigravity         io                  rasutil             win32pdhquery
    anyio               ipaddress           re                  win32pdhutil
    argon2              ipykernel           regcheck            win32pipe
    argparse            ipykernel_launcher  regutil             win32print
    array               ipython_genutils    reprlib             win32process
    ast                 ipywidgets          requests            win32profile
    astunparse          isapi               requests_file       win32ras
    async_generator     itemadapter         requests_oauthlib   win32rcparser
    asynchat            itemloaders         rlcompleter         win32security
    asyncio             iteration_utilities rmagic              win32service
    asyncore            itertools           rsa                 win32serviceutil
    atexit              itsdangerous        runpy               win32timezone
    attr                jedi                sched               win32trace
    attrs               jieba               scipy               win32traceutil
    audioop             jinja2              scrapy              win32transaction
    automat             jmespath            secrets             win32ts
    autoreload          joblib              select              win32ui
    babel               json                selectors           win32uiole
    backcall            json5               send2trash          win32verstamp
    base64              jsonschema          service_identity    win32wnet
    bdb                 jupyter             servicemanager      winerror
    bidict              jupyter_client      setuptools          winioctlcon
    binascii            jupyter_console     shelve              winnt
    binhex              jupyter_core        shiboken2           winperf
    bisect              jupyter_server      shlex               winpty
    bleach              jupyterlab          shutil              winreg
    bs4                 jupyterlab_pygments signal              winsound
    bson                jupyterlab_server   simple_websocket    winxpgui
    builtins            jupyterlab_widgets  site                winxptheme
    bz2                 keras               six                 wordcloud
    cProfile            keras_preprocessing sklearn             wrapt
    cached_property     keyword             smtpd               wsgiref
    cachetools          kiwisolver          smtplib             wsproto
    calendar            lib2to3             sndhdr              xdrlib
    certifi             linecache           sniffio             xlrd
    cffi                locale              socket              xlutils
    cgi                 logging             socketio            xlwings
    cgitb               lxml                socketserver        xlwt
    charset_normalizer  lzma                soupsieve           xml
    chunk               macpath             sqlalchemy          xmlrpc
    clang               macurl2path         sqlite3             xxsubtype
    click               mailbox             sre_compile         zipapp
    cmath               mailcap             sre_constants       zipfile
    cmd                 markdown            sre_parse           zipimport
    code                markupsafe          ssl                 zipp
    codecs              marshal             sspi                zlib
    codeop              math                sspicon             zmq
    collections         matplotlib          stat                
    colorama            mimetypes           statistics          
    
    Enter any module name to get more help.  Or, type "modules spam" to search
    for modules whose name or summary contain the string "spam".


​    


```python
# 1.json
import json

data = {
    "name": "Kenny",
    "age": 30,
    "is_student": "yes",
    "is_boss": "yes",
    "courses": ["Game dev", "nodejs", "js", "3d modeling"]
}

json_str = json.dumps(data, indent=4)
print(json_str)
```

    {
        "name": "Kenny",
        "age": 30,
        "is_student": "yes",
        "is_boss": "yes",
        "courses": [
            "Game dev",
            "nodejs",
            "js",
            "3d modeling"
        ]
    }



```python
# 2.tkinter
import tkinter as tk


def on_btn_click():
    label.config(text="Hello,Guys")


root = tk.Tk()
root.title("tkinter Sample")
label = tk.Label(root, text="click button to see result")
label.pack(pady=40)
button = tk.Button(root, text="click me", command=on_btn_click)
button.pack(pady=40)
root.mainloop()
```


```python
# 3.random
import random as rnd

rnd_int = rnd.randint(0, 100)
print(f"a random integer from 1-100 is {rnd_int}")
langs = ["Python", "Cpp", "Golang", "js"]
rnd_lang = rnd.choice(langs)
print(f"random chosen language is: {rnd_lang}")
```

    a random integer from 1-100 is 5
    random chosen language is: Cpp



```python
# 4.math
import math

pai = math.pi
radius = 10
area = pai * radius ** 2
print(f"a circle with the radius: {radius},will has a area of:{area}")
```

    a circle with the radius: 10,will has a area of:314.1592653589793



```python
# 5.pathlib
from pathlib import Path

# dir = Path("..")
# dirs = [x for x in dir.iterdir() if x.is_dir()]
# for d in dirs:
#     print(d)
dir = Path(".")
dirs = [x for x in dir.iterdir()]
for d in dirs:
    print(d)    
```

    .ipynb_checkpoints
    data.db
    data.db-journal
    data.xlsx
    demo.txt
    gfg.xlsx
    gfg2.xlsx
    gfgm.xlsx
    hello.txt
    jl.cmd
    python-study-live1.ipynb
    python-study-live2.ipynb
    Python-study-live3.ipynb
    Python-study-live4.ipynb
    Python-study-live5.ipynb
    test.txt
    wc.txt



```python
# 6.os.path
import os
# out = os.path.basename("/baz/foo")
# print(out)

# out = os.path.dirname("/baz/foo")
# print(out)

# out = os.path.isabs("/baz/foo")
# print(out)

out = os.path.isdir("C:\\Users")
print(out)

out = os.path.isfile("data.db")
print(out)
```

    True
    True



```python
# The "datetime" module allows for manipulation and reading of date and time values.
# Some of the basic method of "datetime" module are "datetime.date", "datetime.time", "datetime.datetime", and "datetime.timedelta".
import datetime
date_today = datetime.date.today()
time_now = datetime.datetime.now().time()
print(date_today)
print(time_now)

```

    2025-06-30
    07:17:38.121549



```python
# The "sys" module in Python provides functions and variables that interact with the Python runtime environment.
# It allows developers to access Python interpreter attributes and manipulate them. 
# It offers a range of other functionalities, such as input/output stream access, memory info access, and more.
import sys
print("Python version:", sys.version)
print("Command line arguments:", sys.argv)


```

    Python version: 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)]
    Command line arguments: ['D:\\programs\\python3.6_opencv\\Python36X64\\lib\\site-packages\\ipykernel_launcher.py', '-f', 'C:\\Users\\kenny\\AppData\\Roaming\\jupyter\\runtime\\kernel-7f70f331-f78e-425d-b7ac-23aac0b3054e.json']



```python
# The re module in Python provides support for working with regular expressions. 
# Regular expressions (often abbreviated as "regex") are powerful tools for matching strings 
# or sets of strings using a specialized syntax that allows for flexible pattern matching.
import re
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"

text = "Contact us at info@example.com and support@example.org for more details."
match = re.search(pattern, text)
if match:
    print("First found email:", match.group())

emails = re.findall(pattern, text)
print("All found emails:", emails)

```

    First found email: info@example.com
    All found emails: ['info@example.com', 'support@example.org']



```python
# The "hashlib" module in Python provides algorithms for message digests or hashing. 
# It allows for data integrity checks using algorithms like SHA-256, MD5, and more.
import hashlib
message = "python"
hashed = hashlib.sha256(message.encode()).hexdigest()
print(hashed)

```

    11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1



```python
# The calendar module allows operations and manipulations related to calendars.
import calendar
# cal_may = calendar.month(2025, 5) # show one month
# print(cal_may)
# last_year = calendar.calendar(2024) # show the whole year 
# print(last_year)
help('calendar')
```

    Help on module calendar:
    
    NAME
        calendar - Calendar printing functions
    
    DESCRIPTION
        Note when comparing these calendars to the ones printed by cal(1): By
        default, these calendars have Monday as the first day of the week, and
        Sunday as the last (the European convention). Use setfirstweekday() to
        set the first day of the week (0=Monday, 6=Sunday).
    
    CLASSES
        builtins.ValueError(builtins.Exception)
            IllegalMonthError
            IllegalWeekdayError
        builtins.object
            Calendar
                HTMLCalendar
                    LocaleHTMLCalendar
                TextCalendar
                    LocaleTextCalendar
        
        class Calendar(builtins.object)
         |  Base calendar class. This class doesn't do any formatting. It simply
         |  provides data to subclasses.
         |  
         |  Methods defined here:
         |  
         |  __init__(self, firstweekday=0)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  getfirstweekday(self)
         |  
         |  itermonthdates(self, year, month)
         |      Return an iterator for one month. The iterator will yield datetime.date
         |      values and will always iterate through complete weeks, so it will yield
         |      dates outside the specified month.
         |  
         |  itermonthdays(self, year, month)
         |      Like itermonthdates(), but will yield day numbers. For days outside
         |      the specified month the day number is 0.
         |  
         |  itermonthdays2(self, year, month)
         |      Like itermonthdates(), but will yield (day number, weekday number)
         |      tuples. For days outside the specified month the day number is 0.
         |  
         |  iterweekdays(self)
         |      Return an iterator for one week of weekday numbers starting with the
         |      configured first one.
         |  
         |  monthdatescalendar(self, year, month)
         |      Return a matrix (list of lists) representing a month's calendar.
         |      Each row represents a week; week entries are datetime.date values.
         |  
         |  monthdays2calendar(self, year, month)
         |      Return a matrix representing a month's calendar.
         |      Each row represents a week; week entries are
         |      (day number, weekday number) tuples. Day numbers outside this month
         |      are zero.
         |  
         |  monthdayscalendar(self, year, month)
         |      Return a matrix representing a month's calendar.
         |      Each row represents a week; days outside this month are zero.
         |  
         |  setfirstweekday(self, firstweekday)
         |  
         |  yeardatescalendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting. The return
         |      value is a list of month rows. Each month row contains up to width months.
         |      Each month contains between 4 and 6 weeks and each week contains 1-7
         |      days. Days are datetime.date objects.
         |  
         |  yeardays2calendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting (similar to
         |      yeardatescalendar()). Entries in the week lists are
         |      (day number, weekday number) tuples. Day numbers outside this month are
         |      zero.
         |  
         |  yeardayscalendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting (similar to
         |      yeardatescalendar()). Entries in the week lists are day numbers.
         |      Day numbers outside this month are zero.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  firstweekday
        
        class HTMLCalendar(Calendar)
         |  This calendar returns complete HTML pages.
         |  
         |  Method resolution order:
         |      HTMLCalendar
         |      Calendar
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  formatday(self, day, weekday)
         |      Return a day as a table cell.
         |  
         |  formatmonth(self, theyear, themonth, withyear=True)
         |      Return a formatted month as a table.
         |  
         |  formatmonthname(self, theyear, themonth, withyear=True)
         |      Return a month name as a table row.
         |  
         |  formatweek(self, theweek)
         |      Return a complete week as a table row.
         |  
         |  formatweekday(self, day)
         |      Return a weekday name as a table header.
         |  
         |  formatweekheader(self)
         |      Return a header for a week as a table row.
         |  
         |  formatyear(self, theyear, width=3)
         |      Return a formatted year as a table of tables.
         |  
         |  formatyearpage(self, theyear, width=3, css='calendar.css', encoding=None)
         |      Return a formatted year as a complete HTML page.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  cssclasses = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from Calendar:
         |  
         |  __init__(self, firstweekday=0)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  getfirstweekday(self)
         |  
         |  itermonthdates(self, year, month)
         |      Return an iterator for one month. The iterator will yield datetime.date
         |      values and will always iterate through complete weeks, so it will yield
         |      dates outside the specified month.
         |  
         |  itermonthdays(self, year, month)
         |      Like itermonthdates(), but will yield day numbers. For days outside
         |      the specified month the day number is 0.
         |  
         |  itermonthdays2(self, year, month)
         |      Like itermonthdates(), but will yield (day number, weekday number)
         |      tuples. For days outside the specified month the day number is 0.
         |  
         |  iterweekdays(self)
         |      Return an iterator for one week of weekday numbers starting with the
         |      configured first one.
         |  
         |  monthdatescalendar(self, year, month)
         |      Return a matrix (list of lists) representing a month's calendar.
         |      Each row represents a week; week entries are datetime.date values.
         |  
         |  monthdays2calendar(self, year, month)
         |      Return a matrix representing a month's calendar.
         |      Each row represents a week; week entries are
         |      (day number, weekday number) tuples. Day numbers outside this month
         |      are zero.
         |  
         |  monthdayscalendar(self, year, month)
         |      Return a matrix representing a month's calendar.
         |      Each row represents a week; days outside this month are zero.
         |  
         |  setfirstweekday(self, firstweekday)
         |  
         |  yeardatescalendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting. The return
         |      value is a list of month rows. Each month row contains up to width months.
         |      Each month contains between 4 and 6 weeks and each week contains 1-7
         |      days. Days are datetime.date objects.
         |  
         |  yeardays2calendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting (similar to
         |      yeardatescalendar()). Entries in the week lists are
         |      (day number, weekday number) tuples. Day numbers outside this month are
         |      zero.
         |  
         |  yeardayscalendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting (similar to
         |      yeardatescalendar()). Entries in the week lists are day numbers.
         |      Day numbers outside this month are zero.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from Calendar:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  firstweekday
        
        class IllegalMonthError(builtins.ValueError)
         |  Inappropriate argument value (of correct type).
         |  
         |  Method resolution order:
         |      IllegalMonthError
         |      builtins.ValueError
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __init__(self, month)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __str__(self)
         |      Return str(self).
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.ValueError:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.BaseException:
         |  
         |  __delattr__(self, name, /)
         |      Implement delattr(self, name).
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __reduce__(...)
         |      helper for pickle
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __setattr__(self, name, value, /)
         |      Implement setattr(self, name, value).
         |  
         |  __setstate__(...)
         |  
         |  with_traceback(...)
         |      Exception.with_traceback(tb) --
         |      set self.__traceback__ to tb and return self.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from builtins.BaseException:
         |  
         |  __cause__
         |      exception cause
         |  
         |  __context__
         |      exception context
         |  
         |  __dict__
         |  
         |  __suppress_context__
         |  
         |  __traceback__
         |  
         |  args
        
        class IllegalWeekdayError(builtins.ValueError)
         |  Inappropriate argument value (of correct type).
         |  
         |  Method resolution order:
         |      IllegalWeekdayError
         |      builtins.ValueError
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __init__(self, weekday)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __str__(self)
         |      Return str(self).
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.ValueError:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.BaseException:
         |  
         |  __delattr__(self, name, /)
         |      Implement delattr(self, name).
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __reduce__(...)
         |      helper for pickle
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __setattr__(self, name, value, /)
         |      Implement setattr(self, name, value).
         |  
         |  __setstate__(...)
         |  
         |  with_traceback(...)
         |      Exception.with_traceback(tb) --
         |      set self.__traceback__ to tb and return self.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from builtins.BaseException:
         |  
         |  __cause__
         |      exception cause
         |  
         |  __context__
         |      exception context
         |  
         |  __dict__
         |  
         |  __suppress_context__
         |  
         |  __traceback__
         |  
         |  args
        
        class LocaleHTMLCalendar(HTMLCalendar)
         |  This class can be passed a locale name in the constructor and will return
         |  month and weekday names in the specified locale. If this locale includes
         |  an encoding all strings containing month and weekday names will be returned
         |  as unicode.
         |  
         |  Method resolution order:
         |      LocaleHTMLCalendar
         |      HTMLCalendar
         |      Calendar
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __init__(self, firstweekday=0, locale=None)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  formatmonthname(self, theyear, themonth, withyear=True)
         |      Return a month name as a table row.
         |  
         |  formatweekday(self, day)
         |      Return a weekday name as a table header.
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from HTMLCalendar:
         |  
         |  formatday(self, day, weekday)
         |      Return a day as a table cell.
         |  
         |  formatmonth(self, theyear, themonth, withyear=True)
         |      Return a formatted month as a table.
         |  
         |  formatweek(self, theweek)
         |      Return a complete week as a table row.
         |  
         |  formatweekheader(self)
         |      Return a header for a week as a table row.
         |  
         |  formatyear(self, theyear, width=3)
         |      Return a formatted year as a table of tables.
         |  
         |  formatyearpage(self, theyear, width=3, css='calendar.css', encoding=None)
         |      Return a formatted year as a complete HTML page.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from HTMLCalendar:
         |  
         |  cssclasses = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from Calendar:
         |  
         |  getfirstweekday(self)
         |  
         |  itermonthdates(self, year, month)
         |      Return an iterator for one month. The iterator will yield datetime.date
         |      values and will always iterate through complete weeks, so it will yield
         |      dates outside the specified month.
         |  
         |  itermonthdays(self, year, month)
         |      Like itermonthdates(), but will yield day numbers. For days outside
         |      the specified month the day number is 0.
         |  
         |  itermonthdays2(self, year, month)
         |      Like itermonthdates(), but will yield (day number, weekday number)
         |      tuples. For days outside the specified month the day number is 0.
         |  
         |  iterweekdays(self)
         |      Return an iterator for one week of weekday numbers starting with the
         |      configured first one.
         |  
         |  monthdatescalendar(self, year, month)
         |      Return a matrix (list of lists) representing a month's calendar.
         |      Each row represents a week; week entries are datetime.date values.
         |  
         |  monthdays2calendar(self, year, month)
         |      Return a matrix representing a month's calendar.
         |      Each row represents a week; week entries are
         |      (day number, weekday number) tuples. Day numbers outside this month
         |      are zero.
         |  
         |  monthdayscalendar(self, year, month)
         |      Return a matrix representing a month's calendar.
         |      Each row represents a week; days outside this month are zero.
         |  
         |  setfirstweekday(self, firstweekday)
         |  
         |  yeardatescalendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting. The return
         |      value is a list of month rows. Each month row contains up to width months.
         |      Each month contains between 4 and 6 weeks and each week contains 1-7
         |      days. Days are datetime.date objects.
         |  
         |  yeardays2calendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting (similar to
         |      yeardatescalendar()). Entries in the week lists are
         |      (day number, weekday number) tuples. Day numbers outside this month are
         |      zero.
         |  
         |  yeardayscalendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting (similar to
         |      yeardatescalendar()). Entries in the week lists are day numbers.
         |      Day numbers outside this month are zero.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from Calendar:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  firstweekday
        
        class LocaleTextCalendar(TextCalendar)
         |  This class can be passed a locale name in the constructor and will return
         |  month and weekday names in the specified locale. If this locale includes
         |  an encoding all strings containing month and weekday names will be returned
         |  as unicode.
         |  
         |  Method resolution order:
         |      LocaleTextCalendar
         |      TextCalendar
         |      Calendar
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __init__(self, firstweekday=0, locale=None)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  formatmonthname(self, theyear, themonth, width, withyear=True)
         |      Return a formatted month name.
         |  
         |  formatweekday(self, day, width)
         |      Returns a formatted week day name.
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from TextCalendar:
         |  
         |  formatday(self, day, weekday, width)
         |      Returns a formatted day.
         |  
         |  formatmonth(self, theyear, themonth, w=0, l=0)
         |      Return a month's calendar string (multi-line).
         |  
         |  formatweek(self, theweek, width)
         |      Returns a single week in a string (no newline).
         |  
         |  formatweekheader(self, width)
         |      Return a header for a week.
         |  
         |  formatyear(self, theyear, w=2, l=1, c=6, m=3)
         |      Returns a year's calendar as a multi-line string.
         |  
         |  prmonth(self, theyear, themonth, w=0, l=0)
         |      Print a month's calendar.
         |  
         |  prweek(self, theweek, width)
         |      Print a single week (no newline).
         |  
         |  pryear(self, theyear, w=0, l=0, c=6, m=3)
         |      Print a year's calendar.
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from Calendar:
         |  
         |  getfirstweekday(self)
         |  
         |  itermonthdates(self, year, month)
         |      Return an iterator for one month. The iterator will yield datetime.date
         |      values and will always iterate through complete weeks, so it will yield
         |      dates outside the specified month.
         |  
         |  itermonthdays(self, year, month)
         |      Like itermonthdates(), but will yield day numbers. For days outside
         |      the specified month the day number is 0.
         |  
         |  itermonthdays2(self, year, month)
         |      Like itermonthdates(), but will yield (day number, weekday number)
         |      tuples. For days outside the specified month the day number is 0.
         |  
         |  iterweekdays(self)
         |      Return an iterator for one week of weekday numbers starting with the
         |      configured first one.
         |  
         |  monthdatescalendar(self, year, month)
         |      Return a matrix (list of lists) representing a month's calendar.
         |      Each row represents a week; week entries are datetime.date values.
         |  
         |  monthdays2calendar(self, year, month)
         |      Return a matrix representing a month's calendar.
         |      Each row represents a week; week entries are
         |      (day number, weekday number) tuples. Day numbers outside this month
         |      are zero.
         |  
         |  monthdayscalendar(self, year, month)
         |      Return a matrix representing a month's calendar.
         |      Each row represents a week; days outside this month are zero.
         |  
         |  setfirstweekday(self, firstweekday)
         |  
         |  yeardatescalendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting. The return
         |      value is a list of month rows. Each month row contains up to width months.
         |      Each month contains between 4 and 6 weeks and each week contains 1-7
         |      days. Days are datetime.date objects.
         |  
         |  yeardays2calendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting (similar to
         |      yeardatescalendar()). Entries in the week lists are
         |      (day number, weekday number) tuples. Day numbers outside this month are
         |      zero.
         |  
         |  yeardayscalendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting (similar to
         |      yeardatescalendar()). Entries in the week lists are day numbers.
         |      Day numbers outside this month are zero.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from Calendar:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  firstweekday
        
        class TextCalendar(Calendar)
         |  Subclass of Calendar that outputs a calendar as a simple plain text
         |  similar to the UNIX program cal.
         |  
         |  Method resolution order:
         |      TextCalendar
         |      Calendar
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  formatday(self, day, weekday, width)
         |      Returns a formatted day.
         |  
         |  formatmonth(self, theyear, themonth, w=0, l=0)
         |      Return a month's calendar string (multi-line).
         |  
         |  formatmonthname(self, theyear, themonth, width, withyear=True)
         |      Return a formatted month name.
         |  
         |  formatweek(self, theweek, width)
         |      Returns a single week in a string (no newline).
         |  
         |  formatweekday(self, day, width)
         |      Returns a formatted week day name.
         |  
         |  formatweekheader(self, width)
         |      Return a header for a week.
         |  
         |  formatyear(self, theyear, w=2, l=1, c=6, m=3)
         |      Returns a year's calendar as a multi-line string.
         |  
         |  prmonth(self, theyear, themonth, w=0, l=0)
         |      Print a month's calendar.
         |  
         |  prweek(self, theweek, width)
         |      Print a single week (no newline).
         |  
         |  pryear(self, theyear, w=0, l=0, c=6, m=3)
         |      Print a year's calendar.
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from Calendar:
         |  
         |  __init__(self, firstweekday=0)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  getfirstweekday(self)
         |  
         |  itermonthdates(self, year, month)
         |      Return an iterator for one month. The iterator will yield datetime.date
         |      values and will always iterate through complete weeks, so it will yield
         |      dates outside the specified month.
         |  
         |  itermonthdays(self, year, month)
         |      Like itermonthdates(), but will yield day numbers. For days outside
         |      the specified month the day number is 0.
         |  
         |  itermonthdays2(self, year, month)
         |      Like itermonthdates(), but will yield (day number, weekday number)
         |      tuples. For days outside the specified month the day number is 0.
         |  
         |  iterweekdays(self)
         |      Return an iterator for one week of weekday numbers starting with the
         |      configured first one.
         |  
         |  monthdatescalendar(self, year, month)
         |      Return a matrix (list of lists) representing a month's calendar.
         |      Each row represents a week; week entries are datetime.date values.
         |  
         |  monthdays2calendar(self, year, month)
         |      Return a matrix representing a month's calendar.
         |      Each row represents a week; week entries are
         |      (day number, weekday number) tuples. Day numbers outside this month
         |      are zero.
         |  
         |  monthdayscalendar(self, year, month)
         |      Return a matrix representing a month's calendar.
         |      Each row represents a week; days outside this month are zero.
         |  
         |  setfirstweekday(self, firstweekday)
         |  
         |  yeardatescalendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting. The return
         |      value is a list of month rows. Each month row contains up to width months.
         |      Each month contains between 4 and 6 weeks and each week contains 1-7
         |      days. Days are datetime.date objects.
         |  
         |  yeardays2calendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting (similar to
         |      yeardatescalendar()). Entries in the week lists are
         |      (day number, weekday number) tuples. Day numbers outside this month are
         |      zero.
         |  
         |  yeardayscalendar(self, year, width=3)
         |      Return the data for the specified year ready for formatting (similar to
         |      yeardatescalendar()). Entries in the week lists are day numbers.
         |      Day numbers outside this month are zero.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from Calendar:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  firstweekday
    
    FUNCTIONS
        calendar = formatyear(theyear, w=2, l=1, c=6, m=3) method of TextCalendar instance
            Returns a year's calendar as a multi-line string.
        
        firstweekday = getfirstweekday() method of TextCalendar instance
        
        isleap(year)
            Return True for leap years, False for non-leap years.
        
        leapdays(y1, y2)
            Return number of leap years in range [y1, y2).
            Assume y1 <= y2.
        
        month = formatmonth(theyear, themonth, w=0, l=0) method of TextCalendar instance
            Return a month's calendar string (multi-line).
        
        monthcalendar = monthdayscalendar(year, month) method of TextCalendar instance
            Return a matrix representing a month's calendar.
            Each row represents a week; days outside this month are zero.
        
        monthrange(year, month)
            Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
            year, month.
        
        prcal = pryear(theyear, w=0, l=0, c=6, m=3) method of TextCalendar instance
            Print a year's calendar.
        
        prmonth(theyear, themonth, w=0, l=0) method of TextCalendar instance
            Print a month's calendar.
        
        setfirstweekday(firstweekday)
        
        timegm(tuple)
            Unrelated but handy function to calculate Unix timestamp from GMT.
        
        weekday(year, month, day)
            Return weekday (0-6 ~ Mon-Sun) for year (1970-...), month (1-12),
            day (1-31).
        
        weekheader = formatweekheader(width) method of TextCalendar instance
            Return a header for a week.
    
    DATA
        __all__ = ['IllegalMonthError', 'IllegalWeekdayError', 'setfirstweekda...
        day_abbr = <calendar._localized_day object>
        day_name = <calendar._localized_day object>
        month_abbr = <calendar._localized_month object>
        month_name = <calendar._localized_month object>
    
    FILE
        d:\programs\python3.6_opencv\python36x64\lib\calendar.py


​    
​    


```python

```
