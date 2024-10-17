%define		oname MotoGT

Name:		motogt
Version:	20110505
Release:	5
Summary:	Free motorcycle racing game
License:	GPLv2+
Group:		Games/Arcade
Url:		https://motogt.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/motogt/%{oname}-%{version}.zip
Source2:	motogt.desktop
Source3:	MotoGT.png
Patch0:		motogt-makefile.patch
Patch1:		motogt-savedir.patch
Patch2:		motogt-init.patch
Patch3:		motogt-png15.patch
BuildRequires:	sfml-audio-devel
BuildRequires:	sfml-graphics-devel
BuildRequires:	sfml-system-devel
BuildRequires:	sfml-window-devel
BuildRequires:	pkgconfig(glu)
%rename		%{oname}

%description
MotoGT is 2D top-viewed game where you drive a MotoGP bike, and you want
to win races. In career mode you start with a regular bike, but when you
win races you get experience, and experience let's you improve your bike.
If you win championships, you can also unlock hidden features.

%prep
%setup -q -n %{oname}
%patch0 -p1 -b .makefile~
%patch1 -p1 -b .savedir~
%patch2 -p1 -b .init~
%patch3 -p1 -b .png15~

%build
%setup_compile_flags
%make

%install
mkdir -p %{buildroot}%{_libdir}/%{oname}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_iconsdir}
install -Dm 755 %{oname}.bin -D %{buildroot}%{_libdir}/%{oname}/
install -Dm 644 %{SOURCE2} -D %{buildroot}%{_datadir}/applications/
install -Dm 644 %{SOURCE3} -D %{buildroot}%{_iconsdir}/
cp -rf data %{buildroot}%{_libdir}/%{oname}
cp -rf data_low %{buildroot}%{_libdir}/%{oname}
cp -rf doc %{buildroot}%{_libdir}/%{oname}

# 32 bit binary linked against old libs
rm -f %{buildroot}%{_libdir}/%{oname}/data/src/bikes/hue.bin

mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
pushd %{_libdir}/%{oname}
./%{oname}.bin
popd
EOF

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/%{oname}/%{oname}.bin
%{_libdir}/%{oname}/data
%{_libdir}/%{oname}/data_low
%{_libdir}/%{oname}/doc
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{oname}.png


%changelog
* Wed Feb 29 2012 Andrey Bondrov <abondrov@mandriva.org> 20110505-1mdv2011.0
+ Revision: 781446
- Update patches
- imported package motogt

