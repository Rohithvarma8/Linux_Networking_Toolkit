# Linux Networking Toolkit

## Overview
This project showcases the implementation of essential networking and security components using Linux, addressing the needs of a start-up company in Boston. The project integrates DNS, DHCP, web server setup, firewall security, VPN configuration, and automated backup solutions.

## Features
- **DNS Implementation**:
  - Master-Slave DNS setup with Bind9.
  - Support for forward and reverse lookups (IPv4 and IPv6).
  - Automatic synchronization between Master and Slave DNS.

- **DHCP Configuration**:
  - Dynamic IP allocation using IPv4 and IPv6.
  - Address reservation and exclusion ranges.

- **Web Server Setup**:
  - Apache2 configured with virtual hosting.
  - Fail2Ban for intrusion prevention.
  - Secure connection with SSL/TLS certificates.

- **Firewall Configuration**:
  - IP filtering and protocol-based rules using UFW and iptables.
  - Blocking unauthorized access.

- **Backup System**:
  - Automated backup process with compression.
  - Secure transfer of backup files to a remote server using `rsync`.

- **VPN Implementation**:
  - Secure VPN tunnel using StrongSwan.
  - Integration with NFS for secure file sharing.

- **MITM Attack Demonstration**:
  - ARP poisoning implemented with Scapy to simulate a man-in-the-middle attack.

## Project Topology
- **VM1**: DHCP + Master DNS
- **VM2**: Slave DNS
- **VM3**: Webserver + Firewall
- **VM4**: Backup Server
- **VM5**: Test Backup Server
- **VM6**: Attacker (MITM)
- **VM7**: Test Client Server
- **VM8**: VPN Server
- **VM9**: VPN Client

## Requirements
- **Operating System**: Ubuntu
- **Tools and Libraries**:
  - Bind9 for DNS
  - Apache2 for Web Server
  - Fail2Ban for security
  - StrongSwan for VPN
  - Scapy for MITM
  - `tar`, `gzip`, `rsync` for Backup

## Setup
1. **Network Configuration**:
   - Assign static IPs and set up DHCP for dynamic allocation.
   - Define IP addressing scheme for each VM.

2. **DNS**:
   - Configure forward and reverse zones for IPv4 and IPv6.
   - Set up Master and Slave DNS synchronization.

3. **DHCP**:
   - Define address pool, reservations, and exclusions.
   - Test dynamic IP allocation with a client.

4. **Web Server**:
   - Configure Apache2 with a virtual host.
   - Secure the server with UFW and SSL/TLS.

5. **Backup**:
   - Create automated backup scripts.
   - Transfer compressed files to a remote server.

6. **VPN**:
   - Establish a VPN tunnel between server and client.
   - Integrate with NFS for secure file sharing.

## Testing
1. Verify dynamic IP allocation with the DHCP server.
2. Test domain name resolution using Master and Slave DNS.
3. Access the hosted web page from a client.
4. Confirm firewall rules block unauthorized access.
5. Validate VPN tunnel functionality with file sharing.

## Future Enhancements
- Expand DNS and DHCP for larger networks.
- Implement redundancy for DNS and DHCP.
- Enhance backup encryption and automation.
- Integrate Zero Trust Architecture with VPN.

## Contributors
- **You Li**
- **Badrinath Rohith Varma Datla**
- **Cheng Yu-Chang**

## References
- [Linux DNS Configuration Guide](https://phoenixnap.com/kb/ubuntu-dns-nameservers)
- [Man-in-the-Middle Attack Explanation](https://www.imperva.com/learn/application-security/man-in-the-middle-attack-mitm/)
- [StrongSwan VPN Setup](https://strongswan.org/)
