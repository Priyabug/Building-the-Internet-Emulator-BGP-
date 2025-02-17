<h1>Launching BGP network on one of the autonomous system</h1>

<h2>Description</h2>
Border Gateway Protocol (BGP) is the standard exterior gateway protocol designed to exchange routing and reachability information among autonomous systems (AS) on the Internet. It is the "glue" of the Internet, and is an essential piece of the Internet infrastructure. It is also a primary target of attacks, because if attackers can compromise BGP, they can cut off the Internet.

Here we will see how BGP "glues" the Internet together, and how the Internet is actually connected. This lab is based on the Internet Emulator that we developed. We have conducted a series of experiments on the Emulator to see how BGP works. We will also configure a stub and a transit autonomous system. We will eventually launch a network prefix hijacking attack on one of the autonomous systems.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b>
- <b>Bash</b>
- <b>Docker and Docker Compose</b>
- <b>BIRD Internet Routing Daemon</b>
- <b>tcpdump</b>
- <b>Linux Command-Line Utilities</b>
- <b>SEED Internet Emulator Web Interface</b>
- <b>Ununtu 20.04 VM</b>

<h2>Environments Used </h2>

- <b>Windows 10</b> (21H2)

<h2>Program walk-through:</h2>

- <b>Task 1:</b> Stub Autonomous System<br>
     <b>Task 1.a:</b> Understanding AS-155’s BGP Configuration<br>
     <b>Task 1.b:<b>  Observing BGP UPDATE Messages<br>
     <b>Task 1.c:<b>  Experimenting with Large Communities<br>
     <b>Task 1.d:<b>  Configuring AS-180<br>
- <b>Task 2:</b> Transit Autonomous System<br>
     <b>Task 2.a:</b> Experimenting with IBGP<br>
     <b>Task 2.b:</b> Experimenting with IGP<br>
     <b>Task 3:</b> Path Selection<br>
     <b>Task 4:</b>IP Anycast<br>
