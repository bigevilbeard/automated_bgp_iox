import sys
import cli


print "\n\n *** Shutting Down BGP Session  *** \n\n"
cli.configurep(["router bgp 100","neighbor 10.1.2.2 shutdown", "end"])

print "\n\n *** Show BGP Status  *** \n\n"
cli.executep('show bgp summary')
