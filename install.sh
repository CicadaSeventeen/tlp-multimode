#!/bin/bash
install -d -m 755 /etc/tlp-multimode
install -d -m 755 /etc/tlp.d
install -d -m 755 /etc/tlp-multimode/power-saver
install -d -m 755 /etc/tlp-multimode/balanced
install -d -m 755 /etc/tlp-multimode/performance
install -p -m 6755 tlp-multimode-switch.bin /usr/libexec/tlp-multimode-switch.bin
install -p -m 755 tlp-multimode-switch.rb /usr/libexec/tlp-multimode-switch.rb
install -p -m 755 tlp-multimode-ctl /usr/bin/tlp-multimode-ctl
install -p -m 755 tlp-multimode-fix /usr/bin/tlp-multimode-fix
install -p -m 755 modes/power-saver/tlp.conf /etc/tlp-multimode/power-saver/tlp.conf
install -p -m 755 modes/balanced/tlp.conf /etc/tlp-multimode/balanced/tlp.conf
install -p -m 755 modes/performance/tlp.conf /etc/tlp-multimode/performance/tlp.conf
install -p -m 755 modes/power-saver/pre_script /etc/tlp-multimode/power-saver/pre_script
install -p -m 755 modes/balanced/pre_script /etc/tlp-multimode/balanced/pre_script
install -p -m 755 modes/performance/pre_script /etc/tlp-multimode/performance/pre_script
install -p -m 755 modes/power-saver/post_script /etc/tlp-multimode/power-saver/post_script
install -p -m 755 modes/balanced/post_script /etc/tlp-multimode/balanced/post_script
install -p -m 755 modes/performance/post_script /etc/tlp-multimode/performance/post_script
install -p -m 644 applications/tlp-multimode-powersave.desktop /usr/share/applications/tlp-multimode-powersave.desktop
install -p -m 644 applications/tlp-multimode-balance.desktop /usr/share/applications/tlp-multimode-balance.desktop
install -p -m 644 applications/tlp-multimode-performance.desktop /usr/share/applications/tlp-multimode-performance.desktop
install -p -m 644 applications/tlp-multimode.desktop /usr/share/applications/tlp-multimode.desktop
install -p -m 644 tlp-multimode-init.service /usr/lib/systemd/system/tlp-multimode-init.service
cd /usr/bin
ln -s tlp-multimode-ctl tlpmmctl
cd /etc/tlp.d
ln -s /run/tlp-multimode/tlp.conf 99-tlp-multimode.conf
