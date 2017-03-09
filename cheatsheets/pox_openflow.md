# class ofp\_flow\_mod - Creating OpenFlow rules

Instances of `ofp_flow_mod` are messages that are sent to the switch
(openflow device) and tell it to modify the rules in its Flow Table.


This is the class definition with some of its fields and their default values:


```python
class ofp_flow_mod (ofp_header):
    def __init__(self, **kw):
        self.match = None
        self.header_type = OFPT_FLOW
        self.cookie = 0
        self.command = OFPFC_ADD
        self.idle_timeout = 0
        self.hard_timeout = 0
        self.priority = OFP_DEFAULT_PRIORITY
        self.out_port = OFPP_NONE
        self.flags = 0
        self.actions = []

```

## Creating and sending a flow_mod message


```python
my_flow_mod = of.ofp_flow_mod()

# modify the fields as needed
my_flow_mod.match = my_match
my_flow_mod.actions.append(my_action)

# send the message to the switch
connection.send(my_flow_mod)
```

## ofp\_flow\_mod Reference

- cookie(int): identifier for the flow rule (optional)
- command (int): One of the following values:
  - OFPFC_ADD - add a rule (default)
  - OFPFC_MODIFY - modify an existing rule
  - OFPFC_DELETE - delete a rule
  - other values are available in the spec
- idle\_timeout (int) - rule will expire if not used for idle\_timeout seconds
- hard\_timeout (int) - rule will expire after hard\_timeout seconds
- priority (int) - the rules with higher priority match against packets first
- actions (list) - A list of actions that will be applied when the rule matches
  - empty list -> drop the packet
  - one action -> do one thing
  - multiple actions -> do multiple things
- match (ofp\_match) - the match structure for the rule to match on (see below)

# class ofp\_action\_output - Using OpenFlow rules to output the packet to a port

Class definition:

```python
class ofp_action_output(object):
    def __init__(self):
        self.port = None # Purposely bad --require specification

```

## Output back to the input port

```python
my_action = of.ofp_action_output()
my_action.port = of.OFPP_IN_PORT
```

## ofp\_action\_output Reference

Here are some of the various port constants given by the openflow spec and the POX library:

- OFPP\_IN\_PORT - Send the packet back out to the port it came in from
- OFPP\_NORMAL - Process via the legacy L2/L3 switch configuration (if
  available, switch dependent.) Useful for hybrid switches.
- OFPP\_FLOOD - output to all openflow ports except the input port and those with flooding disabled
- OFPP\_ALL - output to all openflow ports except the input port
- OFPP_CONTROLLER - Send to the controller
- OFPP_NONE - Output to nowhere


# class ofp\_match - Tell a rule which packets to match against

An `ofp\_match` object holds a set of values that defines a set of
headers for packets to be matched against.


Some of the available attributes are summarized here:

## Create a match object

```python
my_match = of.ofp_match()
my_match.in_port = 6
```

**IMPORTANT**
If you want to match against an L3 packet, you need to set dl_type like so:

    my_match.dl_type = 0x800

## Match Reference

Here is a list of fields that can be matched in a packet header:

| Attribute     | Meaning                                                    |
| ------------- | ---------------------------------------------------------- |
| in_port       | Switch port number the packet arrived in                   |
| dl\_src       | Ethernet source address                                    |
| dl\_dst       | Ethernet destination address                               |
| dl\_vlan      | VLAN ID                                                    |
| dl\_vlan\_pcp | VLAN priority                                              |
| dl\_type      | Ethertype/length (e.g. 0x800 => IPv4)                      |
| nw\_tos       | IP TOS/DS bits                                             |
| nw\_proto     | IP protocol (e.g., 6 => TCP) or lower 8 bits of ARP opcode |
| nw\_src       | IP source address                                          |
| nw\_dst       | IP destination address                                     |
| tp\_src       | TCP/UDP source port                                        |
| tp\_dst       | TCP/UDP destination port                                   |

# Result

Looking back, we can see that my\_flow\_mod is a message that will
configure a switch so that all packets that arrive from port 6 will be
sent back to port 6.
