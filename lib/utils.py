from ctypes import *
import random
import configparser
config = configparser.RawConfigParser() #Global config
config.read("config.ini")


def print_options(options:dict):
    try:
        print("{:40s}{:40s}{:40s}{}".format(red("args"),red("value"),red("necessity"),red("description")))
        for option_key in options.keys():
            print("{:40s}{:40s}{:40s}{}".format(option_key,
                                               options[option_key]["args"],
                                               "True" if options[option_key]["necessity"] else "False",
                                               options[option_key]["description"]))
    except Exception as e:
        print(e)


def print_info(info:dict):
    for i in info.keys():
        print("{}:{}".format(i,info[i]))

def print_error(msg:str):
    print(red("[Error]:"),msg)

def print_warning(msg:str):
    print(yellow("[Warning]:"),msg)

def print_info(msg:str):
    print(green("[Info]:"),msg)

def strArrayToPointer(strArray:list):
    res = (c_char_p)*(len(strArray))()
    for i in range(len(strArray)):
        res[i] = c_char_p(i)

    return res

def red(msf):
    return "\033[1;31m{}\033[39m".format(msf)

def blue(msf):
    return "\033[1;34m{}\033[39m".format(msf)

def green(msf):
    return "\033[1;32m{}\033[39m".format(msf)

def yellow(msf):
    return "\033[1;34m{}\033[39m".format(msf)
'''
get what is SuperTools running on
'''
def get_platform():
    pass
'''
write config
'''
def config_write(header,args,value):
    config.set(header,args,value)
    with open("config.ini","w+") as f:
        config.write(f)

'''
read config 
'''
def config_read(header,args):
    return config[header][args]


def banner():
    banner = []
    banner.append(("""
  ██████  █    ██  ██▓███  ▓█████  ██▀███  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▒██    ▒  ██  ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
░ ▓██▄   ▓██  ▒██░▓██░ ██▓▒▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
  ▒   ██▒▓▓█  ░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██████▒▒▒▒█████▓ ▒██▒ ░  ░░▒████▒░██▓ ▒██▒  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░ ░▒  ░ ░░░▒░ ░ ░ ░▒ ░      ░ ░  ░  ░▒ ░ ▒░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░  ░  ░   ░░░ ░ ░ ░░          ░     ░░   ░   ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
      ░     ░                 ░  ░   ░                  ░ ░      ░ ░      ░  ░                                                                     
    """))

    banner.append(red("""
███████╗██╗   ██╗██████╗ ███████╗██████╗ ████████╗ ██████╗  ██████╗ ██╗     
██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     
███████╗██║   ██║██████╔╝█████╗  ██████╔╝   ██║   ██║   ██║██║   ██║██║     
╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗   ██║   ██║   ██║██║   ██║██║     
███████║╚██████╔╝██║     ███████╗██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                            
    """))

    banner.append(blue("""
▄▀▀▀▀▄  ▄▀▀▄ ▄▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄     
█ █   ▐ █   █    █ █   █   █ ▐  ▄▀   ▐ █   █   █ █    █  ▐ █      █ █      █ █    █      
   ▀▄   ▐  █    █  ▐  █▀▀▀▀    █▄▄▄▄▄  ▐  █▀▀█▀  ▐   █     █      █ █      █ ▐    █      
▀▄   █    █    █      █        █    ▌   ▄▀    █     █      ▀▄    ▄▀ ▀▄    ▄▀     █       
 █▀▀▀      ▀▄▄▄▄▀   ▄▀        ▄▀▄▄▄▄   █     █    ▄▀         ▀▀▀▀     ▀▀▀▀     ▄▀▄▄▄▄▄▄▀ 
 ▐                 █          █    ▐   ▐     ▐   █                             █         
                   ▐          ▐                  ▐                             ▐      
    """))

    print(banner[random.randint(0,len(banner)-1)])