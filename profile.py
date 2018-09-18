"""This is a trivial example of a gitrepo-based profile; The profile source code and other software, documentation, etc. are stored in in a publicly accessible GIT repository (say, github.com). When you instantiate this profile, the repository is cloned to all of the nodes in your experiment, to `/local/repository`. 

This particular profile is a simple example of using a single raw PC. It can be instantiated on any cluster; the node will boot the default operating system, which is typically a recent version of Ubuntu.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

x = 1
num_of_nodes = 4

# Create a list of nodes, will add all existing nodes
nodeList = list()

# Append all existing nodes into nodeList
for n in range(num_of_nodes):
     nodeList.append(request.XenVM("node-" + str(n)))

# Specify tthe disk image
for node in nodeList:
     node.disk_image = "urn:publicid:IDN+emulad.net+image+emulab-ops:CENTOS7-64-STD"
     node.addService(pg.Execute(shell="sh", command="sudo /local/repository/silly.sh"))
     if x:
          node.routable_control_ip = "true"

# Create another list for custom IPAddresses
address = list()

lan = request.LAN("lan")
address = list()
for m in range(len(nodeList)):
	address.append (nodeList[m].addInterface("if1"))
    	address[m].component_id = "eth1"
	address[m].addAddress(pg.IPv4Address("192.168.1.{}".format(str(m)),"255.255.255.0"))
	lan.addInterface(address[m])

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
