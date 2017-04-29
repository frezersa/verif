import os
import sys

from bokeh.layouts import column, row
from bokeh.server.server import Server
from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from tornado.ioloop import IOLoop
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
import bokeh.plotting
import bokeh.mpl
import verif.data
import verif.output
import verif.input
import verif.metric
import verif.axis
import verif.aggregator
import verif.bokeh_server
import datetime

def main():
   print('Opening Bokeh application on http://localhost:5006/')

   io_loop = IOLoop.current()
   s = verif.bokeh_server.BokehServer(sys.argv[1:])

   #bokeh_app = Application(FunctionHandler(verif.bokeh_server.update))
   def q(doc):
      print 1
      s.update(doc)

   bokeh_app = Application(FunctionHandler(s.update))
   server = Server({'/': bokeh_app}, io_loop=io_loop,
         allow_websocket_origin=["pc4423.pc.met.no:5006", "localhost:5006"])
   server.start()

   #io_loop.add_callback(server.show, "/")
   io_loop.start()


if __name__ == '__main__':
   main()