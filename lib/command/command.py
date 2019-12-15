import importlib
import pkgutil
from cmd import Cmd
from lib.utils import *
from lib.workplace import WorkPlace
import importlib
import configparser
class CMDLine(Cmd):
    module_list = ["BASE"]
    prompt_f = green("{}{}{} ")
    prompt = ""
    options = None
    module = None
    base = "BASE/"
    file = None
    record_file = None
    current_workplace = None #current working place
    module_name = "" #name like Web.PHP.mt_seed
    config = None
    completions = dict()
    def prompt_format(self,module='',prompt="fuck",workplace='None'):
        self.prompt = self.prompt_f.format(blue(module),green(prompt),blue("(")+red(workplace)+blue(")"))
    def init(self):
        self.prompt_format()
        self.config = configparser.RawConfigParser()
        self.config.read('config.ini')
        self.record_file = self.config["header"]["record_file"]
        #for autocompletion of use module
        self.completions["use"] = list()
        def _get_modules(name):
            m = None
            for _,module,_ in pkgutil.iter_modules([name]):
                m = module
                _get_modules(name+module+"/")
            else:
                if m !=None:
                    _ = name + m
                    self.completions["use"].append(_.replace("/",".")[5:])
        _get_modules("BASE/")



    def __init__(self):
        Cmd.__init__(self)
        print(blue("initializing..."))
        self.init()
        print(blue('done'))
    def emptyline(self):
        pass

    def do_use(self,arg):
        try:
            self.module = importlib.import_module("BASE."+arg)
            self.module = self.module.Module()
            self.prompt_format(module=("["+arg+"]"), workplace=self.current_workplace.workplace_name
            if self.current_workplace != None else 'None')
            self.module_name = arg
            self.completions["set"] = list(self.module.getOptions().keys())
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

    def do_workplace(self,arg:str):
        try:
            args = arg.split(" ")
            if args[0] == "create":
                args[1] = args[1].strip()
                if args[1].strip() == "":
                    print_warning("Must name your workplace")
                    return
                workplace = WorkPlace(args[1])
                self.current_workplace = workplace
            elif args[0] == "use":
                args[1] = args[1].strip()
                if args[1] == "":
                    print_warning("Must select your workplace")
                    return
                workplace = WorkPlace(args[1])
                self.current_workplace = workplace
                self.prompt_format(module=self.module_name,workplace=self.current_workplace.workplace_name
                                    if self.current_workplace!=None else 'None')

        except Exception as e:
            print(e)

    def do_run(self,arg):
        cache = self.module.run()
        if arg.strip() == "-save":
            self.current_workplace.save(cache,self.module_name)


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

    def complete_set(self,text,line,begidx,endidx):
        mline = line.partition(' ')[2]
        offs = len(line) - len(text)
        lines = []
        for s in self.completions[line.partition(' ')[0]]:
            if s.startswith(mline):
                lines.append(s)
        return lines

    def complete_use(self,text,line,begidx,endidx):
        mline = line.partition(' ')[2]
        return [s for s in self.completions["use"] if s.startswith(mline)]

def main():
    importlib.import_module("BASE")
    parse = CMDLine()
    parse.cmdloop()


if __name__ == '__main__':
    try:
        main()
    except:
        pass