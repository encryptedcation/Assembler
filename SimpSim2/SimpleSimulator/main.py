import sys
from mem import memHandler
from progCounter import PC
from simEngine import execRunner
from plotCycle import plotter


sim = execRunner()
memFile = memHandler()
memFile.load(sys.stdin)
pc = PC()
memPlot = plotter(pc)
halted = False

while not halted:
    newInstruction = memFile.getInst(pc.COUNTER)
    pc.dump()
    newPC, halted = sim.execute(newInstruction, memFile)
    memPlot.update(newInstruction)
    pc.update(newPC)

memFile.dump()
memPlot.plot()
