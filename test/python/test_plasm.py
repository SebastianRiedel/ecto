#!/bin/python

import ecto
#from ecto.doc import printModuleDoc
import buster

def test_plasm():
    scatter = ecto.make(buster.Scatter, n=10, x=10)
    gather = ecto.make(buster.Gather, n=10)
#    printer = ecto.make(buster.Printer)
#    ecto.printModuleDoc(scatter)
#    ecto.printModuleDoc(gather)
    print "#################\nPlasm test\n#################"
    plasm = ecto.Plasm()
    for f, t in zip(ecto.keys(scatter.outputs), ecto.keys(gather.inputs)):
            plasm.connect(scatter, f, gather, t)
    plasm.go(gather)
    result = gather.o.out.get()
    print "gather out (should be 100):", result
    assert(result == 100)
    #print plasm.viz()

if __name__ == '__main__':
    test_plasm()



