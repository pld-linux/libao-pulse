Summary:	PulseAudio plugin for libao
Summary(pl.UTF-8):	Wtyczka PulseAudio dla libao
Name:		libao-pulse
Version:	0.9.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/libao-pulse/%{name}-%{version}.tar.gz
# Source0-md5:	0f5b7fbed418c158703cb5657004d385
URL:		http://0pointer.de/lennart/projects/libao-pulse/
BuildRequires:	libao-devel >= 0.8.5
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.2
Requires:	libao >= 0.8.5
Obsoletes:	libao-polyp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libao-pulse is a libao driver for the PulseAudio sound server.

%description -l pl.UTF-8
libao-pulse to sterownik libao dla serwera dźwięku PulseAudio.

%prep
%setup -q

%build
%configure \
	--disable-lynx \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/ao/plugins-2/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/ao/plugins-2/libpulse.so
