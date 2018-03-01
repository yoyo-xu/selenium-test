#print 有10种类型的人，有些是binary，有些不是
x="There are %d types of people." %10

binary = "binary"

do_not = "don't"

y = "Those who know %s and those who %s" %(binary,do_not)

print x
print y

#print 我说 :"有10种类型的人"，我也说：'有些是binary，有些不是'
print "I said: %r." %x
print "I also said: '%s'." %y

hilarious = False

joke_evaluation="Isn't that joke so funny?! %r"

#print 这不是很好笑的笑话吗？！False
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#print This is the left side of a string with a right side
print w + e
