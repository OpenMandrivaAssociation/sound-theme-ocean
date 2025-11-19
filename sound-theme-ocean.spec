%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name:		sound-theme-ocean
Version:	6.5.3
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/ocean-sound-theme/-/archive/%{gitbranch}/ocean-sound-theme-%{gitbranchd}.tar.bz2#/ocean-sound-theme-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/ocean-sound-theme-%{version}.tar.xz
%endif
Summary:	The Ocean sound theme
URL:		https://kde.org/
License:	GPL
Group:		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildArch:	noarch

%description
The Ocean sound theme

%prep
%autosetup -p1 -n ocean-sound-theme-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/sounds/ocean
