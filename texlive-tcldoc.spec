Name:		texlive-tcldoc
Version:	22018
Release:	2
Summary:	Doc/docstrip for tcl
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tclldoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcldoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcldoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcldoc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tclldoc package and class simplify the application of the
doc/docstrip style of literate programming with Dr. John
Ousterhout's Tool Command Language (Tcl, pronounced "tickle",
a.k.a. The Cool Language). The tclldoc package is a bit like
the doc package is for LaTeX, whereas the tclldoc class more
parallels the ltxdoc class.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tcldoc/tcldoc.cls
%{_texmfdistdir}/tex/latex/tcldoc/tcldoc.sty
%{_texmfdistdir}/tex/latex/tcldoc/tclldoc.cls
%{_texmfdistdir}/tex/latex/tcldoc/tclldoc.sty
%doc %{_texmfdistdir}/doc/latex/tcldoc/README.txt
%doc %{_texmfdistdir}/doc/latex/tcldoc/examples/README.txt
%doc %{_texmfdistdir}/doc/latex/tcldoc/examples/parsetcl.dtx
%doc %{_texmfdistdir}/doc/latex/tcldoc/examples/parsetcl.ins
%doc %{_texmfdistdir}/doc/latex/tcldoc/examples/pdf.dtx
%doc %{_texmfdistdir}/doc/latex/tcldoc/examples/pdf.ins
%doc %{_texmfdistdir}/doc/latex/tcldoc/tclldoc.pdf
%doc %{_texmfdistdir}/doc/latex/tcldoc/tools/README.txt
%doc %{_texmfdistdir}/doc/latex/tcldoc/tools/eemenu.dtx
%doc %{_texmfdistdir}/doc/latex/tcldoc/tools/eemenu.ins
%doc %{_texmfdistdir}/doc/latex/tcldoc/tools/sourcedtx.dtx
%doc %{_texmfdistdir}/doc/latex/tcldoc/tools/sourcedtx.ins
#- source
%doc %{_texmfdistdir}/source/latex/tcldoc/tclldoc.dtx
%doc %{_texmfdistdir}/source/latex/tcldoc/tclldoc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
