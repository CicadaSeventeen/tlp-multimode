%define __brp_suse_args --exclude /etc/tlp.d/99-tlp-multimode.conf
Name:           tlp-multimode
Version:        0.3.3
Release:        1%{?dist}
Summary:        multi-mode switcher for tlp
License:        BSD-3
URL:            https://github.com/CicadaSeventeen/tlp-multimode
Source0:        %{name}-1.tar.gz

BuildRequires:  gcc
BuildRequires:  bash
BuildRequires:  crystal
Requires:       bash
Requires:       tlp
Requires:       ruby
#Recommends:     kf6-breeze-icons
Suggests:       kf6-breeze-icons

%description
A switcher tools to enable multi-mode choice on the top of tlp

%prep
%setup -q -n %{name}-1

%build
bash rubytrans.sh tlp-multimode-switch.script all
crystal build tlp-multimode-switch.cr -o tlp-multimode-switch.bin

%install
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libexecdir}
install -d -m 755 %{buildroot}%{_datadir}
install -d -m 755 %{buildroot}%{_datadir}/applications
install -d -m 755 %{buildroot}%{_unitdir}
install -p -m 6755 tlp-multimode-switch.bin %{buildroot}%{_libexecdir}/tlp-multimode-switch.bin
install -p -m 755 tlp-multimode-switch.rb %{buildroot}%{_libexecdir}/tlp-multimode-switch.rb
install -p -m 755 tlp-multimode-ctl %{buildroot}%{_bindir}/tlp-multimode-ctl
install -p -m 755 tlp-multimode-fix %{buildroot}%{_bindir}/tlp-multimode-fix
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/power-saver
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/balanced
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/performance
install -p -m 755 modes/power-saver/tlp.conf %{buildroot}%{_sysconfdir}/%{name}/power-saver/tlp.conf
install -p -m 755 modes/balanced/tlp.conf %{buildroot}%{_sysconfdir}/%{name}/balanced/tlp.conf
install -p -m 755 modes/performance/tlp.conf %{buildroot}%{_sysconfdir}/%{name}/performance/tlp.conf
install -p -m 755 modes/power-saver/pre_script %{buildroot}%{_sysconfdir}/%{name}/power-saver/pre_script
install -p -m 755 modes/balanced/pre_script %{buildroot}%{_sysconfdir}/%{name}/balanced/pre_script
install -p -m 755 modes/performance/pre_script %{buildroot}%{_sysconfdir}/%{name}/performance/pre_script
install -p -m 755 modes/power-saver/post_script %{buildroot}%{_sysconfdir}/%{name}/power-saver/post_script
install -p -m 755 modes/balanced/post_script %{buildroot}%{_sysconfdir}/%{name}/balanced/post_script
install -p -m 755 modes/performance/post_script %{buildroot}%{_sysconfdir}/%{name}/performance/post_script
install -p -m 644 applications/tlp-multimode-powersave.desktop %{buildroot}%{_datadir}/applications/tlp-multimode-powersave.desktop
install -p -m 644 applications/tlp-multimode-balance.desktop %{buildroot}%{_datadir}/applications/tlp-multimode-balance.desktop
install -p -m 644 applications/tlp-multimode-performance.desktop %{buildroot}%{_datadir}/applications/tlp-multimode-performance.desktop
install -p -m 644 applications/tlp-multimode.desktop %{buildroot}%{_datadir}/applications/tlp-multimode.desktop
install -p -m 644 tlp-multimode-init.service %{buildroot}%{_unitdir}/tlp-multimode-init.service
cd %{buildroot}/%{_bindir}
ln -s tlp-multimode-ctl tlpmmctl


%post
if [ ! -e /run/tlp-multimode ]
then
    mkdir -p /run/tlp-multimode
fi
if [ ! -e /etc/tlp.d ]
then
    mkdir -p /etc/tlp.d
fi
ln -s /run/tlp-multimode/active/tlp.conf /run/tlp-multimode/tlp.conf
ln -s /run/tlp-multimode/tlp.conf /etc/tlp.d/99-tlp-multimode.conf

%postun
unlink /run/tlp-multimode/active/tlp.conf
unlink /run/tlp-multimode/tlp.conf
rm -rf /run/tlp-multimode

%files
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/balanced
%dir %{_sysconfdir}/%{name}/performance
%dir %{_sysconfdir}/%{name}/power-saver
%config(noreplace) %{_sysconfdir}/%{name}/power-saver/tlp.conf
%config(noreplace) %{_sysconfdir}/%{name}/power-saver/pre_script
%config(noreplace) %{_sysconfdir}/%{name}/power-saver/post_script
%config(noreplace) %{_sysconfdir}/%{name}/balanced/tlp.conf
%config(noreplace) %{_sysconfdir}/%{name}/balanced/pre_script
%config(noreplace) %{_sysconfdir}/%{name}/balanced/post_script
%config(noreplace) %{_sysconfdir}/%{name}/performance/tlp.conf
%config(noreplace) %{_sysconfdir}/%{name}/performance/pre_script
%config(noreplace) %{_sysconfdir}/%{name}/performance/post_script
#%license COPYING
%{_libexecdir}/tlp-multimode-switch.bin
%{_libexecdir}/tlp-multimode-switch.rb
%{_bindir}/tlp-multimode-ctl
%{_bindir}/tlp-multimode-fix
%{_bindir}/tlpmmctl
%{_datadir}/applications/tlp-multimode.desktop
%{_datadir}/applications/tlp-multimode-powersave.desktop
%{_datadir}/applications/tlp-multimode-balance.desktop
%{_datadir}/applications/tlp-multimode-performance.desktop
%{_unitdir}/tlp-multimode-init.service

%changelog
