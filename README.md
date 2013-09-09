This tool calls `install_name_tool -change` for each library or
executable, replacing the specified string in any matched library
names.  It can be used for example to change library linkage to
`@executable_path/../Resources` when creating an app bundle.

Usage:

    relocate_libs <from-string> <to-string> <libanything.dylib ..>

Example:

    relocate_libs /usr/local/lib @executable_path/../Resources/lib *.dylib

This will take all matching `.dylib` files and replace the prefix
`/usr/local/lib` in any of the linkage.  You can look at the linkage
to dependent libraries using the command `otool -L`.  Try using `otool
-L` on a library before and after running this tool.

The source can be found at http://github.com/radarsat1/relocate_libs

Stephen Sinclair, 2013
radarsat1@gmail.com
