
%define short_name beamer
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	A LaTeX class for producing beamer presentations
Name:		tetex-latex-beamer
Version:	2.01
Release:	1
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/latex-beamer/latex-beamer-%{version}.tar.gz
# Source0-md5:	0478c4aecd56f3f4dc8bb4e0df0edd95
Requires:	tetex-latex
Requires:	tetex-latex-xcolor >= 1.06
Requires:	tetex-pgf >= 0.60
Requires(post,postun):	/usr/bin/texhash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A LaTeX class for producing beamer presentations.

%prep
%setup -q -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install */*.{cls,sty} $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc doc/*.pdf
%{_datadir}/texmf/tex/latex/%{short_name}
