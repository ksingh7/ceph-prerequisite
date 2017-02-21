# ceph-prerequisite

This repository aims to configure systems before deploying Ceph on top of them. This repository should ideally be used before ceph-ansible repository. 

Some of the changes that we are automating using this repository are:

* Add correct pre pouplated /etc/hosts file
* Configure network interface bonds and VLANs for admin, Ceph public and Ceph cluster network
* Add local user sys admins
* Add SSH keys for sys admins
* Add opsview/collectd monitoring

This repo also has the logic to update HP / Dell firmwares. This is not a part of the default site.yml playbook, it has to be run separately.

The main playbook which calls all the others is called `site.yml`.

Setup:

    ansible-galaxy install -r requirements.yml

Run:

    ansible-playbook -i inventories/$HOSTS_FILE -c ssh site.yml

To upgrade firmware:
    ansible-playbook -i inventories/$HOSTS_FILE firmware-update.yml -l LIMIT_TO THESE_SERVERS

You should be careful with running the firmware update playbook. Test the firmware updates on a subset of similar test HW before running against production.
