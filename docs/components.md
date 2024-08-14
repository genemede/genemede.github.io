# Components of Genemde

## The GAT

The GAT - Genemede Api and Tools - is a python project meant to be run locally. It will store data and allow for several operations, including search and export.

<div class="gnmd-infobox">
Sometime during the development of Genemede, the GAT will be turned into an installable python package, but for now it needs to be installed and configured as a normal python repository.
</div>

The GAT acts as the brain for all your local functionality. It holds the available metadata types and all the data, it provides an api to interact with it and it also has a set of command line tools to help you manage everything.

### Folders

The first time the GAT runs, it will create a ```genemede``` folder under your local user folder. There you will find this folder structure:

```plaintext
genemede
  ├── data
  ├── logs
  ├── media
  ├── mtypes
  │   ├── imported
  │   └── user
  ├── scratch
  └── config.json
```

```data``` is where all the local data is stored;

```logs``` is where all the operating log files are stored;

```media``` is where all the uploaded files are stored (<span class="gnmd-infotext">(uploading is still under development)</span>);

```mtypes``` holds non-curated metadata types. You can freely create your own metadata types under the ```user``` folder, and the ```imported``` folder is reserved for future use.

```scratch``` holds temporary files, such as exported json files and debug dumps. It is safe to delete anything inside this folder.

### Configuration

These are the contents of the current configuration file:

```json
{
    "json_indent": 4,
    "user": {
        "name": "default user",
        "screen_name": "default user",
        "workspace": "genemede",
        "email": "example@example.com"
    },
    "folders": {
        "user_data": "<homefolder>/genemede/data",
        "user_media": "<homefolder>/genemede/media",
        "user_scratch": "<homefolder>/genemede/scratch",
        "system_mtypes": "<gat_repo_folder>/system/mtypes",
        "user_mtypes": "<homefolder>/genemede/mtypes/user",
        "imported_mtypes": "<homefolder>/genemede/mtypes/imported",
        "global_sources": "<gat_repo_folder>/system/sources",
        "logfiles": "<homefolder>/genemede/logs",
        "user_deleted_data": "<homefolder>/genemede/data/_deleted"
    }
}
```

<div class="gnmd-warningbox">
We don't recommend changing anything except the <code>user</code> section at this time.
</div>

Your ```screen_name``` will be displayed in the GUI, and the GUI will try to use your ```email``` to display a Gravatar image if you have one configured. The ```workspace``` field will be used in the future to differentiate different data workspaces, and the ```name``` field will be used for authentication in the HUB when available.
<div class="gnmd-infobox">
A nicer way to change configuration values is being developed in the GUI, but in the meantime the only way to change configuration values is to edit the json file manually.
</div>

### MTypes

Currently, the Genemede metadata types are included in the GAT itself ([see The Metadata types](#the-metadata-types)).

You can create your own metadata types under the ```user_mtypes``` folder (default <homefolder>/genemede/mtypes/user).

## The GUI

As the functionality of Genemede is relatively complex, it would be unwieldy to work exclusively through a command line interface or API. The GUI app provides a frontend for most of the system functionality, using the underlying GAT api, and storing **no data at all**.

## The HUB

Currently in development, the Genemede HUB will be a central point to share and search data made available by any Genemede user that decides to make their data available to the public.

## The Metadata types

Metadata types are the core of Genemede. Each metadata type defines a field structure and the rules on how a metadata type interacts and links with other types. The Genemede project will maintain a curated list of metadata types tailored for neuroscience but any user can create their own metadata types.

During the initial development phase, the curated metadata types are included in the GAT repository, but will eventually be moved out into their own repository.
