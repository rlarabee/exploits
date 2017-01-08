#!/usr/bin/python
import sys

PML4_SELF_REF_INDEX = 0x1ed

def get_pxe_address(address):
    entry = PML4_SELF_REF_INDEX;
    result = address >> 9;
    lower_boundary = (0xFFFF << 48) | (entry << 39);
    upper_boundary = ((0xFFFF << 48) | (entry << 39) + 0x8000000000 - 1) & 0xFFFFFFFFFFFFFFF8;
    result = result | lower_boundary;
    result = result & upper_boundary;
    return result

if (len(sys.argv) == 1):
	print "Please enter a virtual address and PML4 self ref index in hex format"
	print "The PML4 self ref index is option, the static idex of 0x1ed will be used"
	print "if one is not entered"
	print ""
	print sys.argv[0] + " 0x1000 0x1ed"
	sys.exit(0)

address = int(sys.argv[1], 16)
if (len(sys.argv) > 2):
	PML4_SELF_REF_INDEX = int(sys.argv[2], 16)

pt = get_pxe_address(address)
pd = get_pxe_address(pt)
pdpt = get_pxe_address(pd)
pml4 = get_pxe_address(pdpt)
selfref = get_pxe_address(pml4)

print "Virtual Address: %s" % (hex(address))
print "Self reference index: %s" % (hex(PML4_SELF_REF_INDEX))
print "\n"
print "Page Tables"
print "Self Ref: \t%s" % (hex(selfref))
print "Pml4:\t\t%s" % (hex(pml4))
print "Pdpt:\t\t%s" % (hex(pdpt))
print "Pd:\t\t%s" % (hex(pd))
print "PT:\t\t%s" % (hex(pt))
