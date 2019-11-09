%global _prefix /usr/local

Name:    simulate-slower-network
Version: 0.2
Release: 1
Summary: Simulates a low bandwidth, high-latency network connection

Group:   Development Tools
License: ASL 2.0
Source0: simulate-slower-network

%description
This bash script offers quick shortcuts to simulate slower network connections.
It is useful when you need to simulate a wireless network on a Linux network server,
especially when you are using a virtual machine guest on your local machine or in the cloud.

%install
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
