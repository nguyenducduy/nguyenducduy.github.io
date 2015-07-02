---
layout: post
title:  "Phalcon Jumpstart - CRUD Generator"
date:   2015-05-26
description: Phalcon Jumpstart DevTool comes with a very powerful tool that is in the Admin Panel Code Generator. Code Generator to automatically create tables in the database from the Model and Controller together with the creation of the Admin Module to manage (list, add, edit, delete) to saving time to build basic administrator function.
comments: true
---

<p class="intro">
    <span class="dropcap">P</span>
    halcon Jumpstart DevTool comes with a very powerful tool that is in the Admin Panel Code Generator. Code Generator to automatically create tables in the database from the Model and Controller together with the creation of the Admin Module to manage (list, add, edit, delete) to saving time to build basic administrator function.
</p>

Phalcon Jumpstart DevTool comes with a very powerful tool that is in the Admin Panel Code Generator. Code Generator to automatically create tables in the database from the Model and Controller together with the creation of the Admin Module to manage (list, add, edit, delete) to saving time to build basic administrator function.

When accessing the path ***/admin/codegenerator*** , you will be asked to select generate from table to continue.
<figure>
    <img src="{{ '/uploads/pj/codegenerator-select-table.png' | prepend: site.baseurl }}" alt="Code Generator Select Table">
    <figcaption>Fig1. - Code Generator Select Table.</figcaption>
</figure>

After selecting the table, you start to generate management Model and Controller.

GENERATOR

Code generator allows you to create a Model class and has the corresponding processing lists, add, delete, edit ... similar to the concept in some ORM framework.

Generator will automatically analyze the table you choose and make available copies of class attribute mapping Model name from the table. The system will automatically fill help attribute names.
The figure below describes the process of setting ***fly_post*** table before initializing class ***\Model\Post.php***

Attached to generate Model Class, generator also generate additional administrative functions of this model, including controller, creating language files, interfaces listed, add, edit ...

<figure>
    <img src="{{ '/uploads/pj/post-generate.png' | prepend: site.baseurl }}" alt="Post Table Generate Setting">
    <figcaption>Fig2. - Post Table Generate Setting.</figcaption>
</figure>

After save success full.

<figure>
    <img src="{{ '/uploads/pj/post-generate-success.png' | prepend: site.baseurl }}" alt="Post Table Generate Success">
    <figcaption>Fig3. - Post Table Generate Success.</figcaption>
</figure>