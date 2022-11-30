import usb.core
import usb.util 
import argparse

VENDOR = 0x17cc
PRODUCT = 0x1021

device = usb.core.find(idVendor=VENDOR, idProduct=PRODUCT)


# Traktor Audio 10 OUT brequests
#
# brequest 1: channel thru
#   wValue 0/1 Off/On
#   wIndex 3/5/7/9 = channels 1/2/3/4
#
# brequest 2: phono/line switch
#   wValue 0/1 Line/Phono
#   wIndex 3/5/7/9 = channels 1/2/3/4

def setThru(state, channel, persistant):
    bmRequestType = 0x40
    bmRequest = 1

    if state == 'off':
        wValue = 0x0000
    else:
        wValue = 0x0001

    if channel == 1:
        wIndex = 0x0003
    elif channel == 2:
        wIndex = 0x0005
    elif channel == 3:
        wIndex = 0x0007
    elif channel == 4:
        wIndex = 0x0009

    device.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex)


def setSensitivity(state, channel, persistant):
    bmRequestType = 0x40
    bmRequest = 2

    if state == 'off':
        wValue = 0x0000
    else:
        wValue = 0x0001

    if channel == 1:
        wIndex = 0x0003
    elif channel == 2:
        wIndex = 0x0005
    elif channel == 3:
        wIndex = 0x0007
    elif channel == 4:
        wIndex = 0x0009

    device.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex)


parser = argparse.ArgumentParser(description='A command line utility to configure Native Instruments audio interfaces.')
parser.add_argument('method', type=str,
                    help='The method (get, set)')
parser.add_argument('channel', type=int,
                    help='The audio interface input channel (1-4)')
parser.add_argument('device_function', type=str,
                    help='The function (thru, phono)')
parser.add_argument('value', type=str,
                    help='The value (on, off)')
args = parser.parse_args()

if args.method == 'set':
    if args.device_function == 'thru':
        setThru(args.value, args.channel, False)
    if args.device_function == 'phono':
        setSensitivity(args.value, args.channel, False)

