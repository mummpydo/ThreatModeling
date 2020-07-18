#!/usr/bin/env python3

from pytm import TM, Server, Datastore, Dataflow, Boundary, Actor

tm = TM("my test tm")
tm.description = "another test tm"
tm.isOrdered = True

User_Web = Boundary("User/Web")
Web_DB = Boundary("Web/DB")
