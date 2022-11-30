# hacktoraudio

A python command line utility to configure Native Instruments audio interfaces.


## How to use

Install the requirements:
```
pip install -r requirements.txt
```

Run the script: 
```
python hacktoraudio.py <method> <channel> <device_function> <value>
```

Examples:
```shell
# Turn THRU on channel 1 off
hacktoraudio.py set 1 thru off

# Turn PHONO on channel 3 on
hacktoraudio.py set 3 phono on
```

Dependencies:
- pyusb

## Compatibility
- Native Instruments Traktor Audio 10

Currently supports Traktor Audio 10 only, tested with its latest firmware.

## How it works

I partially reverse engineered the usb commands that are sent by the official control panel. The protocol used is very simple and relies on USB_CONTROL OUT messages.


## ToDo:
- Support reading current state from device
- Support setting a state persistently to device
- Select device option (currently auto-detected)
- Support for other NI audio interfaces (Audio 8...)