Summary:	Pulseaudio visualization
Summary(pl.UTF-8):	Wizualizacja dla Pulseaudio
Name:		projectM-pulseaudio
Version:	2.0.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/projectm/%{name}-%{version}-Source.tar.gz
# Source0-md5:	3b6cad16f93617cdb073fc61dd48ccec
Patch0:		%{name}-pulse.patch
Patch1:		%{name}-include.patch
URL:		http://projectm.sourceforge.net/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	cmake >= 2.4.0
BuildRequires:	libprojectM-devel >= 1:2.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	projectM-qt-devel >= 1:2.0.1
BuildRequires:	pulseaudio-devel >= 0.9.8
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	libprojectM >= 1:2.0.1
Requires:	projectM-qt >= 1:2.0.1
Requires:	pulseaudio-libs >= 0.9.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pulseaudio visualization using projectM.

%description -l pl.UTF-8
Wizualizacja dla Pulseaudio wykorzystująca projectM.

%prep
%setup -q -n %{name}-%{version}-Source
%patch0 -p1
%patch1 -p1

%build
# note: this project doesn't support separate build dir (expects generated include in source dir)
%cmake .

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog 
%attr(755,root,root) %{_bindir}/projectM-pulseaudio
%{_desktopdir}/projectM-pulseaudio.desktop
