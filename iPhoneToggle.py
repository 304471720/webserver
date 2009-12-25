# CTK: Cherokee Toolkit
#
# Authors:
#      Alvaro Lopez Ortega <alvaro@alobbs.com>
#
# Copyright (C) 2009 Alvaro Lopez Ortega
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 2 of the GNU General Public
# License as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

from Widget import Widget, RenderResponse

HEADERS = [
    '<script type="text/javascript" src="/static/js/jquery.ibutton.js"></script>',
    '<link type="text/css" href="/static/css/jquery.ibutton.css" rel="stylesheet" media="all" />'
]

HTML = """
<input type="checkbox" id="%(id)s" name="%(name)s" value="true" />
"""

JS = """
$("#%(id)s").iButton();
"""

class iPhoneToggle (Widget):
    def __init__ (self, props={}):
        Widget.__init__ (self)
        self._props = props

        if not 'id' in props:
            self._props['id'] = 'widget%d'%(self.uniq_id)

    def Render (self):
        html = HTML %(self._props)
        js   = JS   %(self._props)

        return RenderResponse (html, js, HEADERS)
