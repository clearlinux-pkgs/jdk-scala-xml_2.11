Name     : jdk-scala-xml_2.11
Version  : 1.0.4
Release  : 3
URL      : http://repo1.maven.org/maven2/org/scala-lang/modules/scala-xml_2.11/1.0.4/scala-xml_2.11-1.0.4.jar
Source0  : http://repo1.maven.org/maven2/org/scala-lang/modules/scala-xml_2.11/1.0.4/scala-xml_2.11-1.0.4.jar
Source1  : http://repo1.maven.org/maven2/org/scala-lang/modules/scala-xml_2.11/1.0.4/scala-xml_2.11-1.0.4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: jdk-scala-xml_2.11-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-scala-xml_2.11 package.
Group: Data

%description data
data components for the jdk-scala-xml_2.11 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/scala-xml_2.11.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/scala-xml_2.11.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/scala-xml_2.11.xml \
%{buildroot}/usr/share/maven-poms/scala-xml_2.11.pom \
%{buildroot}/usr/share/java/scala-xml_2.11.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/scala-xml_2.11.jar
/usr/share/maven-metadata/scala-xml_2.11.xml
/usr/share/maven-poms/scala-xml_2.11.pom
