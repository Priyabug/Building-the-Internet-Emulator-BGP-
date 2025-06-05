# File: init_autonomous_system.py

# -------------------------------------------
# BGP SEED Emulator - Autonomous System Setup
# -------------------------------------------

from seed_emulator import Base  # Ensure the SEED framework is installed and accessible

# Initialize the base network
base = Base()

# Create Internet Exchange Points
base.createInternetExchange(100)
base.createInternetExchange(101)

# Create a stub Autonomous System with AS number 151
as151 = base.createAutonomousSystem(151)

# Create an internal network inside AS151
as151.createNetwork('net0')

# Create a host and connect it to the internal network
as151.createHost('host0').joinNetwork('net0')

# Create a router and attach it to both an internal network and an IXP
# The router connects 'net0' (internal) and 'ix100' (public exchange)
as151.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')

# Print confirmation
print("✅ Autonomous System 151 setup complete.")
print("   - Network 'net0', Host 'host0', and Router 'router0' created and connected.")
