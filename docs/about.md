# Genemede

## What is Genemede

Genemede aims to provide the means to build ontologies for general purpose data, in turn allowing the creation of a comprehensive ontology for describing neuroscience research projects, along with a set of tools to record, search and interact with data using standardized rules. Using a common ontology for data will allow communities to easily search and share information.

It is comprised of the following components:

### The GAT

The GAT - Genemede Api and Tools - is a python project meant to be run locally. It will store data and allow for several operations, including search and export.

[Repository at github](https://github.com/genemede/gnmd-gat){:target="_blank"}

More in-depth information [here](components.md#the-gat).

### The GUI

The GUI is a Web Application used to interact with the GAT APIs.

[Repository at github](https://github.com/genemede/gnmd-gui){:target="_blank"}

It is a vue.js application, and you can build it yourself or you can use our own public deployment [here](https://genemede.github.io/gnmd-gui/){:target="_blank"}

More in-depth information [here](components.md#the-gui).

### The HUB

<span class="gnmd-warning">(in development)</span>
The HUB is an online platform meant to facilitate the exchange of information such as ontologies.

[Repository at github](https://github.com/genemede/gnmd-hub){:target="_blank"}

More in-depth information [here](components.md#the-hub).

### The Genemede Metatypes

(in development)
This is a collection of officially curated metatypes by the Genemede project.

[Repository at github](https://github.com/genemede/gnmd-mtypes){:target="_blank"}

More in-depth information [here](components.md#the-metadata-types).

## What can Genemede do

- Create researchers, subjects, projects and labs;
- Edit relationships between created objects;
- Search data and view relationships;
- Export all data as a Genemede json file.

## How to install Genemede

### Installing the GAT

Download the repository via github `git clone https://github.com/genemede/gnmd-gat` and follow the instructions on the README file.

### Installing and building the GUI

Download the repository via github `git clone https://github.com/genemede/gnmd-gui` and follow the instructions on the README file.
