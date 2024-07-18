import platform
import subprocess
import psutil

def get_system_info():
    """
    Возвращает информацию о системе (имя системы, версию Windows, битность, имя пользователя)
    """
    system_info = {}
    system_info['name'] = platform.system()
    system_info['version'] = platform.release()
    system_info['bitness'] = platform.architecture()[0]
    system_info['user'] = platform.node()
    return system_info

def get_cpu_info():
    """
    Возвращает информацию о процессоре (количество ядер, частоту, производителя)
    """
    cpu_info = {}
    cpu_info['cores'] = psutil.cpu_count()
    cpu_info['freq'] = psutil.cpu_freq().max
    cpu_info['manufacturer'] = psutil.cpu_info().manufacturer
    return cpu_info

def get_ram_info():
    """
    Возвращает информацию об оперативной памяти (общее количество, используемое количество)
    """
    ram_info = {}
    ram_info['total'] = psutil.virtual_memory().total
    ram_info['used'] = psutil.virtual_memory().used
    return ram_info

def shutdown(timeout=0):
    """
    Выключает компьютер (параметр timeout - время ожидания в секундах перед выключением)
    """
    subprocess.run(['shutdown', '/s', '/t', str(timeout)])

def restart(timeout=0):
    """
    Перезагружает компьютер (параметр timeout - время ожидания в секундах перед перезагрузкой)
    """
    subprocess.run(['shutdown', '/r', '/t', str(timeout)])
