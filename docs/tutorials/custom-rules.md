# Writing Custom Suricata Rules

## Rule Syntax
```
alert protocol src_ip src_port -> dst_ip dst_port (options)
```

## Example
```
alert tcp any any -> $HOME_NET 22 (msg:"SSH Brute Force"; 
  threshold:type threshold, track by_src, count 10, seconds 60; 
  sid:9000001;)
```

## Testing
```bash
sudo suricata-update
sudo systemctl reload suricata
```
