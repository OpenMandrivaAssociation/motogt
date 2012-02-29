%define		oname MotoGT

Name:		motogt
Version:	20110505
Release:	%mkrel 1
Summary:	MotoGT is a free motorcycle racing game.
License:	GPLv2+
Group:		Games/Arcade
Url:		http://motogt.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/motogt/%{oname}-%{version}.zip
Source2:	motogt.desktop
Source3:	MotoGT.png
Patch0:		motogt-makefile.patch
Patch1:		motogt-savedir.patch
Patch2:		motogt-init.patch
BuildRequires:	sfml-audio-devel
BuildRequires:	sfml-graphics-devel
BuildRequires:	sfml-system-devel
BuildRequires:	sfml-window-devel
%rename		%{oname}

%description
MotoGT is 2D top-viewed game where you drive a MotoGP bike, and you want to win races. 
In career mode you start with a regular bike, but when you win races you get experience, 
and experience let's you improve your bike.
If you win championships, you can also unlock hidden features.

%prep
%setup -q -n %{oname}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%setup_compile_flags
%make

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_libdir}/%{oname}
%__mkdir_p %{buildroot}%{_datadir}/applications
%__mkdir_p %{buildroot}%{_iconsdir}
%__install -Dm 755 %{oname}.bin -D %{buildroot}%{_libdir}/%{oname}/
%__install -Dm 644 %{SOURCE2} -D %{buildroot}%{_datadir}/applications/
%__install -Dm 644 %{SOURCE3} -D %{buildroot}%{_iconsdir}/
%__cp -rf data %{buildroot}%{_libdir}/%{oname}
%__cp -rf data_low %{buildroot}%{_libdir}/%{oname}
%__cp -rf doc %{buildroot}%{_libdir}/%{oname}

%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
pushd %{_libdir}/%{oname}
./%{oname}.bin
popd
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/%{oname}/%{oname}.bin
%{_libdir}/%{oname}/data
%{_libdir}/%{oname}/data_low
%{_libdir}/%{oname}/doc
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{oname}.png

