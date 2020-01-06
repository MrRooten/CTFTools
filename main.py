import importlib
import pkgutil
from cmd import Cmd
from lib.utils import *
import importlib
class CMDLine(Cmd):
    module_list = ["BASE"]
    prompt = ">>> "
    options = None
    module = None
    base = "BASE/"
    file = None
    record_file = "record.txt"

    def emptyline(self):
        pass
    def do_use(self,arg):
        try:
            self.module = importlib.import_module("BASE."+arg)
            self.module = self.module.Module()
            self.prompt = "["+arg+"]" + ">>> "
        except Exception as e:
            print_error(e)

    def do_ls(self,arg):
        for _,module,_ in pkgutil.iter_modules(["BASE/"+arg.replace('.','/')]):
            print(module)

    def do_options(self,arg):
        print_options(self.module.getOptions())

    def do_info(self,arg):
        print_info(self.module.getInfo())
        
    def do_set(self,arg:str):
        try:
            key = arg[:arg.find(" ")]
            value = arg[arg.find(" ")+1:]
            self.module.setOption(key,value)

        except:
            pass
    def do_run(self,arg):
        self.module.run()

    def do_exit(self,arg):
        exit(0)

    def do_record(self):
        self.file = open(self.record_file,"w")

    def close(self):
        if self.file:
            self.file.close()
            self.file = None



    def do_playback(self):
        self.close()
        with open(self.record_file) as f:
            self.cmdqueue.extend(f.read().splitlines())
def main():
    importlib.import_module("BASE")
    parse = CMDLine()
    parse.cmdloop()

if __name__ == '__main__':
    main()