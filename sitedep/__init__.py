
import os

SiteDep = None

# Compute paths at import time
try:
  __configRoot = os.environ['AUTOPXE_CONFIG']
except KeyError:
  __configRoot = os.path.dirname(__file__)

__sitedepPath = __configRoot

def sitedepPath():
  return __sitedepPath

def _init():
  global SiteDep
  import os

  cfg_files = ["config.yml", "distro_specific.yml"]

  # make sure all .yml files are readable and have no syntax erors
  SiteDep = dict()
  for cfg_file in cfg_files:
    cfg = sitedepPath() + '/' + cfg_file
    if not os.path.exists(cfg):
      raise RuntimeError('AutoPXE config file is a broken link or does not '\
                         'exist:\n%s\n' % cfg)
    import yaml
    tmp = yaml.load(open(cfg, 'r'))
    if tmp == None:
        raise RuntimeError('AutoPXE config file is empty, or invald YAML: '\
                           '\n%s\n' % cfg)
    SiteDep.update(tmp)


_init()
