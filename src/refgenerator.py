from pathlib import Path
import json
import mkdocs_gen_files
import sys
from dotenv import dotenv_values
from mkdocs.exceptions import PluginError, ConfigurationError

envvalues = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

def envvar(k, dv = None):
    # also considers empty strings as None, to allow for .env to have the key= empty value
    if k in envvalues:
        v = envvalues[k]
        if isinstance(v, str) and v == "":
            v = dv
        return v
    else:
        return dv

class RefMaker:
    def __init__(self):
        self.mtypes_path = None
        self.sources_path = None
        self.mtypes = {}

    def initialize(self):
        # finds path for mtypes and source definitions
        mtp = envvar("MTYPES_PATH", None)
        srcp = envvar("SOURCES_PATH", None)
        print("initialize-------------------------------------")

        ok = False
        if mtp != None and srcp != None:
            try:
                self.mtypes_path = Path(mtp)
                self.sources_path = Path(mtp)
                ok = True
            except Exception as e:
                pass

        if not ok:
            raise PluginError("Invalid paths to MTYPES and SOURCES, please check .env file")

        return ok


    def procFolder(self, folder: Path, ns):
        for f in folder.iterdir():
            if f.is_dir():
                if not f.stem.startswith("_"):
                    fn = Path.joinpath(f, f.stem + ".json")
                    self.procFile(fn)

    def procFile(self, filepath):
        mt = filepath.stem
        rootpath = filepath.parents[0]
        print(rootpath, mt)

        # open main file
        with open(filepath) as json_file:
            data = json.load(json_file)

        data["modules"] = {}
        # open modules
        modpath = Path.joinpath(rootpath, "modules")
        if modpath.is_dir():
            for modfile in modpath.iterdir():
                if modfile.is_file():
                    if not modfile.stem.startswith("_") and modfile.suffix == ".json":
                        with open(modfile) as json_file:
                            moddata = json.load(json_file)
                            if "properties" in data:
                                # only loads module if it has a properties key
                                data["modules"][modfile.stem] = {
                                    "properties": moddata["properties"]
                                }

        self.mtypes[mt] = data

    def makeDoc(self, mtype, data, tofiles = False):
        def addLine(ln):
            nonlocal txt
            txt = txt + ln + "\n"

        if tofiles:
            outputfile = Path("misc/output/ref_" + mtype + ".md")

        txt = ""
        addLine(f"# {mtype}")
        addLine(f"{data['description']}")

        addLine("## Properties")
        for propname in data["properties"]:
            prop = data["properties"][propname]
            addLine(f"#### {propname}")
            addLine(f"description: {prop['description']}")
            #addLine(f"datatype: {prop['description']}")

        #txt = json.dumps(data, indent = 4)
        if tofiles:
            try:
                with open(outputfile, 'w', encoding="utf-8") as fl:
                    fl.write(txt)
            except Exception as e:
                print("Error", e)
        else:
            print("Generating reference for\033[1m", mtype, end="\033[0;0m: ")
            with mkdocs_gen_files.open("reference/mtypes/" + mtype + ".md", "w") as fl:
                print(txt, file=fl)
            print("done.")

    def loadFiles(self):
        self.procFolder(self.mtypes_path, "")

    def makeDocs(self, tofiles=False):
        # all mtypes
        idx = "# Reference\nReference for current metatypes\n---\n"

        for mt in self.mtypes:
            idx = idx + f" - [{mt}]({mt}.md)\n"
            self.makeDoc(mt, self.mtypes[mt], tofiles)

        # reference index file for mtypes
        with mkdocs_gen_files.open("reference/mtypes/index.md", "w") as fl:
            print(idx, file=fl)

        # all sources

        # reference index file for sources





print("======================== START UP =======================================")
# generate reference pages for metatypes (and sources eventually)
ref = RefMaker()
if ref.initialize():
    ref.loadFiles()
    ref.makeDocs(tofiles=False)
