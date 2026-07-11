%global tl_name tcldoc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.40
Release:	%{tl_revision}.1
Summary:	Doc/docstrip for tcl
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tclldoc
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tcldoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tcldoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tcldoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The tclldoc package and class simplify the application of the
doc/docstrip style of literate programming with Dr. John Ousterhout's
Tool Command Language (Tcl, pronounced "tickle", a.k.a. The Cool
Language). The tclldoc package is a bit like the doc package is for
LaTeX, whereas the tclldoc class more parallels the ltxdoc class.

