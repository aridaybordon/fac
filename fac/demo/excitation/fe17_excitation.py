"""calculate the electron impact excitation cross sections
"""

# import the modules
import config
import fac

fac.SetAtom('Fe')
# 1s shell is closed
config.closed('1s')
config.config('2*8', group = 'n2')
config.config('2*7 3*1', group = 'n3')

# Self-consistent iteration for optimized central potential
fac.SetScreening([10])
fac.OptimizeRadial('n2', 'n3')
fac.Structure()
fac.LevelTable('ne.lev')

fac.SetUsrCEGrid([1.0E2, 2.5E3])
fac.CETable(['n2'], ['n3'], 'ne.ce')

