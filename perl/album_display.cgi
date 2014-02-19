#!/usr/bin/perl -w

### This .cgi file is used to display the photos inside the album    ###
### 1. To view the album                                             ###
### 2. Remove photos from the album                                  ###
### 3. Only the inputs shown in the page is valid                    ###
### 4. The valid range for row and column is 1-9 inclusively         ###
### 5. Split in to pages if the number of photos in the album is     ###
###    larger than row*column                                        ###
### 6. Sort the display, sort by size, by name, by upload time.      ###
###    descending/ascending                                          ###
### 7. Display thumbnails only                                       ###
### 8. Display description of the photo when mouse move to the photo ###
### 9. Click and display the target photo                            ###
### 10. For un-authorized user, the album is read only               ###

use strict;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

my $CGI_o = CGI->new();
my $option_r = $CGI_o->param('option_r');
my $option_c = $CGI_o->param('option_c');
my $option_sort = $CGI_o->param('option_sort');
my $option_order = $CGI_o->param('option_order');
my $option_page = $CGI_o->param('option_page');

print $CGI_o->header();

print <<__html_file__;
<html>
    <body>
        <title>Album Display Interface</title>
        <p>Album Display Interface</p>
        <form method="POST" action="album_display.cgi">
            <fieldset>
            <legend>Album Display Interface:</legend><br/>
            Dimension
            <select name="option_r" autofocus>
__html_file__

my $i;
for($i = 1; $i < 10; $i++)
{
    print "<option value=$i>$i</option>";
}

print <<__html_file__;
            </select>
            X
            <select name="option_c" autofocus>
__html_file__

for($i = 1; $i < 10; $i++)
{
    print "<option value=$i>$i</option>";
}

print <<__html_file__;
            </select>
            &nbsp;&nbsp;&nbsp;&nbsp;Sort By
            <select name="option_sort" autofocus>
            <option value="1">File Size</option>
            <option value="2">Name</option>
            <option value="3">Upload Time</option>
            </select>
            &nbsp;&nbsp;&nbsp;&nbsp;Order
            <select name="option_order" autofocus required>
            <option value="1">Ascending</option>
            <option value="2">Descending</option>
            </select>

            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" name="change" value="Change"/>
__html_file__

print "<br/>option_r = $option_r<br/>option_c = $option_c<br/>option_sort = $option_sort<br/>option_order = $option_order<br/>option_page=$option_page<br/>";



###TODO



print <<__html_file__;
            <input type="submit" name="remove" value="Remove Selected"/>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Page
            <select name="option_page" autofocus>
__html_file__

for($1 = 1; $i < 4; $i++)
{
    print "<option value=$i>$i</option>&nbsp;&nbsp;&nbsp;&nbsp;of&nbsp;&nbsp;&nbsp;&nbsp;4";
}

print <<__html_file__;
            </select>
            <input type="submit" name="page" value="Go to Page"/>
__html_file__

print <<__html_file__;
            #<input type="hidden" name="last_option_r" value="">
            #<input type="hidden" name="last_option_c" value="">
            #<input type="hidden" name="last_option_sort" value="">
            #<input type="hidden" name="last_option_order" value="">
            #<input type="hidden" name="last_option_page" value="">
__html_file__

print <<__html_file__;
            </fieldset>
        </form>
    </body>
</html>
__html_file__
#if __html_file__ is the last, then must add a new line