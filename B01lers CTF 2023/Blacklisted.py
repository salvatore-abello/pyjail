blacklist = "._0x/|?*[]{}<>\"'=()\\\t "
blacklist2 = ['eval', 'exec', 'compile', 'import', 'os', 'sys', 'cat', 'ls', 'exit', 'list', 'max', 'min', 'set', 'tuple']

def validate(code):
    for char in blacklist:
        if char in str(code):
            return False
    for word in blacklist2:
        if word in str(code):
            return False
    return True

if __name__ == '__main__':
    print("------------------------------")
    print("Welcome to my very cool python interpreter! \nI hope I blacklisted enough... \nYou can never be too careful with these things...")
    print("Send an empty line to run!")
    print("------------------------------")
    safe_code = ""
    while (True):
        unsafe_code = input(">>> ")
        if (unsafe_code == ""):
            try:
                exec(safe_code)
            except:
                print("Error executing!")
            break
        unsafe_code = unsafe_code.replace("open", "")
        unsafe_code = unsafe_code.replace("print", "")
        if (not validate(unsafe_code)):
            print("Invalid code!")
            continue
        safe_code += str(unsafe_code)+ "\n"
