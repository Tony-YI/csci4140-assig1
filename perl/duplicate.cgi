#!/usr/bin/perl -w

use strict;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

require "./lib.pl";

my $CGI_o = CGI->new();

my $user_name = $CGI_o->param("user_name");
my $file_name = $CGI_o->param("file_name");
my $description = $CGI_o->param("description");


print $CGI_o->header();

print "$user_name $file_name $description<br/>";

###TODO: get back the uploaded file. how? old query? or sotre in the tmp file first?
###########################
open(INFILE, "<", "$file_name");
my $buffer;
my $ret = read(INFILE, $buffer, 1024);
print "$ret<br/>";
close(INFILE);
###########################
print <<__html_file__;
<html>
    <body>
        "$user_name"<br/>
        "$file_name"<br/>
        "$description"<br/>
    </body>
</html>
__html_file__
#if end with __html_file__, must add a new line