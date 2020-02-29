from ctypes import *
import random
def print_options(options:dict):
    for i in options.keys():
        print("{}:{}".format(i,options[i]))


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