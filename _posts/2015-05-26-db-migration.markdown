---
layout: post
title:  "Phalcon Jumpstart - DB Migration"
date:   2015-05-26
description: Migrations are a convenient way for you to alter your database in a structured and organized manner.
comments: true
---

<p class="intro">
    <span class="dropcap">M</span>
    igrations are a convenient way for you to alter your database in a structured and organized manner.
</p>

Migrations are a convenient way for you to alter your database in a structured and organized manner.

Often in development we need to update changes in production environments. Some of these changes could be database modifications like new fields, new tables, removing indexes, etc.

When a migration is generated a set of classes are created to describe how your database is structured at that moment. These classes can be used to synchronize the schema structure on remote databases setting your database ready to work with the new changes that your application implements. Migrations describe these transformations using plain PHP.

Write JSON structure
----

In this framework, have 6 tables existed, you can see it in ***/migration/structure.json***. And you want create a new table name ***fly_product***, you need write a new block like below:

{% highlight json %}
"0007": {
        "prefix": "p",
        "table": "fly_product",
        "alias": "",
        "model": "",
        "description": "Add the fly_product table \n",
        "comment": "",
        "common": false,
        "fields": [
                {
                "sql": "[prefix]_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT",
                "name": "id",
                "validator": "int",
                "common": true,
                "description": ""
            },
            {
                "sql": "[prefix]_name INT(11) UNSIGNED NOT NULL",
                "name": "version",
                "validator": "string",
                "common": true,
                "description": ""
            }
        ],
        "indexes": [
            "PRIMARY KEY ([prefix]_id)"
        ],
        "relationships": [
        ],
        "data": [
        ]
    }
{% endhighlight %}

Then you want to have new table in MySQL database, simply run following command in terminal

```
php cli/cli.php migrate rebuild
```

Write JSON Data
----
You need the many example data to test, after export JSON data from ***phpMyAdmin***, open file ***/migration/data.json*** and paste the content follow structure

{% highlight json %}
{
    "<table_name>": [{<json_data>}]
}
{% endhighlight %}

Then run following command in terminal to load JSON data to MySQL database

```
php cli/cli.php migrate load
```

### Important note
- Write database JSON structure need remove "," character at the end of a block object, array.
- Any INTEGER field in database not null, need to Zero (0) if NULL.