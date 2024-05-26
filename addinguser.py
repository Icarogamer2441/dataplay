import subprocess

username = input("What's your name? > ")
email = input("What's your email? > ")
password = input("What's your password? >")

with open("example.datplay", "a") as ex:
    ex.write(f"\nuser=USERNAME=\"{username}\"EMAIL=\"{email}\"PASSWORD=\"{password}\"")

pythontype = input("you use 'python3' or 'python'? > ")
if pythontype == "python3":
    subprocess.run("python3 dataplay.py example.datplay user", shell=True)
elif pythontype == "python":
    subprocess.run("python dataplay.py example.datplay user", shell=True)
else:
    print("i only now 'python3' and 'python'!")
