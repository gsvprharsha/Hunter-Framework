import vulnscanner


def hunt_vuln():
    target_ip = input("[#] Enter the target to scan for vulnerable open ports: ")
    port_number = int(input("Enter the range of ports to scan(500 for first 500 ports): "))
    vulnerable_file = input("[+]Enter Path to file containing vulnerable softwares: ")
    print("\n")

    target = vulnscanner.Port_scan(target_ip, port_number)
    target.scan()

    with open(vulnerable_file, 'r') as file:
        count = 0
        for banner in target.banner:
            file.seek(0)
            for line in file.readlines():
                if line.strip() in banner:
                    print('[!!] VULNERABLITY FOUND "' + banner + '" ON PORT: ' + str(target.open_ports[count]))
            count += 1