# revision 24010
# category Package
# catalog-ctan /info/translations/filecontents/de
# catalog-date 2011-09-18 09:08:24 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-translation-filecontents-de
Version:	20110918
Release:	1
Summary:	German version of filecontents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/filecontents/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-filecontents-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-filecontents-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a "translation" of the filecontents documentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.dtx
%doc %{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.ins
%doc %{_texmfdistdir}/doc/latex/translation-filecontents-de/filecontents-de.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
