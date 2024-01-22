import platform
import socket
import psutil
import screeninfo
import wmi
import uuid

def get_installed_software():
    software_list = [proc.info['name'] for proc in psutil.process_iter(['name']) if 'name' in proc.info]
    return software_list

def get_screen_resolution():
    monitors = screeninfo.get_monitors()
    resolutions = [(monitor.width, monitor.height) for monitor in monitors]
    return resolutions

def get_cpu_info():
    cpu_info = {
        'model': platform.processor(),
        'cores': psutil.cpu_count(logical=False),
        'threads': psutil.cpu_count(logical=True)
    }
    return cpu_info

def get_gpu_info():
    try:
        w = wmi.WMI()
        gpu_info = w.Win32_VideoController()[0].Caption
    except Exception as e:
        gpu_info = None
    return gpu_info

def get_ram_size():
    ram_size_gb = psutil.virtual_memory().total / (1024 ** 3)
    return ram_size_gb

def get_screen_size():
    standard_dpi = 146
    screen_width_inches = 1920 / standard_dpi
    screen_height_inches = 1080 / standard_dpi
    diagonal_inches = (screen_width_inches**2 + screen_height_inches**2)**0.5
    return diagonal_inches

def get_mac_address():
    try:
        mac_address = ':'.join(['{:02x}'.format((int)(each, 16)) for each in hex(uuid.getnode())[2:].zfill(12)][::-1])
    except Exception as e:
        mac_address = None
    return mac_address

def get_public_ip():
    try:
        public_ip = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        public_ip = None
    return public_ip

def get_windows_version():
    windows_version = platform.system() + ' ' + platform.release()
    return windows_version

if __name__ == "__main__":
    print("Installed Software:", get_installed_software())
    print('\n\n')
    print("Screen Resolution:", get_screen_resolution())
    print('\n\n')
    print("CPU Information:", get_cpu_info())
    print('\n\n')
    print("GPU Information:", get_gpu_info())
    print('\n\n')
    print(f"RAM Size: {get_ram_size():.2f} GB")
    print('\n\n')
    diagonal_size = get_screen_size()
    print(f"Screen Size: {diagonal_size:.2f} inches")
    print('\n\n')
    print("WiFi/Ethernet MAC Address:", get_mac_address())
    print('\n\n')
    print("Public IP Address:", get_public_ip())
    print('\n\n')
    print("Windows Version:", get_windows_version())
