import sys
import json

users = {}
chat = {}
types = {}

def interpret(code, type_):
    lines = code.split("\n")

    for line in lines:
        if type_ == "user":
            if line.startswith("user"):
                username = line.split("=USERNAME=\"")[1].split("\"EMAIL=\"")[0].strip("\"\'")
                email = line.split("\"EMAIL=\"")[1].split("\"PASSWORD=\"")[0].strip("\"\'")
                password = line.split("\"PASSWORD=\"")[1].split("\"")[0].strip("\"\'")
                users[username] = {"email": email, "password": password}
        elif type_ == "chat":
            if line.startswith("chat"):
                username = line.split("=USERNAME=\"")[1].split("\"MESSAGE=\"")[0].strip("\"\'")
                message = line.split("\"MESSAGE=\"")[1].split("\"")[0].strip("\"\'")
                chat[username] = {"message": message}
        elif type_ == "types":
            if line.startswith("types"):
                name = line.split("=NAME=\"")[1].split("\"TYPE=\"")[0].strip("\"\'")
                datatype = line.split("\"TYPE=\"")[1].split("\"")[0].strip("\"\'")
                types[name] = {"datatype": datatype}
    
    if type_ == "user":
        finalusers = json.dumps(users, indent=4)
        with open("users.json", "w") as fi:
            fi.write(finalusers)
    elif type_ == "chat":
        finalchats = json.dumps(chat, indent=4)
        with open("chat.json", "w") as fi:
            fi.write(finalchats)
    elif type_ == "types":
        finaltypes = json.dumps(types, indent=4)
        with open("types.json", "w") as fi:
            fi.write(finaltypes)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <file> <type>")
        print("types:")
        print("user")
        print("chat")
        print("types")
    else:
        if sys.argv[1].endswith(".datplay"):
            with open(sys.argv[1], "r") as f:
                interpret(f.read(), sys.argv[2])
