overtimecnt
===========

<p>statistics overtime days per month</p>

<p>Using your database engines admin interface, create a simple table in your database:</p>
<pre>
<code>
"CREATE TABLE `overtime` (
  `month` varchar(11) DEFAULT '',
  `day` varchar(11) DEFAULT '',
  `overtime` tinyint(1) DEFAULT '0',
   PRIMARY KEY (`day`)
) ENGINE=MyISAM DEFAULT CHARSET=latin;"
</code>
</pre>

<p>And an initial row:</p>
<pre>
<code>
insert into overtime (month, day, overtime) values('201402', '20140201', 0);
</code>
</pre>


