# -*- mode: ruby -*-
# vi: set ft=ruby :

# This script was adopted from https://github.com/illotum/vagrant-mininet/

$init = <<SCRIPT
  sudo apt-get update
  sudo apt-get install -y build-essential \
   libssl-dev \
   python-all python-twisted-conch git tmux vim python-pip python-paramiko \
   python-sphinx openjdk-8-jdk
  sudo pip install alabaster
  echo 'export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"' >> ~/.profile
  source ~/.profile
SCRIPT

# $ovs = <<SCRIPT
#   wget http://openvswitch.org/releases/openvswitch-2.3.2.tar.gz
#   tar xf openvswitch-2.3.2.tar.gz
#   pushd openvswitch-2.3.2
#   DEB_BUILD_OPTIONS='parallel=8 nocheck' fakeroot debian/rules binary
#   popd
#   sudo dpkg -i openvswitch-common*.deb openvswitch-datapath-dkms*.deb \
#    python-openvswitch*.deb openvswitch-pki*.deb openvswitch-switch*.deb \
#    openvswitch-controller*.deb
# SCRIPT

# $mininet = <<SCRIPT
#   git clone git://github.com/mininet/mininet
#   pushd mininet
#   git checkout -b 2.2.1 2.2.1
#   sudo ./util/install.sh -fn
#   popd
# SCRIPT
$mininet = <<SCRIPT
  sudo apt-get -y install mininet
SCRIPT

# $onos = <<SCRIPT
#   wget --quiet http://downloads.onosproject.org/release/onos-1.6.0.tar.gz
#   tar xzf onos-1.6.0.tar.gz
#   rm onos-1.6.0.tar.gz
# SCRIPT
$onos = <<SCRIPT
  git clone https://gerrit.onosproject.org/onos
  pushd onos
  git checkout 1.6.0
  popd
SCRIPT

$gurobi = <<SCRIPT
  wget --quiet http://packages.gurobi.com/6.5/gurobi6.5.2_linux64.tar.gz
  tar xzf gurobi6.5.2_linux64.tar.gz
  rm gurobi6.5.2_linux64.tar.gz
  pushd gurobi652/linux64
  sudo python setup.py install
  popd
  echo 'export GUROBI_HOME="$HOME/gurobi652/linux64"' >> ~/.profile
  echo 'export PATH="${PATH}:${GUROBI_HOME}/bin"' >> ~/.profile
  echo 'export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"' >> ~/.profile
  source ~/.profile
SCRIPT

$sol = <<SCRIPT
  sudo pip install numpy cython msgpack-python networkx requests netaddr six bitstring
SCRIPT

$tmgen = <<SCRIPT
  git clone https://github.com/progwriter/TMgen
  pushd TMgen
  sudo pip install .
  popd
SCRIPT

$cleanup = <<SCRIPT
  sudo apt-get clean
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"

  config.vm.provider "VirtualBox" do |v|
      v.customize ["modifyvm", :id, "--memory", "2048"]
  end

  ## Guest config
  config.vm.hostname = "solvm"
  # config.vm.network :private_network, ip: "192.168.0.100"
  config.vm.network :forwarded_port, guest:6633, host:6633 # OpenFlow
  config.vm.network :forwarded_port, guest:8181, host:8181 # Web UI
  config.vm.network :forwarded_port, guest:8080, host:8080 # ONOS REST API

  ## Provisioning
  config.vm.provision :shell, privileged: false, :inline => $init
  config.vm.provision :shell, privileged: false, :inline => $onos
  config.vm.provision :shell, privileged: false, :inline => $gurobi
  config.vm.provision :shell, privileged: false, :inline => $tmgen
  config.vm.provision :shell, privileged: false, :inline => $sol
  config.vm.provision :shell, privileged: false, :inline => $cleanup

  ## SSH config
  config.ssh.forward_x11 = false

  ## Folder config, for dev versions
  config.vm.synced_folder ".", "/sol"

end
