from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def launch ():
  """
  Launch is the entry point of the module, much like __main__
  """

  # Register the hub_component to the system
  core.registerNew(HubComponent)

class HubComponent(object):
	'''
	The hub component is the handler of opendlow events for our 
	application
	'''
	def __init__(self):
		log.info("Starting HubComponent")
		
		# Make the hub component a listener to openflow events
		core.openflow.addListeners(self)
	
	def _handle_ConnectionUp(self, event):
		log.info("Creating hub device on %s", event.connection)
		
		# Create a new Hub on the device having this connection
		Hub(event.connection)

class Hub(object):
	'''
	The Hub class is instantiated once for each openflow device
	that connects to the hub component. The hub class tranforms the
	said device to an ethernet hub
	'''
	def __init__(self, connection):
		log.info("Created hub on switch %s", connection)
		
