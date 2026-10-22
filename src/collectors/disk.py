import psutil

path = "/"

def get_disk_usage():
    return psutil.disk_usage(path).percent


