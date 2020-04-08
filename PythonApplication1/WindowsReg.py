import winreg
import sys


print("Returning information about a key in 3 items \nIndex number:\n0 An integer giving the number of sub keys this key has. \n1 An integer giving the number of values this key has.\n2 An integer giving when the key was last modififed (if available) as 100's of nanoseconds since Jan 1, 1601.\n")
print("HKEY_CLASSES_ROOT")
print(winreg.QueryInfoKey(winreg.HKEY_CLASSES_ROOT))
print("\nHKEY_CURRENT_USER")
print(winreg.QueryInfoKey(winreg.HKEY_CURRENT_USER))
print("\nHKEY_LOCAL_MACHINE")
print(winreg.QueryInfoKey(winreg.HKEY_LOCAL_MACHINE))
print("\nHKEY_USERS")
print(winreg.QueryInfoKey(winreg.HKEY_USERS))
print("\nHKEY_PERFORMANCE_DATA")
print(winreg.QueryInfoKey(winreg.HKEY_PERFORMANCE_DATA))

