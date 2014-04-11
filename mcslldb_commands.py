#!/usr/bin/env python
# encoding: utf-8

import json as json_lib
from os import system
from tempfile import NamedTemporaryFile

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JavascriptLexer

from mcslldb_helpers import get_value, lldb_command


@lldb_command
def json(debugger, expression):
    # get JSON string
    value = get_value(debugger, expression)
    json_string = value.GetObjectDescription()

    # prettify JSON
    pretty_json_string = json_lib.dumps(json_lib.loads(json_string),
                                        sort_keys=True, indent=4)

    # render HTML with highlighted JSON
    formatter = HtmlFormatter(linenos=True)
    html = """
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">

        <style>
            {style}
        </style>
    </head>

    <body>
        {body}
    </body>
</html>
    """.format(**{
        'style': formatter.get_style_defs('.highlight'),
        'body': highlight(pretty_json_string, JavascriptLexer(), formatter),
    })

    # save HTML to a temporary file
    with NamedTemporaryFile(delete=False) as f:
        f.write(html)

        # add ".html" extension
        original_path = f.name
        path = original_path + '.html'
        system('mv "%s" "%s"' % (original_path, path))

    # show HTML in Quick Look and delete file at the end
    system('qlmanage -p "%s" > /dev/null && rm "%s" &' % (path, path))
