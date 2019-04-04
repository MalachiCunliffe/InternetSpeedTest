'''
Author: Malachi Cunliffe
Contact: Mal.Cunliffe@gmail.com
13/05/18


This program tests the internet speed from Carlaw to the uni

This is to see the improvement of the new fibre cable once it is implemented

'''
import time
import speedtest
import pickle
import requests
import socket
import datetime
fileName = "internet_test_results_post_fibre.txt"



def internet_on():
    try:
        r = requests.get('https://google.co.nz')
        return True


    except: 
        return False

    
def write_results(results):
    file = open(fileName, 'a')
    file.write(results + '\n')
    file.close()




# setting the desired server to speed2.snap.net.nz:8080 id = 5539
#s = speedtest.Speedtest()
#server = [5539]

#print(s.get_servers(server))

def do_test():
        s = speedtest.Speedtest()
        server = [5539]
        
        try:
            s.get_servers(server)
        except:
            main()
        else:
            s.get_best_server()
            #s.get_servers(server)
            s.download()
            s.upload()
            s.results.share()
            results_dict = s.results.json()
            write_results(results_dict)
            print('Great success!')
            time.sleep(600)
            main()




def main():
    if internet_on():
        do_test()
        
    else:
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        outage = 'INTERNET-DOWN {0}'.format(st)
        print('Internet out  waiting 1 minute')
        write_results(outage)
        time.sleep(60)
        main()

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
start_t = 'Testing started at: {0}'.format(st)
print(start_t)
write_results(start_t)
main()  
