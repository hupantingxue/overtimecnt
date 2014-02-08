overtimecnt
===========

statistics overtime days per month

Using your database engines admin interface, create a simple table in your database:
CREATE TABLE `overtime` (
  `month` varchar(11) DEFAULT '',
  `day` varchar(11) DEFAULT '',
  `overtime` tinyint(1) DEFAULT '0',
   PRIMARY KEY (`day`)
) ENGINE=MyISAM DEFAULT CHARSET=latin;

And an initial row:
insert into overtime (month, day, overtime) values('201402', '20140201', 0);


