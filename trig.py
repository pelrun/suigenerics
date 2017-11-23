import math

print "sine_table:"
print "defb {}".format(','.join([str(int(round(127*math.sin(bdeg*math.pi/128)))) for bdeg in xrange(0,256)]))
print "cosine_table:"
print "defb {}".format(','.join([str(int(round(127*math.cos(bdeg*math.pi/128)))) for bdeg in xrange(0,256)]))
