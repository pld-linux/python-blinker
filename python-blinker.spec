#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	blinker
Summary:	Fast, simple object-to-object and broadcast signaling
Summary(pl.UTF-8):	Szybkie, proste przesyłanie sygnałów pomiędzy obiektami
Name:		python-%{module}
Version:	1.4
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/blinker/
Source0:	https://files.pythonhosted.org/packages/source/b/blinker/%{module}-%{version}.tar.gz
# Source0-md5:	8b3722381f83c2813c52de3016b68d33
URL:		https://pythonhosted.org/blinker/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
%if %{with doc}
BuildRequires:	python3-flask_sphinx_themes
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.5
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

%package -n python3-%{module}
Summary:	Fast, simple object-to-object and broadcast signaling
Summary(pl.UTF-8):	Szybkie, proste przesyłanie sygnałów pomiędzy obiektami
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
Blinker provides a fast dispatching system that allows any number of
interested parties to subscribe to events, or "signals". Signal
receivers can subscribe to specific senders or receive signals sent by
any sender.

%description -n python3-%{module} -l pl.UTF-8
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
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests
%endif
%endif

%if %{with doc}
sphinx-build-3 -b html docs/source docs/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README.md LICENSE
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README.md LICENSE
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/html/{_static,*.html,*.js}
%endif
