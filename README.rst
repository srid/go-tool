go -- quick directory switching
===============================

::

    Home            : http://trentm.com/projects/go/
    License         : MIT (see LICENSE.txt)
    Platforms       : Windows, Linux, Mac OS X, Unix
    Current Version : 1.2.1
    Dev Status      : mature
    Requirements    : Python >= 2.4 (http://www.activestate.com/activepython)


Why go?
-------

``go`` is a small command for changing directories quickly.
Typically you have a set of directories that you work in.  Typing out
the names of those dirs in full can be tedious.  ``go`` allows you to
give a shortcut name for a directory, say ``ko`` for
``D:\trentm\main\Apps\Komodo-devel``, and do the following::

    C:\> go ko
    D:\trentm\main\Apps\Komodo-devel>

and::

    C:\> go ko/test
    D:\trentm\main\Apps\Komodo-devel\test>

Think of it as a super ``cd``. 

``go`` is free (MIT License).  Please send any feedback to `Trent
Mick <mailto:trentm@google's mail thing>`_.


Install Notes
-------------

Download the latest (1) ``go`` source package, (2) unzip it, (3) run
``python setup.py install`` in the unzipped directory, and (4) run
``go-setup`` (or ``python -m go``) to setup the shell driver::

    unzip go-1.2.1.zip
    cd go-1.2.1
    python setup.py install
    go-setup   # to setup shell integration

If your install fails then please visit `the Troubleshooting
FAQ <http://trentm.com/faq.html#troubleshooting-python-package-installation>`_.


Getting Started
---------------

The most common things you'll do with ``go`` are adding new shortcuts::

    [~/Library/Application Support/Komodo]$ go -a koappdata

listing the shortcuts you've created::

    [~]$ go --list
                        Go Shortcuts
                        ============

    Default shortcuts:
      .                     .
      ..                    ..
      ...                   ../..
      tmp                   /tmp
      ~                     /Users/trentm

    Custom shortcuts:
      cgi-bin               /Library/WebServer/CGI-Executables
      koappdata             /Users/trentm/Library/Application Support/Komodo
      pyinstall             /Library/Frameworks/Python.framework/Versions/2.6
      staging               /Users/trentm/Sites/staging
      www                   /Users/trentm/Sites

and switching to directories using those shortcuts::

    [~]$ go pyinstall
    [/Library/Frameworks/Python.framework/Versions/2.6]$ go www
    [~/Sites]$ 

Run ``go --help`` for full usage details or just `take a look at the
``go.py`` script.

::

    $ go --help
    Quick directory changing.

    Usage:
        go <shortcut>[/sub/dir/path]    # change directories
                                        # same as "go -c ..."
        go -c|-o|-a|-d|-s ...           # cd, open, add, delete, set
        go --list [<pattern>]           # list matching shortcuts

    Options:
        -h, --help                      print this help and exit
        -V, --version                   print verion info and exit

        -c, --cd <path>                 cd to shortcut path in shell
        -s, --set <shortcut> <dir>      set a shortcut to <dir>
        -a, --add-current <shortcut>    add shortcut to current directory
        -d, --delete <shortcut>         delete the named shortcut
        -o, --open <path>               open the given shortcut path in
                                        explorer (Windows only)
        -l, --list [<pattern>]          list current shortcuts

    Generally you have a set of directories that you commonly visit.
    Typing these paths in full can be a pain. This script allows one to
    define a set of directory shortcuts to be able to quickly change to
    them. For example, I could define 'ko' to represent
    "D:\trentm\main\Apps\Komodo-devel", then
        C:\> go ko
        D:\trentm\main\Apps\Komodo-devel>
    and
        C:\> go ko/test
        D:\trentm\main\Apps\Komodo-devel\test>

    As well, you can always use some standard shortcuts, such as '~'
    (home) and '...' (up two dirs).

    See <http://trentm.com/projects/go/> for more information.
