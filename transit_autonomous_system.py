as2 = base.createAutonomousSystem(2)

# Create 3 internal networks
as2.createNetwork('net0')
as2.createNetwork('net1')
as2.createNetwork('net2')

# Create four routers and attach them to networks. 
# ix100 <--> r1 <--> r2 <--> r3 <--> r4 <--> ix101
as2.createRouter('r1').joinNetwork('net0').joinNetwork('ix100')
as2.createRouter('r2').joinNetwork('net0').joinNetwork('net1')
as2.createRouter('r3').joinNetwork('net1').joinNetwork('net2')
as2.createRouter('r4').joinNetwork('net2').joinNetwork('ix101')
