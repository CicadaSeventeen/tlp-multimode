Name:           tlp-multimode
Version:        0.1
Release:        1%{?dist}
Summary:        multi-mode switcher for tlp
License:        BSD
URL:            https://github.com/hirak99/yabsnap
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  bash
BuildRequires:  crystal
Requires:       bash
Requires:       tlp
Requires:       python3

%description
A switcher tools to enable multi-mode choice on the top of tlp

%prep
%setup -q -n %{name}-%{version}

%build
bash rubytrans.sh tlp-multimode-switch.script cr
crystal build tlp-multimode-switch.cr

%install
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 755 %{buildroot}%{_sysconfdir}/tlp.d
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 6755 tlp-multimode-switch %{buildroot}%{_bindir}/tlp-multimode-switch
#ln -s %{buildroot}%{_datadir}/%{name}/tlp-multimode-switch %{buildroot}%{_datadir}/%{name}/tlpmmctl
install -p -m 755 tlp-multimode-set-default %{buildroot}%{_bindir}/tlp-multimode-set-default
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


%files
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
%{_bindir}/tlp-multimode-switch
%{_bindir}/tlp-multimode-set-default


%changelog
