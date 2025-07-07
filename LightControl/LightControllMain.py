from phue import Bridge
import sys
import argparse
import time

def connect_to_bridge():
    b = Bridge('192.168.1.97')
    b.connect()
    return b

def get_lights_names(b: Bridge):
    for light in b.lights:
        print(light)

def SwitchLights(bridge, room, state):
    for light in room.lights:
        if room.name == "Kaffe":
            continue
        command = {'on' : state}
        bridge.set_light(int(light.light_id), command)

def DimRoom(bridge, room, brightness: int):
    
    for light in room.lights:
        if room.name == "Kaffe":
            continue
       
        if light.on:
            print(light)
        
            command = {'transitiontime':50, 'bri' : brightness}
            bridge.set_light(int(light.light_id), command)

def main():
    parser = argparse.ArgumentParser(description = "Control Lights Dimmer")
    parser.add_argument('action', choices =['up', 'down', 'on', 'off'], help = "dim control up/down")

    args = parser.parse_args()
    bridge = connect_to_bridge()
    current_status = bridge.get_light(1, 'on')
    for room in bridge.groups:
        
        # living_room = bridge.get_group(room) #TODO: hämta via ID istället
        
        if args.action == 'up':
            DimRoom(bridge,room, 200)
        if args.action == 'down':
            DimRoom(bridge, room, 20)
        if args.action == 'on':
            SwitchLights(bridge,room, not current_status)
        if args.action == 'off':
            SwitchLights(bridge,room,False)


if __name__=="__main__":
    main()
