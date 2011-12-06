#!/usr/bin/python

import conf
import db

import os
import math
import random

def main():
    path = conf.path
    neg = conf.negatives
    Base.metadata.create_all(engine)
    toprocess = []
    for root, dir, files in os.walk(path):
        for f in files:
            if os.path.splitext(f)[1] == ".mp3":
                toprocess.append(os.path.join(root, f))
    print "Found", len(toprocess), "files"
    cutoff = int(math.ceil(len(toprocess) * neg / 100.0))
    print "Keeping back", cutoff, "of them (%d%%)" % cutoff
    random.shuffle(toprocess)
    negativefiles = toprocess[:cutoff]
    fpfiles = toprocess[cutoff:]

    for f in negativefiles:
        nfile = db.NegativeFile(unicode(f, errors="ignore"))
        db.session.add(nfile)

    for f in fpfiles:
        fpfile = db.FPFile(unicode(f, errors="ignore"))
        db.session.add(fpfile)
    db.session.commit()

if __name__ == "__main__":
    main()


