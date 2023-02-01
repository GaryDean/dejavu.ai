import os
import sys
from colorama import init, Fore, Back, Style
from markdown import markdownFromFile
import random

EDITOR = ''
def getEDITOR():
  _ent_EDITOR = os.environ.get('EDITOR')
  EDITOR = os.environ.get('EDITOR')
  if not EDITOR:
    if _ent_EDITOR:
      EDITOR = _ent_EDITOR
    elif os.environ.get('SUDO_EDITOR'):
      EDITOR = os.environ.get('SUDO_EDITOR')
    elif os.environ.get('SELECTED_EDITOR'):
      EDITOR = os.environ.get('SELECTED_EDITOR')
    elif os.path.isfile(os.path.join(os.environ.get('HOME'), '.selected_editor')):
      with open(os.path.join(os.environ.get('HOME'), '.selected_editor')) as f:
        SELECTED_EDITOR = f.read()
      if SELECTED_EDITOR:
        EDITOR = SELECTED_EDITOR
    elif os.path.isfile('/etc/alternatives/editor'):
      EDITOR = '/etc/alternatives/editor'

getEDITOR()
exit()

InputFile = 'README.md'
OutputFile = '/tmp/dejavu-'+''.join(random.choices('qertyuiopxyz1234567890-_',k=12))+'.html'
markdownFromFile(input=InputFile, output=OutputFile)
