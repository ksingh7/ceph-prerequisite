# ceph-prerequisite

This repository aims to configure systems before deploying Ceph on top of them. This repository should ideally be used before ceph-ansible repository. 

Some of the changes that we are automating using this repository are :

* Add correct pre pouplated /etc/hosts file
* Configure network interface bonds and VLANs for admin, Ceph public and Ceph cluster network
* Add local user sys admins
* Add SSH keys for sys admins

The main playbook which calls all the others is called `site.yml`.

This playbook uses external roles. You need to install them before it will work:
 - install ansible repos with:
    ansible-galaxy install -r requirements.yml
