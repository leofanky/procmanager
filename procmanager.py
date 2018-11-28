#!/usr/bin/env python3

import os

class Command():
    def __init__(self, args):
        pass

class ListProcs(Command):
    def __init__(self, args):
        pass

    def run(self):
        proc = "/proc"
        for d in os.listdir("/proc"):
            if os.path.isdir(proc + "/" + d) and d.isdigit():
                print(d)
class limits():
	def __init__(self, args):
		self.arg = args[0]
	
	def run(self):
		for line in open(f"/proc/" + self.arg + "/limits").readlines():
			print(line.split('\t')
			
commands = {
    "list" : lambda args: ListProcs(args) ,
    "limits" : lambda args : limits (args)
}

def get_command():
    strs = input("> ").split()
    try:
        cmd = commands[strs[0]](strs[1:])
    except KeyError as e:
        print("Unknown command")
    return cmd

while True:
    cmd = get_command()
    cmd.run()
