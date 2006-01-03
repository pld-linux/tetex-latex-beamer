#
# TODO:
# - package emacs and LyX files
#
%define	short_name	beamer
%define	texhash		[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;
#
Summary:	A LaTeX class for producing beamer presentations
Summary(pl):	Klasa LaTeXa do tworzenia prezentacji rzutnikowych
Name:		tetex-latex-beamer
Version:	3.06
Release:	1
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/latex-beamer/latex-beamer-%{version}.tar.gz
# Source0-md5:	ab7eeb972d75e758117460aabdddb1e6
Requires:	tetex-latex
Requires:	tetex-latex-xcolor >= 2.00
Requires:	tetex-pgf >= 0.95
Requires(post,postun):	/usr/bin/texhash
URL:		http://latex-beamer.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A LaTeX class for producing beamer presentations.

%description -l pl
Klasa LaTeXa do tworzenia prezentacji rzutnikowych.

%package examples
Summary:	Example presentations created using the LaTeX Beamer class
Summary(pl):	Przyk�adowe prezentacje stworzone z wykorzystaniem klasy LaTeX Beamer
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}-%{release}

%description examples
Example presentations created using the LaTeX Beamer class.

%description examples -l pl
Przyk�adowe prezentacje stworzone z wykorzystaniem klasy LaTeX Beamer.

%prep
%setup -q -n latex-%{short_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/texmf/tex/latex/%{short_name},%{_examplesdir}/%{name}-%{version}}

cp -ar base emulation extensions themes $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

cp -ar examples/* solutions $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog doc/*.pdf README TODO
%{_datadir}/texmf/tex/latex/%{short_name}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}