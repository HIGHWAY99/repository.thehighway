""" downloaded from http://xbmc-addons.googlecode.com/svn/addons/ """
""" addons.xml generator """

""" Modified by Rodrigo@XMBCHUB to zip plugins/repositories to a "zip" folder """
""" This file is "as is", without any warranty whatsoever. Use as own risk """



import os
import md5
import zipfile
import shutil
from xml.dom import minidom
import glob
import datetime

class Generator:
    global zippath
    """
        EDIT THE ZIP PATH TO YOUR LIKING.
        Don't add the ending /
    """
    zippath = 'zips'








    """
        Generates a new addons.xml file from each addons addon.xml file
        and a new addons.xml.md5 hash file. Must be run from the root of
        the checked-out repo. Only handles single depth folder structure.
    """


    def __init__( self ):

        # generate files
        self._generate_addons_file()
        self._generate_md5_file()
        self._generate_zip_files()
        # notify user
        print "Finished updating addons xml, md5 files and zipping addons"

    def _generate_zip_files ( self ):
        addons = os.listdir( "." )
        # loop thru and add each addons addon.xml file
        for addon in addons:
            try:
                # skip any file or .git folder
                if ( not os.path.isdir( addon ) or addon == ".git" or addon == zippath): continue
                # create path
                _path = os.path.join( addon, "addon.xml" )
                # split lines for stripping
                document = minidom.parse(_path)
                for parent in document.getElementsByTagName("addon"):
                    version = parent.getAttribute("version")
                    addonid = parent.getAttribute("id")
                self._generate_zip_file(addon, version, addonid)
            except Exception, e:
                print e

    def _generate_zip_file ( self, path, version, addonid):
        filename = path + "-" + version + ".zip"
        try:
            zip = zipfile.ZipFile(filename, 'w')
            for root, dirs, files in os.walk(path + "\\"):
                for file in files:
                    zip.write(os.path.join(root, file))
            zip.close()
            if os.path.isfile(zippath + "\\" + addonid + "\\" + filename):
                os.rename(zippath + "\\" + addonid + "\\" + filename, zippath + "\\" + addonid + "\\" + filename + "." + datetime.datetime.now().strftime("%Y%m%d%H%M%S") )
            shutil.move(filename, zippath + "\\" + addonid + "\\")
        except Exception, e:
            print e

    def _generate_addons_file( self ):
        # addon list
        addons = os.listdir( "." )
        # final addons text
        addons_xml = u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<addons>\n"
        # loop thru and add each addons addon.xml file
        for addon in addons:
            try:
                # skip any file or .git folder
                if ( not os.path.isdir( addon ) or addon == ".git" ): continue
                # create path
                _path = os.path.join( addon, "addon.xml" )
                # split lines for stripping
                xml_lines = open( _path, "r" ).read().splitlines()
                # new addon
                addon_xml = ""
                # loop thru cleaning each line
                for line in xml_lines:
                    # skip encoding format line
                    if ( line.find( "<?xml" ) >= 0 ): continue
                    # add line
                    addon_xml += unicode( line.rstrip() + "\n", "utf-8" )
                # we succeeded so add to our final addons.xml text
                addons_xml += addon_xml.rstrip() + "\n\n"
            except Exception, e:
                # missing or poorly formatted addon.xml
                print "Excluding %s for %s" % ( _path, e, )
        # clean and add closing tag
        addons_xml = addons_xml.strip() + u"\n</addons>\n"
        # save file
        self._save_file( addons_xml.encode( "utf-8" ), file="addons2.xml" )

    def _generate_md5_file( self ):
        try:
            # create a new md5 hash
            m = md5.new( open( "addons2.xml" ).read() ).hexdigest()
            # save file
            self._save_file( m, file="addons2.xml.md5" )
        except Exception, e:
            # oops
            print "An error occurred creating addons.xml.md5 file!\n%s" % ( e, )

    def _save_file( self, data, file ):
        try:
            # write data to the file
            open( file, "w" ).write( data )
        except Exception, e:
            # oops
            print "An error occurred saving %s file!\n%s" % ( file, e, )


if ( __name__ == "__main__" ):
    # start
    Generator()
