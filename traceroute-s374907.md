# Perform a traceroute to www.google.com
```
traceroute to www.google.com (216.58.211.4), 30 hops max, 60 byte packets
 1  Quiescent.mshome.net (172.27.160.1)  0.207 ms  0.249 ms  0.245 ms
 2  192.168.0.1 (192.168.0.1)  2.039 ms  2.033 ms  2.564 ms
 3  * * *
 4  cm-84.208.24.252.get.no (84.208.24.252)  3.286 ms  3.660 ms  3.654 ms
 5  109-163-76-160.telia-isp.no (109.163.76.160)  3.294 ms  3.665 ms  4.013 ms
 6  oso-b1-link.ip.twelve99.net (62.115.175.156)  3.978 ms  3.623 ms  3.614 ms
 7  s-bb1-link.ip.twelve99.net (62.115.116.101)  10.402 ms  15.340 ms  15.328 ms
 8  s-b2-link.ip.twelve99.net (62.115.140.215)  9.989 ms  9.977 ms  9.970 ms
 9  72.14.205.198 (72.14.205.198)  11.115 ms 72.14.219.132 (72.14.219.132)  10.529 ms 72.14.196.176 (72.14.196.176)  9.656 ms
10  * * *
11  142.250.239.184 (142.250.239.184)  9.608 ms 209.85.242.82 (209.85.242.82)  10.530 ms 142.251.48.44 (142.251.48.44)  9.597 ms
12  209.85.241.29 (209.85.241.29)  11.063 ms muc03s13-in-f4.1e100.net (216.58.211.4)  11.103 ms 108.170.254.34 (108.170.254.34)  11.607 ms
```
# Explain how traceroute discovers a path to a remote host
> Traceroute reveals the each hop the packet has to go through to reach it's destination

Traceroute does this by sending as many packets (max of 30 in this case) till reaches it's destination. Each packet has an increasing TTL (time to live). What happens is that our computer sends a packet with a TTL to google, however the packet dies at the first hop, so our first destionation sends a ICMP message back of "life exceeded". Thus the IP of the first hop is revealed. We just do this incemetially till the packet reaches the destination and then we have our full traceroute.