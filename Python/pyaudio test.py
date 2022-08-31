import pyaudio

pa =  pyaudio.PyAudio()


pa.get_default_input_device_info()


print(pa.get_default_host_api_info())