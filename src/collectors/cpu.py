import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=None) #non-blocking

get_cpu_usage()
