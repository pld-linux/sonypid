#
Summary:	Sony Vaio SPIC Daemon (enables jog dial mouse wheel)
Name:		sonypid
Version:	1.9.1
Release:	1
License:	GPL
Group:		Applications/System
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	http://popies.net/sonypi/%{name}-%{version}.tar.bz2
# Source0-md5:	d27cf0f34132f1b0b900bd0415a79181
URL:		http://popies.net/sonypi/

%description
This daemon enables the jog dial on a Sony VAIO as a mouse wheel.

%prep
%setup -q -n %{name}-%{version}

%build
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d
install sonypid $RPM_BUILD_ROOT%{_sbindir}
install sonypid.xinitrc $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/sonypid
%post
grep 'alias char-major-10-250 sonypi' /etc/modules.conf > /dev/null
RETVAL=$?
if [ $RETVAL -ne 0 ]; then
	echo 'alias char-major-10-250 sonypi' >> /etc/modules.conf
	echo 'options sonypi minor=250' >> /etc/modules.conf
fi

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %{_sbindir}/sonypid
%attr(0755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/sonypid
%doc AUTHORS CHANGES
