Summary:	Apache server-status viewer
Name:		ftss
Version:	0.9.3
Release:	1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://fabletech.com/ftss-download/%{name}-%{version}.tar.gz
# Source0-md5:	2a8a364a87e1b9f310e3b068e2f20fe5
URL:		http://fabletech.com/ftss
BuildRequires:	apache-devel
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Apache server-status viewer from "name based" shared memory segment
setup in apache for the scoreboard.

%prep
%setup -q

%build
%configure \
	CFLAGS="%{rpmcppflags} $(%{_bindir}/apu-1-config --includes)" \
	--with-apr-config=%{_bindir}/apr-1-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/ftss
