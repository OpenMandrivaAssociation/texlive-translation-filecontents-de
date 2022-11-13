Name:		texlive-translation-filecontents-de
Version:	24010
Release:	1
Summary:	German version of filecontents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/filecontents/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-filecontents-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-filecontents-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a "translation" of the filecontents documentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.dtx
%doc %{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.ins
%doc %{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
