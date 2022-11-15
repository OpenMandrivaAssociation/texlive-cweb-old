Name:		texlive-cweb-old
Version:	49271
Release:	1
Summary:	
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cweb-old
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb-old.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description

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
