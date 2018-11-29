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
		self.ps = map(lambda pid: psutil.Process(int(pid)), args);

class ListVars(Command):
    def __init__(self, args):
        self.args = args

    def run(self):
        keys = []
        values = []
        with open("/proc/" + self.args[0] + "/environ") as f:
            vars = f.read().split('=')
            for var in vars:
                val = ''
                key = ''
                for v in var:
                    if v.isupper():
                        key += v
                    else:
                        val += v
                keys.append(key)
                if val:
                    values.append(val.strip('\x00_'))
        print(dict(zip(keys, values)))

	def run(self):
		print([p.status() for p in self.ps])

class showMem:
    def __init__(self, args):
        self.arg = args

    def run(self):
        DIR = '/proc/'
        process = self.arg[0]
        path = DIR + process + '/status'
        exst = False
        for n,line in enumerate(open(path)):
            if line[:6] == 'VmSize':
                exst = True
                print (line[10:])
        if not exst: 
                print ('No status')

class limits():
	def __init__(self, args):
		self.arg = args[0]
	
	def run(self):
		for line in open(f"/proc/" + self.arg + "/limits").readlines():
			print(line)
                  
commands = {
    "list" : lambda args: ListProcs(args),
    "show_status": lambda args: ShowStatus(args), 
    "send_signal": lambda pid: SendSignal(pid) // added by Marius
    "env"  : lambda args: ListVars(args)
    "memory_usage": lambda args: showMem(args)
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
