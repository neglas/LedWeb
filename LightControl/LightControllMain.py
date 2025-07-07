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
    parser.add_argument('action', choices =['up', 'down'], help = "dim control up/down")

    args = parser.parse_args()
    bridge = connect_to_bridge()
    for room in bridge.groups:
        
        # living_room = bridge.get_group(room) #TODO: hämta via ID istället
        
        if args.action == 'up':
            DimRoom(bridge,room, 200)
        if args.action == 'down':
            DimRoom(bridge, room, 20)


if __name__=="__main__":
    main()