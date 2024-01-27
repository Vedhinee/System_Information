from django.shortcuts import render
import psutil
import platform
import datetime

def system_info(request):
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage_perc = psutil.disk_usage('/').percent
    disk_usage = psutil.disk_usage('/')
    disk_total=int((disk_usage.total)/(1024*1024*1024))
    disk_used=int((disk_usage.used)/(1024*1024*1024))
    disk_free=int((disk_usage.free)/(1024*1024*1024))
    os_version = platform.system() + ' ' + platform.release() + ' - ' + platform.version()
    sensors_battery = psutil.sensors_battery().percent
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    platform_architecture = (platform.architecture())[0]
    python_version = platform.python_version()

    sys_info_dict = {
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'disk_usage_perc': disk_usage_perc,
        'disk_usage': disk_usage,
        'disk_total': disk_total,
        'disk_used': disk_used,
        'disk_free': disk_free,
        'os_version': os_version,
        'sensors_battery': sensors_battery,
        'boot_time': boot_time,
        'platform_architecture': platform_architecture,
        'python_version': python_version
    }

    return render(request, 'system_info.html', sys_info_dict)
