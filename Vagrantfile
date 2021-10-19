Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end

  config.vm.boot_timeout = 600

  #configure provisioners on tha machine
  config.vm.provision :docker
  config.vm.provision :docker_compose

  config.vm.define "server-1" do |server1|
    server1.vm.network "private_network", ip:'192.168.33.60'
    server1.vm.hostname = "server-1"
    server1.vm.provision "shell", inline: <<-SHELL
      apt-get -y update
      apt-get -y install nginx
      service nginx start
    SHELL
  end

  config.vm.define "server-2" do |server2|
    server2.vm.network "private_network", ip:'192.168.33.61'
    server2.vm.hostname = "server-2"
  end

end