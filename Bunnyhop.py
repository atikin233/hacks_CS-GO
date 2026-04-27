import pymem
import pymem.process
import keyboard

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

def bhop():
    while True:
        localPlayerInt = pm.read_uint(client + 0xdea964)
        m_fFlags = 0x104
        forceJump = (client + 0x52bbc7c)
        read_jump = pm.read_int(forceJump)
        if keyboard.is_pressed("space"):
            if localPlayerInt:
                on_ground = pm.read_int(localPlayerInt + m_fFlags)
                if on_ground == 257 and read_jump != 5:
                    pm.write_int(forceJump, 5)
                else:
                    pm.write_int(forceJump, 4)

if __name__ == '__main__':
    bhop()
