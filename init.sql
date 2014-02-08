CREATE TABLE `overtime` (
      `month` varchar(11) DEFAULT '',
      `day` varchar(11) NOT NULL DEFAULT '',
      `overtime` tinyint(1) DEFAULT '0',
      PRIMARY KEY (`day`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
