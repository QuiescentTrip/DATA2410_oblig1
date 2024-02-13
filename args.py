import argparse

lower_limit = 1024
upper_limit = 65535

def check_port(val):
    try:
        value = int(val)
    except ValueError:
        raise argparse.ArgumentTypeError('Expected an integer but you entered a string')
    
    if not lower_limit <= value <= upper_limit:
        raise argparse.ArgumentTypeError(f"Invalid port. It must be within the range [{lower_limit},{upper_limit}]")

    return value

def check_ip(val):
    split = val.split(".") 
    if len(split) != 4:
        raise argparse.ArgumentTypeError("The IP needs to be written in standard format")
    for num in split:
        try:
            if not 0 <= int(num) <= 255:
                raise argparse.ArgumentTypeError("The IP needs to be written in standard format")
        except ValueError:
             raise argparse.ArgumentTypeError("The IP address should only contain numbers.")

    return val

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="positional arguments", epilog="end of help")
    parser.add_argument('-s', '--server', action='store_true', help="Run in server mode")
    parser.add_argument('-c', '--client', action='store_true', help="Run in client mode")
    parser.add_argument('-p', '--port', type=check_port, default=8088, help="Port number")
    parser.add_argument('-i', '--ip', type=check_ip, default="10.0.0.2", help="IP address")

    args = parser.parse_args()
    
    if args.server and args.client:
        parser.error("You cannot use both server and client mode at the same time.")

    if not args.server and not args.client:
        parser.error("You should run either in server or client mode.")

    mode = "server" if args.server else "client"
    print(f"The {mode} is running with IP address = {args.ip} and port address = {args.port}")
