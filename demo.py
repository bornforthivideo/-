# -*- coding: utf-8 -*-
# @Time    : 2022/11/20 09:10
# @Author  : AI悦创
# @FileName: demo.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# from http.server import HTTPServer, BaseHTTPRequestHandler
#
#
# def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
#     server_address = ('', 9090)
#     httpd = server_class(server_address, handler_class)
#     httpd.serve_forever()
#
# if __name__ == '__main__':
#     run()
# import http.server
# import socketserver
#
# PORT = 65535
#
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()
# !/usr/bin/env python

import wx

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World")  # A Frame is a top-level window.
frame.Show(True)  # Show the frame.
app.MainLoop()
