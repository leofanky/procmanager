#!/usr/bin/env python3

import os
import psutil

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
                
class SendSignal(Command): // added by Marius
    def __init__(self, args):
        pass

    def run(self, pid):
        os.kill(pid, signal.SIGUSR1)

class ShowStatus(Command):
	def __init__(self, args):
		if len(args) == 0:
			raise Exception("No pid passed!")
		self.ps = map(lambda pid: psutil.Process(pid), args);

	def run(self):
		print([p.status() for p in self.ps])
                
commands = {
    "list" : lambda args: ListProcs(args),
    "show_status": lambda args: ShowStatus(args), 
    "send_signal": lambda pid: SendSignal(pid) // added by Marius
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
