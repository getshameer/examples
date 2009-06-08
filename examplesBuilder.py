import os, sys

cwd = os.getcwd();
success = 1;
logDir = cwd + "/../../build/logs";

if os.path.isdir(logDir):
  os.system("rm -r " + logDir)
  os.rmdir(cwd + "/../../build")
os.mkdir(cwd + "/../../build")
os.mkdir(logDir);
logFile = open(logDir + "/log.txt","w")
compiler = sys.argv[1];
failedExample = '';

def buildExample(path) :
  global failedExample, success, compiler, logDir;
  os.chdir(path)
  err=0
  if compiler == 'gnu' :
    err=os.system("make COMPILER=gnu > " + logDir + "/" + path.replace('/', '_')+ " 2>&1")
  elif compiler == 'intel' :
    err=os.system("make > " + logDir + "/" + path.replace('/', '_') + " 2>&1")
  if err==0 :
    logFile.write(path.replace('/', '_')+'=success\n') 
  else :
    success=0
    logFile.write(path.replace('/', '_')+'=fail\n') 
    failedExample += path.replace('/', ' - ') + ' '
  os.chdir(cwd)
  return;

buildExample("ClassicalField/AnalyticLaplace")
buildExample("ClassicalField/Diffusion")
buildExample("ClassicalField/Helmholtz")
buildExample("ClassicalField/Laplace")
buildExample("ClassicalField/NonlinearPoisson")

buildExample("Bioelectrics/Monodomain")

buildExample("FluidMechanics/StokesFlow/HexChannel")
buildExample("FluidMechanics/StokesFlow/HexPipe")
buildExample("FluidMechanics/StokesFlow/SingleElement")
buildExample("FluidMechanics/StokesFlow/VesselPipe")

# TODO Group them
buildExample("LagrangeSimplexMesh")
buildExample("LinearElasticity")
buildExample("cellml")
buildExample("Darcy")
buildExample("define-geometry-and-export")
buildExample("FiniteElasticity")
buildExample("MoreComplexMesh")
buildExample("simple-field-manipulation-direct-access")
buildExample("SimplexMesh")
buildExample("TwoRegions")

logFile.close()
if success==0 :
  raise RuntimeError, 'Failed in %s' % (failedExample)


