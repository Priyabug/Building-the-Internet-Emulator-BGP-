as151 = base.createAutonomousSystem(151)

#Create an internal network
as151.createNetwork('net0')

#Create a host and attach it to the network
as151.createHost('host0').joinNetwork('net0')

#Create a router and attach it to two networks
as151.createRouter('router0').joinNetwork('net0').joinNetwork('1x100')
