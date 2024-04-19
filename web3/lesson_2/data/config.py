import os
import sys
from pathlib import Path


pk = '0xeb6e7e98a5d86228b598cb85ea064123378f9d7d5997b56237c30f9221627353'

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

ABIS_DIR = os.path.join(ROOT_DIR, 'data', 'abis')