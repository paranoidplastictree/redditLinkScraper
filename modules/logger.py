from datetime import datetime, timezone

def error(message):
    __log("ERROR", message)

def warn(message):
    __log("WARN", message)

def info(message):
    __log("INFO", message)

def __log(level, message):
    now = datetime.now(timezone.utc).strftime("%c")
    log_msg = "{} {}: {}\n".format(now, level, message)
    
    file_name = "{}.log".format(datetime.now(timezone.utc).strftime("%Y_%m_%d"))
    f = open(file_name, "a")
    f.write(log_msg)
    f.close()