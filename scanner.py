import nmap

target_ip = "192.168.40.1"  # Replace with your target IP
scanner = nmap.PortScanner()

# Perform TCP scan on ports 1–1024
scanner.scan(target_ip, '1-1024', '-v')

# Display the results
for host in scanner.all_hosts():
    print("----------------------------------------------------")
    print("Host: {} ({})".format(host, scanner[host].hostname()))
    print("----------------------------------------------------")

    for protocol in scanner[host].all_protocols():
        print("Protocol: {}".format(protocol))
        ports = scanner[host][protocol]
        for port_num, port_info in ports.items():
            print("Port: {}\tState: {}\tService: {}".format(
                port_num, port_info['state'], port_info.get('name', 'N/A')))
