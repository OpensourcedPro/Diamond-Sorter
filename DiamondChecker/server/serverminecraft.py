# python3

import socket
import pickle

import json


from sqlighter import SQLighter


from datetime import datetime

BUFFER_SIZE = 4096

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('0.0.0.0', 53210))
serv_sock.listen(10)




while True:
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    all_data = bytearray()

    while True:
        data = client_sock.recv(BUFFER_SIZE)
        if not data:
            break
        data = json.loads(data.decode())
        whid = data.get("WHID")
        username = data.get("username")
        print(whid)
        print(username)

        db = SQLighter('server_dlc.db')
        user_info = db.whid_bd(username)

        if bool(len(user_info)) == 1:
            print("username TRUE")

            for info in user_info:
                print(info)
            if info[8] != None:
                print(info[8])
                if info[8] == whid:
                    print("WHID TRUE")
                    if info[7] == 1:
                        if datetime.now().date() < datetime.date(datetime.strptime(info[6], '%Y-%m-%d')):
                            print("STATUS SUBSCRIBE TIME TRUE")
                            data = json.dumps({"Donat": "1", "Messages": "Subscription is active Welcome to the club"})
                            client_sock.send(data.encode())
                        else:
                            print("STATUS SUBSCRIBE TIME FALSE PODPISKA KONCHILAS")
                            data = json.dumps({"Donat": "0", "Messages": "The subscription has not ended"})
                            client_sock.send(data.encode())
                    else:
                        print("STATUS SUBSCRIBE FALSE")
                        data = json.dumps({"Donat": "0", "Messages": "Subscription not found"})
                        client_sock.send(data.encode())
                else:
                    print("WHID FALSE MULTILOGIN PEREPREFEZkA NUZHNA ?")
                    data = json.dumps({"Donat": "0",
                                       "Messages": "The checker is attached by hardware to reconnect, contact the saport"})
                    client_sock.send(data.encode())
            else:
                print("WHID FALSE DOBAVIT WHID I VIKINYT")
                data = json.dumps({"Donat": "1", "Messages": "The license is linked by HWID: ", "WHID": whid})
                client_sock.send(data.encode())
                db.add_hid_db(username, whid)
        else:
            print("username FALSE @TG KYPIT")
            data = json.dumps({"Donat": "0", "Messages": "The user was not found"})
            client_sock.send(data.encode())

    print('Close')
    client_sock.close()
    db.close()
