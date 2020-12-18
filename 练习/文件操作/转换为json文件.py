from configparser import ConfigParser
import json

filename = '/tmp/test.ini'
jsonname = '/tmp/test.json'

cfg = ConfigParser()
cfg.read(filename)

dest = {}

for sect in cfg.sections():
    print(sect, cfg.items(sect))
    dest[sect] = dict(cfg.items(sect))

json.dump(dest, open(jsonname,'w'))