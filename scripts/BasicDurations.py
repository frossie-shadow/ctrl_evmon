import sys, os, re

from lsst.ctrl.evmon import EventMonitor
from lsst.ctrl.evmon.durations import fromdb
import lsst.ctrl.evmon.db as db

def main():
    runid = sys.argv[1]
    host = "lsst10"
    if len(sys.argv) > 2:
        host = sys.argv[2]
    dest = "durations"
    if len(sys.argv) > 3:
        dest = sys.argv[3]
    authinfo = db.readAuthInfo(host)

    monitor = EventMonitor(fromdb.LoopDuration(runid, authinfo, dest))
    monitor.addJob(fromdb.ProcessDuration(runid, authinfo, dest))
    monitor.addJob(fromdb.EventWaitDuration(runid, authinfo, dest))
    monitor.addJob(fromdb.StageDuration(runid, authinfo, dest))

    monitor.runJobs()

if __name__ == "__main__":
    main()
    