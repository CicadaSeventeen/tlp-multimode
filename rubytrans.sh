#!/bin/sh
input_name=$1
short_name=$(basename $input_name | sed 's/\.[^.]*$//')
formart=$2
case $formart in
	'rb'|'ruby')
		formart='ruby'
		output_name="$short_name"'.rb'
		awk '
BEGIN {
    print "#!/usr/bin/env ruby"
    map["#FILE_REALPATH"] = "File.realpath"
    map["#FILE_EXIST"] = "File.exist"
    map["#REQUIRE_FILEUITILS"] = "require \"fileutils\""
    map["#REQUIRE_OPTPARSE"] = "require \"optparse\""
    map["#PARSER_PARSE_ARGV"] = "parser.parse!(ARGV)"
    map["#GET_PROFILE_NAME"] = "profile_name=ARGV.shift"
    map["#SYSTEM"] = "system"
}
{
    for (pattern in map) {
        gsub(pattern, map[pattern])
    }
    print
}' 		$input_name > $output_name
		;;

	'cr'|'cy'|'crystall')
			formart='crystall'
			output_name="$short_name"'.cr'
			awk '
BEGIN {
    print "lib LibC"
    print "  fun setuid(uid : UInt32) : Int32"
    print "  fun system(command : UInt8*) : Int32"
    print "  fun exit(status : Int32) : NoReturn"
    print "end"
    print "def c_system(string)"
    print "  LibC.setuid(0)"
    print "  LibC.system(string)"
    print "end"
    map["#FILE_REALPATH"] = "File.realpath"
    map["#FILE_EXIST"] = "File.exists"
    map["#REQUIRE_FILEUITILS"] = "require \"file_utils\""
    map["#REQUIRE_OPTPARSE"] = "require \"option_parser\""
    map["#PARSER_PARSE_ARGV"] = "parser.parse(ARGV)"
    map["#GET_PROFILE_NAME"] = "profile_name=ARGV.shift?||\"\""
    map["#SYSTEM"] = "c_system"
}
{
    for (pattern in map) {
        gsub(pattern, map[pattern])
    }
    print
}' 		$input_name > $output_name
		;;
    "all"|"a")
        bash $0 $1 'ruby'
        bash $0 $1 'crystall'
    ;;
esac

