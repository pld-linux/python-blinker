#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests

%define 	module	blinker
Summary:	Fast, simple object-to-object and broadcast signaling
Summary(pl.UTF-8):	Szybkie, proste przesyłanie sygnałów pomiędzy obiektami
Name:		python-%{module}
# keep 1.5 here for python2 support
Version:	1.5
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/blinker/
Source0:	https://files.pythonhosted.org/packages/source/b/blinker/%{module}-%{version}.tar.gz
# Source0-md5:	e1c3eec8e52210f69ef59d299c6cca07
URL:		https://pythonhosted.org/blinker/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
%endif
%if %{with doc}
BuildRequires:	python3-flask_sphinx_themes
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blinker provides a fast dispatching system that allows any number of
interested parties to subscribe to events, or "signals". Signal
receivers can subscribe to specific senders or receive signals sent by
any sender.

%description -l pl.UTF-8
Blinker dostarcza szybki system rozporowadzania sygnałów, który
pozwala na dowolną liczbę odbiorców zdarzeń czy sygnałów. Odbiorcy
sygnałów mogą zapisywać się do wybranych nadawców lub odbierać sygnały
nadadane przez wszystkich nadawców.

%package apidocs
Summary:	Blinker API documentation
Summary(pl.UTF-8):	Dokumentacja API modułu Blinker
Group:		Documentation

%description apidocs
API documentation for Blinker.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Blinker.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with tests}
nosetests-%{py_ver} tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.rst README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_images,_static,*.html,*.js}
%endif
