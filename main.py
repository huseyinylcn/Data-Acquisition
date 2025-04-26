import my_network
import tcp
import my_adc
import  my_clock
import write





import utime
import time
import _thread






net = my_network.Network("Hy", "12345678", 20)
net.wifi_connect()



mytcp = tcp.TCP("192.168.13.116", 50000)
result = mytcp.connect()


clock = my_clock.My_Clock()

fileProcess = write.Write()



def core1_task():
	
	
	INTERVAL_US = 10000
	our_adc= my_adc.myADC()
	
	
	while True:
		start_time = utime.ticks_us()
		adcData = our_adc.adcRead()


		elapsed_time = utime.ticks_diff(utime.ticks_us(), start_time)
		if elapsed_time < INTERVAL_US:
			remaining_time = INTERVAL_US - elapsed_time
			time.sleep(remaining_time / 1000000)
			
		
		
		

_thread.start_new_thread(core1_task, ())


songun = None 
def main_core():
	INTERVAL_US = 10000
	start_time = utime.ticks_us()
	global songun
	
	zaman = clock.get_clock()
	trh = clock.get_date()
	
	data = zaman + " \n"
	
	
	if songun != trh:
		fileProcess.dosya_kapat()
		filename = trh + ".log"
		fileProcess.dosya_acma(filename)
		songun = trh

	try :
		fileProcess.dosya_yaz(data)
	except Exception as e:
		pass
	
	
	
	
	

	

	if net.is_connected():
		tcpSendResult = mytcp.send(data)
		if not tcpSendResult:
			result = mytcp.connect()
	else:
		connection_state = net.check_connection_status()
		if not connection_state:
			net.wifi_connect()
			
			
			
	
	
	elapsed_time = utime.ticks_diff(utime.ticks_us(), start_time)
	if elapsed_time < INTERVAL_US:
		remaining_time = INTERVAL_US - elapsed_time
		time.sleep(remaining_time / 1000000)
    
    
    




while True:
	main_core()

  



