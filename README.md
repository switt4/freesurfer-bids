# freesurfer-bids
Snakemake BIDS app for FS 7.1 recon-all, uses the snakebids package for running snakemake workflow as bids app

## Install:
pip install -e git+https://github.com/akhanf/freesurfer-bids#egg=freesurfer-bids

## Dry run:
freesurfer-bids BIDS OUTPUT participant -np

## Run using all cores:
freesurfer-bids BIDS OUTPUT participant --cores all

## Or submit jobs using an exection profile (cc-slurm for compute canada):
freesurfer-bids BIDS OUTPUT participant --profile cc-slurm

Note: install instructions for cc-slurm here https://github.com/khanlab/cc-slurm, see https://github.com/Snakemake-Profiles for others
