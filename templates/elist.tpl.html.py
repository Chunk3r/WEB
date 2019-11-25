# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574687170.5551798
_enable_loop = True
_template_filename = '/home/pinkman/web/p2/uv/templates/elist.tpl.html'
_template_uri = 'elist.tpl.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        data_o = context.get('data_o', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n   <head>\r\n      <title>Urlaubsliste / Mitarbeiter</title>\r\n      <meta charset="UTF-8" />\r\n      <link rel="stylesheet" href="elist.css" />\r\n      <script src="/elist.js">\r\n      </script>\r\n   </head>\r\n   <body>\r\n      <table>\r\n         <tr>\r\n            <th>Name</th>\r\n            <th>Vorname</th>\r\n            <th>Funktion</th>\r\n            <th>Urlaubstage (Soll)</th>\r\n            <th>Urlaubstage (Ist)</th>\r\n         </tr>\r\n')
        for key_s in data_o:
            __M_writer('         <tr>\r\n            <td>')
            __M_writer(str(data_o[key_s]["name"]))
            __M_writer('</td>\r\n            <td>')
            __M_writer(str(data_o[key_s]["vorname"]))
            __M_writer('</td>\r\n            <td>')
            __M_writer(str(data_o[key_s]["funktion"]))
            __M_writer('</td>\r\n            <td>')
            __M_writer(str(data_o[key_s]["urlaubstage"]))
            __M_writer('</td>\r\n            <td>')
            __M_writer(str(data_o[key_s]["urlaubist"]))
            __M_writer('</td>\r\n            <td>\r\n               <a href="#" data-id="')
            __M_writer(str(key_s))
            __M_writer('" data-action="edit">bearbeiten</a>  /\r\n               <a href="#" data-id="')
            __M_writer(str(key_s))
            __M_writer('" data-action="delete" >löschen</a>\r\n            </td>\r\n         </tr>\r\n')
        __M_writer('      </table>\r\n      <div>\r\n         <a href="#" data-action="add" data-id="">erfassen</a>\r\n      </div>\r\n   </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/pinkman/web/p2/uv/templates/elist.tpl.html", "uri": "elist.tpl.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 6, "23": 24, "24": 25, "25": 26, "26": 26, "27": 27, "28": 27, "29": 28, "30": 28, "31": 29, "32": 29, "33": 30, "34": 30, "35": 32, "36": 32, "37": 33, "38": 33, "39": 37, "45": 39}}
__M_END_METADATA
"""
