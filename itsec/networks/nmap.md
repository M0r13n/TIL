# NMAP

## Open Closed Filtered
- remember the three way handshake: **SYN - SYN/ACK - ACK**
- **filtered**	: port does not respond(no service or dropped by FW)
- **closed**	: host responds with **RST ACK** (host is reachable, but port is unused)
- **open**		: host responds with **SYN/ACK** indicating a running service

## NMAP answers with RST
- nmap answers with RST to prevent the host from resending it's packet

## Stealth Scanning (-sS)
- TCP SYN Scanning
- fast and unobtrusive
- therefore it's the default
- SYN scan:
	1. **Attacker**	: send SYN to host:port
	2. **Target**	: respond with SYN/ACK or RST or not at all
	3. **Attacker**	: Answers with RST 
- if target does not respond, nmap repeats step 1.
- add `--packet-trace` for verbose output

## Connect Scan (-sT)
- alternative for SYN Scanning when user does not have raw packet privileges
- nmap asks the OS to craft the packets
- uses connect sys call
- **ALWAYS PREFER TCP SYN SCANNING**

## UDP Scan (-sU)
- used to test UDP services
- for example DNS on port 53
- UDP is unreliable, which introduces problems and makes scanning slow

## SCTP INIT (-sY)
- used for SS7/SIGTRAN
- **SCTP equivalent of a TCP SYN scan**
- unobtrusive and stealthy
- half opening 

## TCP NULL, FIN, Xmas (-sN, -sF, -sX)
- exploit RFC 793, page 65
- Null: send not bits (TCP flag header = 0)
- FIN: set TCP FIN bit
- FIN, PSH, and URG: --> Christmas tree

## Examples
- `nmap -sP 10.0.0.0/24` : scan the network with pings
- `nmap -p 1-65535 -sV -sS -T4 target` : TCP Scan of all ports with version detection @target
- `nmap -v -sS -A -T4 target` : verose stealth scanning of target including OS and version detection
- `nmap -iL list-of-ips.txt` : scan target from text file
- `nmap 192.168.1.1-20` :  scan a ip range
