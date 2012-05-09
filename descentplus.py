#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  
#  Copyright 2012 Brian Manderville, DescentOS <brian@descentos.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import gtk
import webkit
import gobject

class Browser: #Definitely need the browser class for this since it's... a browser
      default_site = "http://www.descentos.org" #Testing URL right now just to prove webkit works.
      name = "Descent Plus" #Don't really think this matters here
      def delete_event(self, widget, event, data=None):
          return False
      def destroy (self, widget, data=None):
          gtk.main_quit()
      def __init__(self):
          gobject.threads_init()
          self.window =  gtk.Window(gtk.WINDOW_TOPLEVEL)
          self.window.set_resizable(True)
          self.window.set_default_size (700, 450) #Setting default window size.
          self.window.connect("delete_event", self.delete_event)
          self.window.connect("destroy", self.destroy)
          self.web_view = webkit.WebView()
          self.web_view.open(self.default_site)
          scroll_window = gtk.ScrolledWindow(None, None)
          scroll_window.add(self.web_view)
          vbox = gtk.VBox(False, 0)
          vbox.add(scroll_window)
          self.window.add(vbox)
          self.window.show_all()  #Finished a bit of the GTK stuff as well. Need this to scale.
      def on_active(self, widget, data=None):
          url = self.address_bar.get_text() #Playing it safe because url needs to be defined to open the file.
          try:
              url.index("://")
          except:
                 url = "http://"+url
          self.address_bar.set_text(url)
          self.web_view.open(url) #Now Webkit opens the URL, yay!
      def update_buttons(self, widget, data=None):
          self.address_bar.set_text( widget.get_main_frame().get_uri() )
      def main(self):
        gtk.main()
if __name__ == "__main__":
    browser = Browser()
    browser.main()

#So we have here is a stripped down web browser. I will probably add go back buttons at some point for people who are browsing apps
#Also, I need to find a way to link it into apt somehow (AptURL?)
