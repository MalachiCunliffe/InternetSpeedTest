'''
Author: Malachi Cunliffe
Contact: Mal.Cunliffe@gmail.com

This program tests the internet speed from Carlaw to the uni

This is to see the improvement of the new fibre cable once it is implemented

'''
import speedtest
import pickle
fileName = "internet_res.txt"
#file = open(fileName, 'w')
#server = [5539]
server = []
# setting the desired server to speed2.snap.net.nz:8080 id = 5539


s = speedtest.Speedtest()
try :
    s.get_servers(server)
except:
    s.get_closest_servers()

s.get_best_server()
s.download()
s.upload()
s.results.share()

results_dict = s.results.json()
pickle.dump(results_dict, open( fileName, "wb" ), pickle.HIGHEST_PROTOCOL)

#file.close()
print(results_dict)
