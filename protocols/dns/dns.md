# General
- resolvers read from right to left
- **@** is a substitute for **$ORIGIN**


# DNS Record Types (only the common ones)

- **A** 		: IPv4 address. Maps hostname -> IP
- **AAAA** 		: IPv6 address. Maps hostname -> IP
- **CNAME** 	: Canonical name. Alias of one name to another. 
- **MX** 		: Maps domain to a list of message transfer agents (MAIL)
- **NS** 		: Delegate a DNS zone to the authoritative name servers

# Rootservers
- 13 rootservers delegated to the ICANN
- there are obviously more than 13 physical servers
- for each rootserver there are mirrors with the same IP
- --> **anycast**
- return the NS for the given TLD
- asking for *www.leonmortenrichter.de* will return the address of the name server responsible for *.de*
 
 Rootservers are at the top of the DNS hierarchy. Also they don't have a formal name, their label is an empty string. So all FQDN's can be regarded as ending with that empty string. So I can access `www.leonmortenrichter.de` under `www.leonmortenrichter.de.`. 


# TLD-Servers
- second place in the DNS hierarchy
- manage TLD's like *.de*
- resolve domain to NS
- asking for *www.leonmortenrichter.de* will answer with the address of the NS responsible for *leonmortenrichter.de*

# Domain-Level Name Server = Authoritative Name Server
- provides actual answer to my query and returns the IP (**A record**)
- **Master Server**: stores the master copies of all zone records. slaves are updated via a special updating mechanism of the DNS protocol. 
- **Slave Server** exact replication of master
