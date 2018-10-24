# Centos Dockerfile
FROM centos:7

#Maintainer Name
MAINTAINER BaruaVT

# install openssh
RUN yum -y install openssh-server openssh-clients sshpass
# install python
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y update
RUN yum -y install python36u python36u-libs python36u-devel python36u-pip

# enable pub key authentication
RUN sed -i 's/PermitRootLogin no/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/PubkeyAuthentication no/PubkeyAuthentication yes/' /etc/ssh/sshd_config
CMD systemctl restart sshd.service

# generate keygen
RUN yes y |ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa

# copy keygen
RUN sshpass -p 12345677 ssh-copy-id -o StrictHostKeyChecking=no -f root@35.237.97.128

# Define working directory.
WORKDIR /home/

# Adding Data folder
RUN scp -r root@35.237.97.128:/home/data /home/data/
# Copy Python Script
ADD ./start.py /home/

RUN ls

# Permission
RUN chmod 755 ./start.py
RUN chmod 755 -R ./data

# Run Python Script
RUN python3.6 start.py
