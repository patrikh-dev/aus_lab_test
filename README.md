# Images

```bash
docker pull ubuntu:22.04
docker pull quay.io/frrouting/frr:10.1.0

docker pull ghcr.io/openconfig/gnmic:0.38.2
docker pull quay.io/prometheus/prometheus:v2.54.0
docker pull grafana/grafana:11.1.4
```

# Containerlab
- https://containerlab.dev/install/#quick-setup

```bash
curl -sL https://containerlab.dev/setup | sudo -E bash -s "all"
```

# linux bridge
```bash
sudo ip link add br-clab type bridge
sudo ip link set dev br-clab up
```

# Build
## birdc
- https://bird.network.cz/?get_doc&v=20&f=bird-6.html#ss6.4

```bash
cd birdc && docker build -t birdc:2.15.1 .
```

## gnmic
examples
```bash
./gnmic sub -a 192.168.0.1:57400 --mode stream --stream-mode sample --insecure -u admin -p admin@123 --format prototext --debug --path /network-instances/network-instance/protocols/protocol/bgp/global/state
./gnmic sub -a 192.168.0.1:57400 --mode once --stream-mode sample --insecure -u admin -p admin@123 --format prototext --debug --path /network-instances/
```

# Resources
- https://bird.network.cz/?get_doc&v=20&f=bird-6.html#ss6.4
  - https://packetfire.org/post/intro-to-bgp/
  - https://mellowd.dev/posts/migrating-bird-to-bird2/
  - https://mellowd.dev/posts/migrating-bird-to-bird2-part2/
  - https://mellowd.dev/posts/migrating-bird-to-bird2-part3/
  - https://mellowd.dev/posts/rpkiserver-for-12c-a-year/
  - https://dn42.eu/howto/Bird2
  - https://docs.netx.as/tutorials/bgp/basic-bgp.html
- https://containerlab.dev/manual/kinds/vr-vmx/
- https://github.com/Exa-Networks/exabgp
  - https://thepacketgeek.com/exabgp/
  - https://juliopdx.com/2022/02/25/exabgp-in-the-lab/
  - https://jasonmurray.org/posts/2020/exabgp-fulltable/
- https://docs.frrouting.org/en/latest/bgp.html
- https://gnmic.openconfig.net/
  - https://github.com/openconfig/gnmic/tree/main/examples/deployments
