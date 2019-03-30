import argparse
import logging
import os
import sys

# from sleepyDaemon import SleepyDaemon
from main_ras import run_daemo
from main_ras import Control_Sensor

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="chuong trinh dieu khien va kiem soat nhiet do khong khi.")
    parser.add_argument('-s', '--start-session',
                        help='start a new session for rasberipy', action='store_true')
    parser.add_argument('-v', '--view-system',
                        help='view all setting of system', action='store_true')
    parser.add_argument('-c', '--controler',
                        help='choose switch want to on/off.', type=list)
    parser.add_argument('-p', '--process',
                        help='choose process want to do (1-On, 0-Off).', type=int)
    parser.add_argument(
        '-g', '--get-value', help='get all value in all sensor.', action='store_true')
    parser.add_argument('-r', '--reset',
                        help='reset sesion', action='store_true')
    parser.add_argument('-x', '--exit',
                        help='exit and shutdown service', action='store_true')

    args = parser.parse_args()

    logfile = os.path.join(os.getcwd(), "sleepy.log")
    pidfile = os.path.join(os.getcwd(), "sleepy.pid")
    logging.basicConfig(filename=logfile, level=logging.DEBUG)

    d = run_daemo(pidfile=pidfile)

    action = ''
    if (args.start_session):
        action = 'start'
    if (args.reset):
        action = 'restart'
    if (args.exit):
        action = 'stop'

    print(args)

    if action == "start":
        d.start()
    if action == "stop":
        d.stop()
    if action == "restart":
        d.restart()

    if args.get_value:
        cs = Control_Sensor.getInstance()
        cs.get_value()
    if args.controler != None and args.process != None:
        cs = Control_Sensor.getInstance()
        cs.setPinToControl(args.controler, args.process)
        print(cs)
    elif (args.controler != None or args.process != None):
        sys.stdout.write('should user -c [list] -p 0/1 \n')
        print(cs)

    # print(args)
