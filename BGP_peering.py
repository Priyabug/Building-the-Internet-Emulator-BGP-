ebgp    = Ebgp()

# Peer AS-2 with ASes 151, 152, and 153 (AS-2 is the Internet service provider)
ebgp.addPrivatePeering(100, 2, 151, abRelationship = PeerRelationship.Provider)
ebgp.addPrivatePeering(101, 2, 152, abRelationship = PeerRelationship.Provider)
ebgp.addPrivatePeering(101, 2, 153, abRelationship = PeerRelationship.Provider)

# Peer AS-152 and AS-153 (as equal peers for mutual benefit)
ebgp.addPrivatePeering(101, 152, 153, abRelationship = PeerRelationship.Peer)
