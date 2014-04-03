MCSLLDBToolkit
==============

Set of handy LLDB commands that will dramatically improve your debugging workflow


Commands
--------

### `json`

View formatted and colored JSON string in Quick Look.

![](images/json.png)


Installation
------------

To use MCSLLDBToolkit you have to download the project and import it in
`~/.lldbinit`.  To use the `json` command you have to have [Pygments][]
installed.  You can do all of the above with a few simple commands:

    mkdir ~/.lldb
    cd ~/.lldb
    git clone git@github.com:macoscope/MCSLLDBToolkit.git
    echo 'command script import ~/.lldb/MCSLLDBToolkit/mcslldb_main.py' >> ~/.lldbinit
    sudo easy_install pygments

  [Pygments]: http://pygments.org/


Copyright
---------

MCSLLDBToolkit is developed by [Macoscope](http://macoscope.com/)
and licensed under [Apache v2 license](LICENSE).
