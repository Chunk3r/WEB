# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574687179.8673882
_enable_loop = True
_template_filename = '/home/pinkman/web/p2/uv/templates/eform.tpl.html'
_template_uri = 'eform.tpl.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        key_s = context.get('key_s', UNDEFINED)
        data_o = context.get('data_o', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<head>\r\n   <title>Urlaubsliste / Mitarbeiter</title>\r\n   <meta charset="UTF-8" />\r\n   <link rel="stylesheet" href="eform.css" />\r\n   <script src="/eform.js"></script>\r\n</head>\r\n<body>\r\n   <form id="idForm" action="/employee/save" method="POST">\r\n      <input type="hidden" value="')
        __M_writer(str(key_s))
        __M_writer('" id="id_spl" name="id_spl" />\r\n      <div>\r\n         <label for="vorname_spl">Vorname</label>\r\n         <input type="text" value="')
        __M_writer(str(data_o["vorname"]))
        __M_writer('" id="vorname_spl" name="vorname_spl" required />\r\n      </div>\r\n      <div>\r\n         <label for="name_spl">Name</label>\r\n         <input type="text" value="')
        __M_writer(str(data_o["name"]))
        __M_writer('" id="name_spl" name="name_spl" required />\r\n      </div>\r\n      <div>\r\n         <label for="funktion_spl">Funktion</label>\r\n         <input type="text" value="')
        __M_writer(str(data_o["funktion"]))
        __M_writer('" id="funktion_spl" name="funktion_spl" required />\r\n      </div>\r\n      <div>\r\n         <label for="urlaubstage_ipl">Urlaubstage</label>\r\n         <input type="number" value="')
        __M_writer(str(data_o["urlaubstage"]))
        __M_writer('" min="')
        __M_writer(str(data_o["minurlaub"]))
        __M_writer('" max="')
        __M_writer(str(data_o["maxurlaub"]))
        __M_writer('" id="urlaubstage_ipl" name="urlaubstage_ipl" required />\r\n      </div>\r\n      <div>\r\n         <a href="#" data-action="save">speichern</a>\r\n         <a href="#" data-action="reset">zurücksetzen</a>\r\n         <a href="#" data-action="quit">beenden</a>\r\n      </div>\r\n   </form>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/pinkman/web/p2/uv/templates/eform.tpl.html", "uri": "eform.tpl.html", "source_encoding": "utf-8", "line_map": {"16": 0, "23": 6, "24": 16, "25": 16, "26": 19, "27": 19, "28": 23, "29": 23, "30": 27, "31": 27, "32": 31, "33": 31, "34": 31, "35": 31, "36": 31, "37": 31, "43": 37}}
__M_END_METADATA
"""
