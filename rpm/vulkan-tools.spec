# Based on Fedora packaging

Name:           vulkan-tools
Version:        1.3.270
Release:        1
Summary:        Vulkan tools
License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-Tools
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
#BuildRequires:  glslang
BuildRequires:  ninja
BuildRequires:  python3-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)

%description
Vulkan tools

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
#cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DGLSLANG_INSTALL_DIR=%{_prefix}
%cmake . \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_CUBE=OFF \
  -DBUILD_WSI_DIRECTFB_SUPPORT=OFF \
  -DBUILD_WSI_XCB_SUPPORT=OFF \
  -DBUILD_WSI_XLIB_SUPPORT=OFF
%ninja_build

%install
%ninja_install

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/*
