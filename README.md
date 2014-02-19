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

<p>Return to overtime.py to change the datebase config, while the forsae branch you do not need to change it.</p>
<pre>
<code>
db = web.database(dbn='mysql', user='db_user', pw='db_pwd', db='db_dbname')
</code>
</pre>

<p>The value of the overtime in database is 0 means "work normal" whereas 1 means "work overtime".</p>
<p>Run server:</p>
<pre>
<code>
python overtime.py  port
</code>
</pre>
