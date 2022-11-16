Name:		texlive-cweb-old
Version:	49271
Release:	1
Summary:	CWEB system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cweb-old
License:	distributable
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb-old.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The CWEB system is a system for literate programming, also known as structured
software documentation, with code written in the C and C++ languages.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/plain/cweb-old

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
