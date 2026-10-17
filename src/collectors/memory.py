import psutil

def get_memory_usage():
    return psutil.virtual_memory().percent

get_memory_usage()
