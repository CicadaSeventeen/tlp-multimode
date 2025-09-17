#!/bin/bash
SCRIPT_DIR=$(dirname "${BASH_SOURCE[0]}")
#bash ${SCRIPT_DIR}/rubytrans.sh tlp-multimode-switch.script all
bash ${SCRIPT_DIR}/rubytrans.sh tlp-multimode.script cr
crystal build tlp-multimode-switch.cr
sudo chown root:root tlp-multimode-switch
sudo chmod 6755 tlp-multimode-switch
ln -s tlp-multimode-switch tlpmmctl
